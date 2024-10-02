import graphene
from models.schemas.movieSchema import CreateMovie, UpdateMovie, DeleteMovie
from models.schemas.genreSchema import CreateGenre, UpdateGenre, DeleteGenre

class Mutation(graphene.ObjectType):
  create_movie = CreateMovie.Field()
  update_movie = UpdateMovie.Field()
  delete_movie = DeleteMovie.Field()
  create_genre = CreateGenre.Field()
  update_genre = UpdateGenre.Field()
  delete_genre = DeleteGenre.Field()
  