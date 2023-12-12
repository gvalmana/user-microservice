from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy import String
from uuid import uuid4
from sqlalchemy import MetaData

class Base(object):
    uid: Mapped[str] = mapped_column(String(50), init=False, default_factory=uuid4, primary_key=True)
    created_at: Mapped[datetime] | datetime | None = Column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] | datetime | None = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    is_deleted: Mapped[bool] | bool | None = Column(Boolean, default=False)
    metadata = MetaData()
