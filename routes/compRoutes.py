

from fastapi import APIRouter, HTTPException 
#import compModel
from typing import List
from models.compModel import CompDetails,CompTable
from database import SessionLocal
#from pydantic import BaseModel

db=SessionLocal()

compRouter = APIRouter()

@compRouter.get('/comps',status_code=200)
def get_all_comp():
    comps = db.query(CompDetails).all()

    return comps

#get 1 comp
@compRouter.get('/comp/{comp_id}',status_code=200)
def get_user(comp_id:int):
    comp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id).first()
    return comp
                  
#create                   
@compRouter.post('/comps',status_code=201)
def create_comp(comp:CompTable):
    db_comp = db.query(CompDetails).filter(CompDetails.name==comp.name).first()
    if db_comp is not None:
        raise HTTPException(status_code=400,detail="Comp already exists")

    new_comp = CompDetails(
        comp_id = comp.comp_id,
        name = comp.name,
        status =comp.status,
        url = comp.url,
        is_deleted = comp.is_deleted,
        created_at = comp.created_at,
        updated_at = comp.updated_at,
        user_id = comp.user_id
    )

    db.add(new_comp)
    db.commit()

    return {"message":"comp added successfully"}
    
#update
@compRouter.put('/comp/{comp_id}',status_code=200)
def update_user(comp_id:int,comp:CompTable):
    updatecomp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id).first()
    updatecomp.name = comp.name
    updatecomp.status = comp.status
    updatecomp.url = comp.url
    updatecomp.is_deleted = comp.is_deleted
    updatecomp.created_at = comp.created_at
    updatecomp.updated_at = comp.updated_at
    updatecomp.user_id = comp.user_id

    db.commit()

    return {"message":"competition details updated successfully"}
#delete
@compRouter.delete('/comp/{comp_id}')
def delete_comp(comp_id:int):
    deletecomp = db.query(CompDetails).filter(CompDetails.comp_id==comp_id).first()

    if deletecomp is None:
        raise HTTPException(status_code=404, detail="comp not found to delete")
    db.delete(deletecomp)
    db.commit()
    return {"message": "Competition details is deleted"}

# end of comp routes
