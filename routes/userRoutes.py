
from fastapi import APIRouter,HTTPException
from models.userModel import UserTable
from models.userModel import UserTable,UserDetails
#from pydantic import BaseModel
from typing import List
from database import SessionLocal
#from datetime import datetime

userRouter = APIRouter()
db=SessionLocal()

#user routes

#get all
@userRouter.get('/users',status_code=200)
def get_all_users():
    users = db.query(UserDetails).all()

    return users

#get 1 user
@userRouter.get('/user/{user_id}',status_code=200)
def get_user(user_id:int):
    user = db.query(UserDetails).filter(UserDetails.User_Id==user_id).first()
    return user
                  
#create                   
@userRouter.post('/users',status_code=201)
def create_user(user:UserTable):
    db_user = db.query(UserDetails).filter(UserDetails.Name==user.Name).first()
    if db_user is not None:
        raise HTTPException(status_code=400,detail="User already exists")

    new_user = UserDetails(
        User_Id = user.User_Id,
        Name = user.Name,
        Password =user.Password,
        Email = user.Email,
        is_Deleted = user.is_Deleted,
        created_at = user.created_at,
        updated_at = user.updated_at
    )

    db.add(new_user)
    db.commit()

    return {"message":"User added Successfully"}
    
#update
@userRouter.put('/user/{user_id}',status_code=200)
def update_user(user_id:int,user:UserTable):
    updateuser = db.query(UserDetails).filter(UserDetails.User_Id==user_id).first()
    updateuser.Name = user.Name
    updateuser.Password = user.Password
    updateuser.Email = user.Email
    updateuser.is_Deleted = user.is_Deleted
    updateuser.created_at = user.created_at
    updateuser.updated_at = user.updated_at

    db.commit()

    return {"message":"User updated successfully"}
'''
@userRouter.put('/user/{user_id}/name',status_code=200)
def update_username(user_id:int,user:UserTable):
    updateusername = db.query(UserDetails).filter(UserDetails.User_Id==user_id).first()
    updateusername.Name = user.Name
    db.commit()
    return updateusername

'''

#delete
@userRouter.delete('/user/{user_id}')
def delete_user(user_id:int):
    deleteuser = db.query(UserDetails).filter(UserDetails.User_Id==user_id).first()

    if deleteuser is None:
        raise HTTPException(status_code=404, detail="user not found to delete")
    db.delete(deleteuser)
    db.commit()
    return {"message":"user with {user_id} is deleted successfully"}



# end of user routes
