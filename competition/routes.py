from fastapi import APIRouter, Depends
from competition.schema import CompTable
from competition.model import CompDetails
from database_files.database import SessionLocal
from user.schema import UserDetails
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

compRouter = APIRouter()



def get_db():
    try:
        db = SessionLocal()
        return db
    except AttributeError:
        print("Can not get the DB.")



#comp routes that are not deleted
@compRouter.get('/comps/all', status_code=200)
def get_all_comp(db: Session = Depends(get_db)):
    comps = db.query(CompDetails).filter(CompDetails.is_deleted!=True).all()

    return comps





#get 1 comp that is not deleted
@compRouter.get('/comp/{comp_id}', status_code=200)
def get_user(comp_id:str, db:Session=Depends(get_db)):
    comp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id, CompDetails.is_deleted!=True).first()
    
    return comp



#comp routes that are deleted
@compRouter.get('/comps/del', status_code=200)
def get_all_deleted_comp(db:Session=Depends(get_db)):
    comps = db.query(CompDetails).filter(CompDetails.is_deleted==True).all()

    return comps




#create new competition details                
@compRouter.post('/comps', status_code=201)
def create_comp(comp:CompTable, db:Session=Depends(get_db)):
    db_comp = db.query(CompDetails).filter(CompDetails.name==comp.name, UserDetails.is_Deleted!=True).first()
    
    if db_comp:
        return {"message": "Competiton details already exists"}


    new_comp= CompDetails(
        comp_id= comp.comp_id,
        name= comp.name,
        status= comp.status,
        url= comp.url,        
        user_id= comp.user_id
    )
    db.add(new_comp)
    db.commit()

    return {"message":"New Competiton details added successfully"}




#update
@compRouter.put('/comp/{comp_id}', status_code=200)
def update_user(comp_id:str, comp:CompTable, db:Session=Depends(get_db)):
    updatecomp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id, CompDetails.is_deleted!=True).first()
    
    if updatecomp:
        updatecomp.update(comp.dict())
        
        db.add(updatecomp)
        db.commit()
        return {"message": f"competiton with id: {comp_id} is updated"}
    
    return {"message": f"competiton with id: {comp_id} is deleted so cannot update"}



#delete
@compRouter.delete('/comp/{comp_id}')
def delete_comp(comp_id:str, db:Session=Depends(get_db)):
    deletecomp= db.query(CompDetails).filter(CompDetails.comp_id==comp_id).first()

    if deletecomp:
        return {"message": "Competition details not found to delete"}
    
    deletecomp.is_deleted= True
    db.commit()
    return {"message": f"Competition details with id: {comp_id} is deleted"}


# end of comp routes









################################ UNWANTED CODE ################################

#is_deleted = comp.is_deleted,
        #created_at = datetime.utcnow(),
        #updated_at = comp.updated_at,

    # db.commit()

        # json_compatible_item_data = jsonable_encoder(updatecomp)
        # comp.dict() this only returns the field with updated value and other fields as null
        # JSONResponse(content=json_compatible_item_data)
        # {"message": f"competiton with id: {comp_id} is updated"}



    # return {"message":"competition details updated successfully"}
'''updatecomp.name = comp.name
    updatecomp.status = comp.status
    updatecomp.url = comp.url
    updatecomp.is_deleted = comp.is_deleted
    updatecomp.created_at = comp.created_at
    updatecomp.updated_at = comp.updated_at
    updatecomp.user_id = comp.user_id
    '''


