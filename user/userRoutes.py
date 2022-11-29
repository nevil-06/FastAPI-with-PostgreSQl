from fastapi import APIRouter,HTTPException,Depends
from user.user_model import UserTable
from user.user_schema import UserDetails
from datetime import datetime
from database_files.database import SessionLocal 
from sqlalchemy.orm import Session


userRouter = APIRouter()


def get_db():
    try:
        db=SessionLocal()
        return db
    except:
        print("Can not get the DB.")

#user routes



#get all
@userRouter.get('/users',status_code=200)
def get_all_users(db:Session= Depends(get_db)):
    users = db.query(UserDetails).all()

    return users



#get 1 user
@userRouter.get('/user/{user_id}',status_code=200)
def get_user(user_id:int, db:Session= Depends(get_db)):
    user = db.query(UserDetails).filter(UserDetails.User_Id==user_id).first()

    return user
                  


#create new user and provide their details           
@userRouter.post('/users',status_code=201)
def create_user(user:UserTable, db:Session= Depends(get_db)):
    db_user = db.query(UserDetails).filter(UserDetails.Name==user.Name).first()
    
    if db_user is not None:
        raise HTTPException(status_code=400,detail="User already exists")

    new_user = UserDetails(
        User_Id = user.User_Id,
        Name = user.Name,
        Password =user.Password,
        Email = user.Email,
        
    )

    db.add(new_user)
    db.commit()

    return {
        "message": " New User added Successfully"
        }
    
#update user and their values
@userRouter.put('/user/{user_id}',status_code=200)
def update_user(user_id:int, user:UserTable, db:Session= Depends(get_db)):
    updateuser:UserDetails = db.query(UserDetails).filter(UserDetails.User_Id==user_id, UserDetails.is_Deleted==False).first()
    
    if updateuser:
        updateuser.update(user.dict())
        # updateuser.updated_at = user.updated_at
        db.add(updateuser)
        db.commit() 
        return {f"message":"user with user_id: {user_id} is updated"}
    else:
        return {f"message":"user with user_id: {user_id} is deleted so cannot update"}
    



#delete
@userRouter.delete('/user/{user_id}')
def delete_user(user_id:int, user:UserTable, db:Session= Depends(get_db)):
    deleteuser = db.query(UserDetails).filter(UserDetails.User_Id==user_id).first()

    if deleteuser is None:
        raise HTTPException(status_code=404, detail="user not found to delete")
    else:
        deleteuser.is_Deleted = True

    db.commit()
    return {"message": f"User with user_id: {user_id} is deleted successfully"}



# end of user routes













#################################### UNWANTED CODE ##################################
'''    
# is_Deleted = user.is_Deleted,
        # created_at = datetime.utcnow()
        #updated_at = datetime.utcnow()





    try:
        if updateuser:
            breakpoint()
            updateuser.update(user.dict(exclude_unset=True))
    except:
        return {"message":"cannot update user"}
    finally:


    updateuser.Name = user.Name
    updateuser.Password = user.Password
    updateuser.Email = user.Email

    #return {"message : {updateuser} is updated successfully"}
    #return {"message":"User updated successfully"


@userRouter.put('/user/{user_id}/name',status_code=200)
def update_username(user_id:int,user:UserTable):
    updateusername = db.query(UserDetails).filter(UserDetails.User_Id==user_id).first()
    updateusername.Name = user.Name
    db.commit()
    return updateusername

'''