from typing import List
from sqlalchemy.orm import Session
from src.user.model import User
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.utils.db_session_create import get_db
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends, status, HTTPException
from src.user.schema import UserTable, UserResponse, UserCreate, UserLogin


user_router = APIRouter()


outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")


pwd_context = CryptContext(schemes= ["bcrypt"], deprecated= "auto")


def get_password_hash(self, password):
    return self.pwd_context.hash(password)

def verify_password(self, plain_password, hashed_password):
    return self.pwd_context.verify(plain_password, hashed_password)


@user_router.get('/users')
def get_users(token : str= Depends(outh2_scheme)):
    return {"token": token}


# user routes
# get all users that are not deleted 
@user_router.get('/users/all', status_code = status.HTTP_200_OK, response_model= List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_deleted != True).all()
    return users


# get 1 user that is not not deleted 
@user_router.get('/get/user/{id}', status_code = status.HTTP_200_OK)
def get_user(id: str, db: Session = Depends(get_db)):
    one_user = db.query(User).filter(
        User.id == id, User.is_deleted != True).first()
    if one_user:
        return one_user
    else: 
        return {"message" :  "user is already deleted"}



# get only users that are deleted 
@user_router.get('/users/del', status_code=200, response_model= List[UserResponse])
def get_all_deleted_users(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_deleted == True).all()
    if users:
        return users
    else:
        return {"message": "User might not be deleted or some other error"}


#admin function to see full data 
@user_router.get('/admin/users/all')
def admin_get_all(db: Session = Depends(get_db)):
        users = db.query(User).filter(User.is_deleted != True).all()
        return users


# create new user and provide their details
@user_router.post('/users', status_code= status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        User.email == user.email).first()
    try:    
        if db_user:
            return {"message": "user already exists with this email id"}
        else:
            new_user = User(
                name = user.name,
                password = user.password,
                email = user.email)
            
            db.add(new_user)
            
            db.commit()
            return {"message" : "user created successfully"}
    except Exception as e:
        return e



# update user and their desired values
@user_router.put('/user/{id}', status_code= status.HTTP_202_ACCEPTED)
def update_user(id: str, user: UserTable, db: Session = Depends(get_db)):
    updateuser = db.query(User).filter(
        User.id == id, User.is_deleted == False).first()

    if updateuser:
        updateuser.update(user.dict())
        db.add(updateuser)
        db.commit()
        return {"message" : "user details updated"}
        
    else:
        return {"message : User is deleted so cannot update"}



# delete user that you want to
@user_router.delete('/user/del/{id}')
def delete_user(id: str, db: Session = Depends(get_db)):
    deleteuser = db.query(User).filter(
        User.id == id).first()

    if deleteuser.is_deleted != True:
        deleteuser.is_deleted = True
        db.commit()
        return {"message" : "user deleted successfully"}

    elif deleteuser.is_deleted == True:
        return {"message" : "user is already deleted"}


# user login api
@user_router.post('/user/login', status_code= status.HTTP_201_CREATED)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        User.email == user.email).first()
    
    if db_user and db_user.password == user.password: 
        return {"success" : "user login successful"}
    elif  db_user.password != user.password:
        raise HTTPException(status_code=404, detail="user not found, please check your credentials")

# end of user routes

