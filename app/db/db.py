from app.utils import get_db_url
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)