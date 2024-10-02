import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.genreModel import Genre as GenreModel
from database import db
from sqlalchemy.orm import Session

class Genre(SQLAlchemyObjectType):
  class Meta:
    model = GenreModel
  
class CreateGenre(graphene.Mutation):
  class Arguments:
    name = graphene.String(required=True)

  genre = graphene.Field(Genre)

  def mutate(self, info, name):
    with Session(db.engine) as session:
      with session.begin():
        if not name or len(name) > 50:
            raise Exception("Genre name must be non-empty and not exceed 50 characters.")
        genre = GenreModel(name=name)
        session.add(genre)
        session.flush()
      session.refresh(genre)
      return CreateGenre(genre=genre)

class UpdateGenre(graphene.Mutation):
  class Arguments:
    id = graphene.Int(required=True)
    name = graphene.String(required=True)

  genre = graphene.Field(Genre)

  def mutate(self, info, id, name):
    with Session(db.engine) as session:
      with session.begin():
        if not name or len(name) > 50:
          raise Exception("Genre name must be non-empty and not exceed 50 characters.")
        genre = session.execute(db.select(GenreModel).where(GenreModel.id==id)).scalars().first()
        if genre:
          genre.name = name
        else:
          return None
      session.refresh(genre)
    return UpdateGenre(genre=genre)

class DeleteGenre(graphene.Mutation):
  class Arguments:
    id = graphene.Int(required=True)

  success = graphene.Boolean()

  def mutate(self, info, id):
    with Session(db.engine) as session:
      with session.begin():
        genre = session.execute(db.select(GenreModel).where(GenreModel.id==id)).scalars().first()
        if genre:
          session.delete(genre)
        return DeleteGenre(success=True)
      return DeleteGenre(success=False)