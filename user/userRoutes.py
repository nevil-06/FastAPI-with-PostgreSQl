from fastapi import APIRouter, Depends
from user.user_model import UserDetails
from user.user_schema import UserTable
from database_files.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



userRouter = APIRouter()



def get_db():
    try:
        db = SessionLocal()
        return db
    except:
        print("Can not get the DB.")

# user routes


# get all users that are not deleted
@userRouter.get('/users/all', status_code=200)
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserDetails).filter(UserDetails.is_Deleted != True).all()

    return users


# get 1 user that is not not deleted
@userRouter.get('/user/{user_id}', status_code=200)
def get_user(user_id: str, db: Session = Depends(get_db)):
    one_user = db.query(UserDetails).filter(
        UserDetails.User_Id == user_id, UserDetails.is_Deleted != True).first()
    if one_user:
        return one_user


# get only users that are deleted
@userRouter.get('/users/del', status_code=200)
def get_all_deleted_users(db: Session = Depends(get_db)):
    users = db.query(UserDetails).filter(UserDetails.is_Deleted == True).all()
    if users:
        return users
    else:
        return {"message": "User might not be deleted or some other error"}


# create new user and provide their details
@userRouter.post('/users', status_code=201)
def create_user(user: UserTable, db: Session = Depends(get_db)):
    db_user = db.query(UserDetails).filter(
        UserDetails.Name == user.Name).first()

    if db_user:
        return {"message": "User already exists"}

    else:
        new_user = UserDetails(
            Name=user.Name,
            Password=user.Password,
            Email=user.Email)
        json_compatible_item_data = jsonable_encoder(new_user)
        db.add(new_user)
        db.commit()
        return JSONResponse(content=json_compatible_item_data)

        # manual method is also available if you want to prevent structure of body
        # return {"Name": new_user.Name,
        # "Password": new_user.Password,
        # "Email": new_user.Email}
        # automatic method in form of jsonable_endcoder and JSONResponse is also available         
        # 

# update user and their desired values
@userRouter.put('/user/{user_id}', status_code=200)
def update_user(user_id: str, user: UserTable, db: Session = Depends(get_db)):
    updateuser: UserDetails = db.query(UserDetails).filter(
        UserDetails.User_Id == user_id, UserDetails.is_Deleted == False).first()

    if updateuser:
        updateuser.update(user.dict())
        db.add(updateuser)
        db.commit()
        return updateuser

    else:
        return {"message": f"User with user_id: {user_id} is deleted so cannot update"}


# delete user that you want to
@userRouter.delete('/user/{user_id}')
def delete_user(user_id: str, db: Session = Depends(get_db)):
    deleteuser = db.query(UserDetails).filter(
        UserDetails.User_Id == user_id).first()

    if deleteuser is None:
        return {"message": "User not found to delete"}

    else:
        deleteuser.is_Deleted = True
        db.commit()
        return {"message": f"User with user_id: {user_id} is deleted successfully"}


# end of user routes
