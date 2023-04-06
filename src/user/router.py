from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import false, true
from sqlalchemy.orm import Session

from src.user.model import User
from src.user.schema import LoggedInUser, UserCreate, UserLogin, UserResponse, UserTable
from src.utils.current_user import get_current_user
from src.utils.db_session_create import get_db
from src.utils.hahspassword import get_password_hash, verify_password
from src.utils.token import create_access_token

user_router = APIRouter()


# user routes
# get all users that are not deleted
@user_router.get(
    "/users/all", status_code=status.HTTP_200_OK, response_model=List[UserResponse]
)
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_deleted != true()).all()
    return users


# get 1 user that is not not deleted
@user_router.get("/get/user/{id}", status_code=status.HTTP_200_OK)
async def get_user(id: str, db: Session = Depends(get_db)):
    one_user = db.query(User).filter(User.id == id, User.is_deleted != true()).first()
    if one_user:
        return one_user
    else:
        return {"message": "user is already deleted"}


# get only users that are deleted
@user_router.get("/users/del", status_code=200, response_model=List[UserResponse])
async def get_all_deleted_users(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_deleted == true()).all()
    if users:
        return users
    else:
        return {"message": "User might not be deleted or some other error"}


# admin function to see full data
@user_router.get("/admin/users/all")
async def admin_get_all(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_deleted != true()).all()
    return users


# create new user and provide their details
@user_router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    try:
        if db_user:
            return {"message": "user already exists with this email id"}
        else:
            new_user = User(
                name=user.name,
                password=get_password_hash(user.password),
                email=user.email,
            )

            db.add(new_user)

            db.commit()
            return {"message": "user created successfully"}
    except Exception as e:
        return e
    finally:
        db.close()


# update user and their desired values
@user_router.put("/user/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(id: str, user: UserTable, db: Session = Depends(get_db)):
    updateuser = (
        db.query(User).filter(User.id == id, User.is_deleted == false()).first()
    )

    if updateuser:
        updateuser.update_fields(user.dict())
        db.add(updateuser)
        db.commit()
        return {"message": "user details updated"}

    else:
        return {"message : User is deleted so cannot update"}


# delete user that you want to
@user_router.delete("/user/del/{id}")
async def delete_user(id: str, db: Session = Depends(get_db)):
    deleteuser = db.query(User).filter(User.id == id).first()

    if deleteuser.is_deleted is not True:
        deleteuser.is_deleted = True
        db.commit()
        return {"message": "user deleted successfully"}

    elif deleteuser.is_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user is already deleted"
        )


# user login api
@user_router.post("/user/login", status_code=status.HTTP_200_OK)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # breakpoint()
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user and verify_password(user.password, db_user.password):
        return {
            "message": "user login successful",
            "access_token": create_access_token(
                subject={"id": db_user.id, "email": db_user.email}
            ),
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found, please check credentials and try again",
        )


@user_router.get(
    "/user/me", status_code=status.HTTP_200_OK, response_model=LoggedInUser
)
async def display_user(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return {"email": f"{current_user}"}
