from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=True)
    title = Column(String, nullable=True)
    content = Column(String, nullable=True)
    published = Column(Boolean, default=True)
