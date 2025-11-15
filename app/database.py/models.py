from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine 


ENGINE = create_async_engine("mysql+pymysql://root:HIGHT99900HIGHT@localhost:3306/tasks", echo=True)