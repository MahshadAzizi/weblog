from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from .base import DBBase
from ..config.engine import Base

# Declare Classes / Tables
article_tags = Table('article_tags', Base.metadata,
                     Column('article_id', ForeignKey('article.id'), primary_key=True),
                     Column('tag_id', ForeignKey('tag.id'), primary_key=True)
                     )


class Article(DBBase, Base):
    __tablename__ = 'article'

    owner_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255), nullable=False)
    description = Column(String(5000), nullable=True)

    owner = relationship("User", back_populates="articles")
    tag = relationship("Tag", secondary="article_tags", back_populates='articles')


class Comment(DBBase, Base):
    __tablename__ = 'comment'

    description = Column(String(5000), nullable=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="comment")

    article_id = Column(Integer, ForeignKey("article.id"))
    article = relationship("Article", back_populates="comments")


class Tag(DBBase, Base):
    __tablename__ = 'tag'

    article = relationship("Article", secondary="article_tags", back_populates='tags')
    name = Column(String(20), nullable=False)


class Like(DBBase, Base):
    __tablename__ = 'like'

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="like")
    article_id = Column(Integer, ForeignKey("article.id"))
    article = relationship("Article", back_populates="likes")
