from fastapi import APIRouter, Depends, status
from app.user.model import UserDetails
from app.user.schema import UserTable, UserResponse, UserCreate
from app.utils.db_session_create import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List


userRouter = APIRouter()


# user routes
# get all users that are not deleted #testing done
@userRouter.get('/users/all', status_code = status.HTTP_200_OK, response_model=  List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserDetails).filter(UserDetails.is_deleted != True).all()
    return users


# get 1 user that is not not deleted #testing done
@userRouter.get('/get/user/{user_id}', status_code = status.HTTP_200_OK, response_model= UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    one_user = db.query(UserDetails).filter(
        UserDetails.user_id == user_id, UserDetails.is_deleted != True).first()
    if one_user:
        return one_user


# get only users that are deleted #testing done
@userRouter.get('/users/del', status_code=200, response_model= List[UserResponse])
def get_all_deleted_users(db: Session = Depends(get_db)):
    users = db.query(UserDetails).filter(UserDetails.is_deleted == True).all()
    if users:
        return users
    else:
        return {"message": "User might not be deleted or some other error"}


#admin function to see full data #testing done
@userRouter.get('/admin/users/all')
def admin_get_all(db: Session = Depends(get_db)):
        users = db.query(UserDetails).filter(UserDetails.is_deleted != True).all()
        return users


# create new user and provide their details
@userRouter.post('/users', status_code= status.HTTP_201_CREATED, response_model= list[UserResponse])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserDetails).filter(
        UserDetails.email == user.email).first()

    if db_user:
        return {"message: User already exists"}
    else:
        new_user = UserDetails(
            name = user.name,
            password = user.password,
            email = user.email)
        db.add(new_user)
        db.commit()
        return new_user



# update user and their desired values #testing done for updating one user at once
@userRouter.put('/user/{user_id}', status_code= status.HTTP_202_ACCEPTED, response_model= UserResponse)
def update_user(user_id: str, user: UserTable, db: Session = Depends(get_db)):
    updateuser = db.query(UserDetails).filter(
        UserDetails.user_id == user_id, UserDetails.is_deleted == False).first()

    if updateuser:
        updateuser.update(user.dict())
        db.add(updateuser)
        db.commit()
        return updateuser
        
    else:
        return {f"message : User with user_id: {user_id} is deleted so cannot update"}



# delete user that you want to #testing done
@userRouter.delete('/user/del/{user_id}', response_model= UserResponse)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    deleteuser = db.query(UserDetails).filter(
        UserDetails.user_id == user_id).first()

    if deleteuser.is_deleted != True:
        deleteuser.is_deleted = True
        db.commit()
        return deleteuser

    elif deleteuser.is_deleted == True:
        return deleteuser


# end of user routes
