import graphene
from database import db
from models.movieModel import Movie as MovieModel
from models.genreModel import Genre as GenreModel
from models.schemas.movieSchema import Movie
from models.schemas.genreSchema import Genre


class Query(graphene.ObjectType):
    movies = graphene.List(Movie)
    movieById = graphene.Field(Movie, id=graphene.Int(required=True))
    getMoviesByGenre = graphene.List(Movie, genreId=graphene.Int(required=True))
    genres = graphene.List(Genre)
    genreById = graphene.Field(Genre, id=graphene.Int(required=True))
    getGenreByMovie = graphene.Field(Genre, movieId=graphene.Int(required=True))

    def resolve_movies(self, info):
        return db.session.execute(db.select(MovieModel)).scalars()

    def resolve_movieById(self, info, id):
        return db.session.execute(db.select(MovieModel).where(MovieModel.id == id)).scalars().first()

    def resolve_getMoviesByGenre(self, info, genreId):
        return db.session.execute(db.select(MovieModel).where(MovieModel.genre_id == genreId)).scalars()
    
    def resolve_genres(self, info):
        return db.session.execute(db.select(GenreModel)).scalars()

    def resolve_genreById(self, info, id):
        return db.session.execute(db.select(GenreModel).where(GenreModel.id == id)).scalars().first()

    def resolve_getGenreByMovie(self, info, movieId):
        movie = db.session.execute(db.select(MovieModel).where(MovieModel.id == movieId)).scalars().first()
        if movie:
            return db.session.execute(db.select(GenreModel).where(GenreModel.id == movie.genre_id)).scalars().first()
        return None


