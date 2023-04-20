from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, Text, URL, DATE, INTEGER, FLOAT
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from storage import Base

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text, unique=True)
    description: Mapped[Optional[str]]
    posted_date: Mapped[Optional[int]]
    deadline: Mapped[Optional[int]]
    expected_time_limit: Mapped[Optional[int]]
    price_fixed: Mapped[Optional[float]]
    price_fixed_min: Mapped[Optional[float]]
    price_hourly: Mapped[Optional[float]]
    price_hourly_min: Mapped[Optional[float]]
    tags: Mapped[List["Tag"]] = relationship(
         back_populates="project", cascade="all, delete-orphan")

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    project: Mapped["Project"] = relationship( back_populates="tags")


