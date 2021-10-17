from ariadne import QueryType, make_executable_schema, ObjectType
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from routers import recordings, masters
from routers.retrieval import find_recordings_by_show_title, find_recordings_by_show_title_and_production
from util.data import load_recordings_from_json, clear_recordings

app = FastAPI()

app.include_router(recordings.router)
app.include_router(masters.router)

json_path = 'data.json'


@app.on_event("startup")
def startup_event():
    load_recordings_from_json(json_path)


@app.on_event("shutdown")
def shutdown_event():
    clear_recordings()


type_defs = """
    type Query {
        recordings(title: String!, production: String): [Show]
    }
    
    type Show {
        title: String!
        production: String!
        cast: [[String]]
        type: ShowType!
        id: ID!        
    }
    
    type ShowType {
        recording: Recording!
        completeness: Completeness!
        authorship: Authorship!    
    }
    
    enum Recording {
        audio
        video
    }
    
    enum Completeness {
        full
        highlights
    }
    
    enum Authorship {
        proshot
        bootleg
    }
"""

query = QueryType()


@query.field("recordings")
def resolve_recordings(*_, title, production=None):
    if production is not None:
        return find_recordings_by_show_title_and_production(title, production)
    return find_recordings_by_show_title(title)


show = ObjectType("Show")


@show.field("cast")
def resolve_recordings(obj, *_):
    return list(map(list, obj.cast.items()))


schema = make_executable_schema(type_defs, query, show)

app.mount("/graphql", GraphQL(schema, debug=True))
