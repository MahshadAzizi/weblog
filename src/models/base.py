from datetime import datetime
import uuid as uuid
from sqlalchemy import Column, TIMESTAMP, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from pytz import timezone

UTC = timezone('UTC')


def time_now():
    return datetime.now(UTC)


class DBBase:
    """Base class for all db orm models"""
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), default=time_now, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), default=time_now, onupdate=time_now, nullable=False)
    is_deleted = Column(Boolean, default=False)
