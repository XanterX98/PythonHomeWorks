"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    relationship,
    sessionmaker,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
PG_ASYNC_CONN_URI = "postgresql+asyncpg://username:passwd!@localhost:5432/blog"


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> users
        Author -> authors
        """
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(url=PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine, cls=Base)


async_engine = create_async_engine(
    PG_ASYNC_CONN_URI,
    echo=True,
)
Session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class User(Base):
    name = Column(String(30))
    username = Column(String(30), unique=True)
    email = Column(String(100), unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name!r}"
            f"username={self.username!r}"
            f"email={self.email!r}"
            ")"
        )


class Post(Base):
    user_id = Column(
        Integer(),
        ForeignKey("users.id"),
        nullable=False,
        unique=False,
    )
    title = Column(String(200))
    body = Column(String())

    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"user_id={self.user_id!r}"
            f"title={self.title!r}"
            f"body={self.body!r}"
            ")"
        )
