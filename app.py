from database import db
from flask import Flask
from flask_graphql import GraphQLView
import graphene
from resolvers.query import Query
from utilities.mutation import Mutation


def create_app(config_name):
  app = Flask(__name__)
  
  app.config.from_object(f'config.{config_name}')
  db.init_app(app)
  
  schema = graphene.Schema(query=Query, mutation=Mutation)

  app.add_url_rule(
      '/graphql/movies',
      view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
  )

  return app

if __name__ == '__main__':
  app = create_app('DevelopmentConfig')
  
  with app.app_context():
    db.create_all()
    
  app.run(debug=True)