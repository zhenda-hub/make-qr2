"""QR Code Generator API.

This module provides a FastAPI application for generating QR codes with
customization options and storing them in a SQLite database.
"""

import logging
import os
import uuid
from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import qrcode
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
SQLALCHEMY_DATABASE_URL = os.getenv(
    "SQLALCHEMY_DATABASE_URL",
    "sqlite:///./sql_app.db"
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_pre_ping=True
)

# Create database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database error: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()


# Database Models
class QRCode(Base):
    """QR Code database model."""
    __tablename__ = "qrcodes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500), index=True, nullable=False)
    image_path = Column(String(500), unique=True, nullable=False)
    fg_color = Column(String(7), default="#000000")
    bg_color = Column(String(7), default="#FFFFFF")
    size = Column(Integer, default=200)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return f"<QRCode(id={self.id}, url='{self.url}')>"

    @classmethod
    def create_qr_code(
        cls,
        db: Session,
        url: str,
        size: int,
        fg_color: str,
        bg_color: str,
        image_path: str
    ) -> 'QRCode':
        """Create a new QR code record in the database."""
        db_qr = cls(
            url=url,
            size=size,
            fg_color=fg_color,
            bg_color=bg_color,
            image_path=image_path
        )
        db.add(db_qr)
        db.commit()
        db.refresh(db_qr)
        return db_qr

    @classmethod
    def get_qr_code(
        cls,
        db: Session,
        qr_id: int
    ) -> Optional['QRCode']:
        """Get a QR code by ID."""
        return db.query(cls).filter(cls.id == qr_id).first()

    @classmethod
    def get_recent_qr_codes(
        cls,
        db: Session,
        limit: int = 10
    ) -> List['QRCode']:
        """Get most recent QR codes."""
        return db.query(cls).order_by(
            cls.created_at.desc()
        ).limit(limit).all()



class Page(Base):
    """Page database model for storing website pages."""
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, index=True, nullable=False)
    content = Column(String(5000))
    is_published = Column(Integer, default=1)  # 1 = published, 0 = draft
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Page(id={self.id}, title='{self.title}')>"

    @classmethod
    def create_page(
        cls,
        db: Session,
        title: str,
        content: str,
        slug: str = None
    ) -> 'Page':
        """Create a new page in the database."""
        if not slug:
            slug = f"{title.lower().replace(' ', '-')}-{uuid.uuid4().hex[:6]}"

        db_page = cls(
            title=title,
            content=content,
            slug=slug
        )
        db.add(db_page)
        db.commit()
        db.refresh(db_page)
        return db_page

    @classmethod
    def get_page(
        cls,
        db: Session,
        page_id: int = None,
        slug: str = None
    ) -> Optional['Page']:
        """Get a page by ID or slug."""
        if page_id:
            return db.query(cls).filter(cls.id == page_id).first()
        if slug:
            return db.query(cls).filter(
                cls.slug == slug,
                cls.is_published == 1
            ).first()
        return None

    @classmethod
    def list_pages(
        cls,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        published_only: bool = True
    ) -> List['Page']:
        """List pages with pagination and optional published filter."""
        query = db.query(cls)
        if published_only:
            query = query.filter(cls.is_published == 1)
        return query.order_by(
            cls.updated_at.desc()
        ).offset(skip).limit(limit).all()

    @classmethod
    def update_page(
        cls,
        db: Session,
        page_id: int,
        **kwargs
    ) -> Optional['Page']:
        """Update page fields."""
        db_page = cls.get_page(db, page_id=page_id)
        if not db_page:
            return None

        for key, value in kwargs.items():
            if hasattr(db_page, key):
                setattr(db_page, key, value)

        db_page.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_page)
        return db_page

    @classmethod
    def delete_page(cls, db: Session, page_id: int) -> bool:
        """Delete a page by ID."""
        db_page = cls.get_page(db, page_id=page_id)
        if not db_page:
            return False

        db.delete(db_page)
        db.commit()
        return True

def init_db():
    # 创建数据库表
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created")

# 初始化数据库
init_db()

app = FastAPI(
    title="QR Code Generator API",
    description="API for generating and managing QR codes and pages",
    version="1.0.0"
)

# 创建必要的目录
os.makedirs("generated_qrcodes", exist_ok=True)
os.makedirs("uploads", exist_ok=True)

# 配置静态文件路由
app.mount("/qrcodes", StaticFiles(directory="generated_qrcodes"), name="qrcodes")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

# 请求模型
class QRCodeCreate(BaseModel):
    url: str = Field(..., max_length=500)
    size: int = Field(200, ge=100, le=1000)
    fg_color: str = Field("#000000", regex=r'^#(?:[0-9a-fA-F]{3}){1,2}$')
    bg_color: str = Field("#FFFFFF", regex=r'^#(?:[0-9a-fA-F]{3}){1,2}$')

class PageCreate(BaseModel):
    title: str = Field(..., max_length=200)
    content: str = Field(..., max_length=5000)
    slug: Optional[str] = Field(None, max_length=200)
    is_published: bool = True

class PageUpdate(PageCreate):
    title: Optional[str] = Field(None, max_length=200)
    content: Optional[str] = Field(None, max_length=5000)

# 响应模型
class QRCodeResponse(BaseModel):
    id: int
    url: str
    image_url: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class PageResponse(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    is_published: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

# 配置
QR_CODE_DIR = "generated_qrcodes"
UPLOAD_DIR = "uploads"
ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# 确保目录存在
os.makedirs(QR_CODE_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

def cleanup_old_files(directory: str, hours: int = 24):
    """清理指定目录中超过指定小时的文件"""
    now = datetime.now()
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            if os.path.isfile(filepath):
                file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                if now - file_time > timedelta(hours=hours):
                    os.remove(filepath)
                    logger.info(f"Removed old file: {filepath}")
        except Exception as e:
            logger.error(f"Error removing file {filepath}: {str(e)}")

def get_file_extension(filename: str) -> str:
    return filename.split('.')[-1].lower()

def is_allowed_file(filename: str) -> bool:
    return '.' in filename and get_file_extension(filename) in ALLOWED_IMAGE_EXTENSIONS

@app.on_event("startup")
async def startup_event():
    """应用启动时执行的任务"""
    # 清理旧文件
    cleanup_old_files(QR_CODE_DIR, hours=24)
    cleanup_old_files(UPLOAD_DIR, hours=24)
    logger.info("Application startup: Cleaned up old files")

@app.get("/api/health")
async def health_check():
    """健康检查端点"""
    return {"status": "ok", "timestamp": datetime.utcnow()}

@app.post("/api/qrcode", response_model=QRCodeResponse)
async def generate_qrcode(
    qr_data: QRCodeCreate,
    db: Session = Depends(get_db)
):
    """
    生成新的二维码
    """
    try:
        # 生成唯一文件名
        filename = f"{uuid.uuid4().hex}.png"
        filepath = os.path.join(QR_CODE_DIR, filename)
        
        # 生成二维码
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        qr.add_data(qr_data.url)
        qr.make(fit=True)
        
        # 处理颜色
        fg_color = qr_data.fg_color.lstrip('#')
        bg_color = qr_data.bg_color.lstrip('#')
        
        # 创建二维码图片
        qr_img = qr.make_image(
            fill_color=f"#{fg_color}",
            back_color=f"#{bg_color}"
        )
        
        # 调整大小
        qr_img = qr_img.resize((qr_data.size, qr_data.size))
        
        # 保存图片
        qr_img.save(filepath)
        
        # 保存到数据库
        image_url = f"/qrcodes/{filename}"
        db_qr = QRCode.create_qr_code(
            db=db,
            url=qr_data.url,
            size=qr_data.size,
            fg_color=qr_data.fg_color,
            bg_color=qr_data.bg_color,
            image_path=image_url
        )
        
        return {
            "id": db_qr.id,
            "url": db_qr.url,
            "image_url": image_url,
            "created_at": db_qr.created_at
        }
        
    except Exception as e:
        logger.error(f"Error generating QR code: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate QR code"
        )

# 页面管理API
@app.post("/api/pages/", response_model=PageResponse, status_code=status.HTTP_201_CREATED)
def create_page(
    page: PageCreate,
    db: Session = Depends(get_db)
):
    """
    创建新页面
    """
    try:
        db_page = Page.create_page(
            db=db,
            title=page.title,
            content=page.content,
            slug=page.slug
        )
        if not page.is_published:
            db_page.is_published = 0
            db.commit()
            db.refresh(db_page)
        return db_page
    except Exception as e:
        logger.error(f"Error creating page: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create page"
        )

@app.get("/api/pages/", response_model=List[PageResponse])
def list_pages(
    skip: int = 0,
    limit: int = 10,
    published_only: bool = True,
    db: Session = Depends(get_db)
):
    try:
        pages = db.query(Page).all()
        return pages
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"获取页面列表失败: {str(e)}"
        )
