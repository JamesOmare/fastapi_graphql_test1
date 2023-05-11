from fastapi import FastAPI

import strawberry
from strawberry.asgi import GraphQL


@strawberry.type
class Query:
  @strawberry.field
  def hello(self) -> str:
    return "Hello World"


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()


app.add_route("/graphql", graphql_app)

# import graphene
# from fastapi import FastAPI
# from starlette_graphene3 import GraphQLApp

# app = FastAPI()

# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema()))