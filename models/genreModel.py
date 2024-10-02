from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Genre(Base):
  __tablename__ = "Genres"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(db.String(255))
  
  movies: Mapped[List['Movie']] = db.relationship('Movie', back_populates='genre')