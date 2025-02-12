from typing import Dict, Any
from sqlalchemy.orm import Mapped, DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs
from .annotations import create_time, update_time


class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    create_time: Mapped[create_time]
    update_time: Mapped[update_time]
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
    
    def to_dict(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}