from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, Text, URL, DATE, INTEGER, FLOAT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from storage import Base

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    url: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    posted_date: Mapped[Optional[int]]
    deadline: Mapped[Optional[int]]
    expected_time_limit: Mapped[Optional[int]]
    price_fixed: Mapped[Optional[float]]
    price_fixed_min: Mapped[Optional[float]]
    price_hourly: Mapped[Optional[float]]
    price_hourly_min: Mapped[Optional[float]]
    tags: Mapped[Optional[str]]

