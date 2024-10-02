from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column,relationship

class Movie(Base):
  __tablename__ = 'Movies'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(db.String(255))
  director: Mapped[str] = mapped_column(db.String(255))
  year: Mapped[int] = mapped_column(db.Integer)
  genre_id: Mapped[int] = mapped_column(db.ForeignKey('Genres.id'))
  
  genre: Mapped['Genre'] = db.relationship(back_populates='movies', lazy='joined')