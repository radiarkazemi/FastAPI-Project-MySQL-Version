from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import posts, user, auth, vote
from . import models, database

# models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def test():
    return {"message": "Everything is Ok!"}
