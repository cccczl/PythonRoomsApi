from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    """Default usefull entities timestamps"""

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
