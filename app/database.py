from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, select
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BD_PATH = os.path.join(BASE_DIR, "..", "data.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)


engine = create_async_engine(f"sqlite+aiosqlite:///{BD_PATH}", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

async def add_user(name,phone):
    async with async_session() as session:
        statement = select(User).where(User.phone == phone)
        result = await session.execute(statement)
        existing_user = result.scalar_one_or_none()

        if existing_user:
            return False

        new_user = User(name=name, phone=phone)
        session.add(new_user)
        await session.commit()
        return True

async def get_all_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        return result.scalars().all()

