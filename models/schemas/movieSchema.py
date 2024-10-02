import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.movieModel import Movie as MovieModel
from database import db
from sqlalchemy.orm import Session

class Movie(SQLAlchemyObjectType):
  class Meta:
    model = MovieModel

class CreateMovie(graphene.Mutation):
  class Arguments:
    title = graphene.String(required=True)
    director = graphene.String(required=True)
    year = graphene.Int(required=True)
    genre_id = graphene.Int(required=True)

  movie = graphene.Field(Movie)

  def mutate(self, info, title, director, year, genre_id):
    with Session(db.engine) as session:
      with session.begin():
        movie = MovieModel(title=title, director=director, year=year, genre_id=genre_id)
        session.add(movie)
        session.flush()
      session.refresh(movie)
      return CreateMovie(movie=movie)

class UpdateMovie(graphene.Mutation):
  class Arguments:
    id = graphene.Int(required=True)
    title = graphene.String()
    director = graphene.String()
    year = graphene.Int()
    genre_id = graphene.Int()

  movie = graphene.Field(Movie)

  def mutate(self, info, id, title=None, director=None, year=None, genre_id=None):
    with Session(db.engine) as session:
      with session.begin():
        movie = session.execute(db.select(MovieModel).where(MovieModel.id == id)).scalars().first()
        if movie:
          if title:
              movie.title = title
          if director:
              movie.director = director
          if year:
              movie.year = year
          if genre_id:
              movie.genre_id = genre_id
        else:
            return None
      session.refresh(movie)
      return UpdateMovie(movie=movie)

class DeleteMovie(graphene.Mutation):
  class Arguments:
    id = graphene.Int(required=True)

  success = graphene.Boolean()

  def mutate(self, info, id):
    with Session(db.engine) as session:
      with session.begin():
        movie = session.execute(db.select(MovieModel).where(MovieModel.id == id)).scalars().first()
        if movie:
          session.delete(movie)
          return DeleteMovie(success=True)
        return DeleteMovie(success=False)