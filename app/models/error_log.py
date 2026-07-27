from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class ErrorLog(Base):
    __tablename__ = "error_logs"

    id = Column(Integer, primary_key=True, index=True)

    endpoint = Column(String(255))

    method = Column(String(20))

    error_message = Column(Text)

    stack_trace = Column(Text)

    user_id = Column(Integer, nullable=True)

    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)