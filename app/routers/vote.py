from fastapi import APIRouter, HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from .. import schemas, oauth2, models

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(votes: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(type(votes.post_id))
    print(type(models.Post.id))
    print(votes.post_id)
    print(models.Post.id)
    post = db.query(models.Vote).filter(models.Post.id == votes.post_id).first()
    post_test = db.query(models.Vote).filter(models.Post.id == votes.post_id).first()
    print(post_test)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post With Id  {votes.post_id} Does Not Exist!")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == votes.post_id,
                                              models.Vote.user_id == current_user.id)
    print(vote_query)
    found_vote = vote_query.first()

    if votes.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"User {current_user.id} Has Already Vote on Post {votes.post_id}")

        new_post = models.Vote(post_id=votes.post_id, user_id=current_user.id)
        db.add(new_post)
        db.commit()
        return {"Message": "Successfully Added Vote!"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote Does Not Exist!")

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message": "Successfully Deleted Vote!"}
