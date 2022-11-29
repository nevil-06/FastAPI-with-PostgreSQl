from fastapi import APIRouter, HTTPException 
from competition.competition_schema import CompDetails
from competition.competition_model import CompTable
from database_files.database import SessionLocal
#from datetime import datetime


db=SessionLocal()


compRouter = APIRouter()


#comp routes
@compRouter.get('/comps', status_code=200)
def get_all_comp():
    comps = db.query(CompDetails).all()

    return comps


#get 1 comp
@compRouter.get('/comp/{comp_id}', status_code=200)
def get_user(comp_id:int):
    comp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id).first()
    
    return comp


#create                   
@compRouter.post('/comps', status_code=201)
def create_comp(comp:CompTable):
    db_comp = db.query(CompDetails).filter(CompDetails.name==comp.name).first()
    
    if db_comp is not None:
        raise HTTPException(status_code=400,detail="Comp already exists")


    new_comp = CompDetails(
        comp_id = comp.comp_id,
        name = comp.name,
        status =comp.status,
        url = comp.url,        
        user_id = comp.user_id
    )


    db.add(new_comp)
    db.commit()


    return {"message":"comp added successfully"}




#update
@compRouter.put('/comp/{comp_id}', status_code=200)
def update_user(comp_id:int,comp:CompTable):
    updatecomp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id).first()
    
    if updatecomp:
        updatecomp.update(comp.dict())
        updatecomp.updated_at = comp.updated_at

        db.add(updatecomp)
        db.commit()
        return {f"message":"competiton with id: {comp_id} is updated"}
    else:
        return {f"message":"competiton with id: {comp_id} is deleted so cannot update"}



#delete
@compRouter.delete('/comp/{comp_id}')
def delete_comp(comp_id:int):
    deletecomp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id).first()

    if deletecomp is None:
        raise HTTPException(status_code=404, detail="comp not found to delete")
    else:
        deletecomp.is_deleted=True
    
    db.delete(deletecomp)
    db.commit()
    return {"message": "Competition details with id: {comp_id} is deleted"}


# end of comp routes









################################ UNWANTED CODE ################################

#is_deleted = comp.is_deleted,
        #created_at = datetime.utcnow(),
        #updated_at = comp.updated_at,

    # db.commit()

    # return {"message":"competition details updated successfully"}
'''updatecomp.name = comp.name
    updatecomp.status = comp.status
    updatecomp.url = comp.url
    updatecomp.is_deleted = comp.is_deleted
    updatecomp.created_at = comp.created_at
    updatecomp.updated_at = comp.updated_at
    updatecomp.user_id = comp.user_id
    '''


