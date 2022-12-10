from fastapi import APIRouter, Depends, status
from app.competition.schema import CompTable, CompResponse
from app.competition.model import CompDetails
from app.utils.db_session_create import get_db
from app.user.schema import UserDetails
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List


compRouter = APIRouter()


#comp routes that are not deleted
@compRouter.get('/comps/all', status_code = status.HTTP_200_OK, response_model= List[CompResponse])
def get_all_comp(db: Session = Depends(get_db)):
    comps = db.query(CompDetails).filter(CompDetails.is_deleted != True).all()
    return comps


#get 1 comp that is not deleted
@compRouter.get('/comp/{comp_id}', status_code = status.HTTP_200_OK, response_model= CompResponse)
def get_user(comp_id: str, db: Session = Depends(get_db)):
    comp = db.query(CompDetails).filter(CompDetails.comp_id == comp_id, CompDetails.is_deleted != True).first()
    return comp


#comp routes that are deleted
@compRouter.get('/comps/del', status_code = status.HTTP_200_OK, response_model= List[CompResponse])
def get_all_deleted_comp(db: Session = Depends(get_db)):
    comps = db.query(CompDetails).filter(CompDetails.is_deleted == True).all()
    return comps


#admin function to see full data #testing done
@compRouter.get('/admin/comps/all')
def admin_get_all(db: Session = Depends(get_db)):
        comps = db.query(CompDetails).filter(CompDetails.is_deleted != True).all()
        return comps



#create new competition details                
@compRouter.post('/comps', status_code = status.HTTP_201_CREATED)
def create_comp(comp:CompTable, db: Session = Depends(get_db)):
    db_comp = db.query(CompDetails).filter(CompDetails.name == comp.name, UserDetails.is_deleted != True).first()
    
    if db_comp:
        return {"message": "Competiton details already exists"}
    else:
        new_comp = CompDetails(
            comp_id = comp.comp_id,
            name = comp.name,
            status = comp.status,
            url = comp.url,        
            user_id = comp.user_id
        )
        db.add(new_comp)
        db.commit()
        return new_comp


#update
@compRouter.put('/comp/{comp_id}', status_code = status.HTTP_202_ACCEPTED, response_model= CompResponse)
def update_user(comp_id: str, comp: CompTable, db: Session = Depends(get_db)):
    updatecomp = db.query(CompDetails).filter(CompDetails.comp_id == comp_id, CompDetails.is_deleted != True).first()
    
    if updatecomp:
        updatecomp.update(comp.dict())
        db.add(updatecomp)
        db.commit()
        return updatecomp
    else:
        return {"message": f"competiton with id: {comp_id} is deleted so cannot update"}



#delete
@compRouter.delete('/comp/{comp_id}', response_model= CompResponse)
def delete_comp(comp_id: str, db: Session = Depends(get_db)):
    deletecomp = db.query(CompDetails).filter(CompDetails.comp_id == comp_id).first()
    if deletecomp.is_deleted != True:
        deletecomp.is_deleted = True
        db.commit()
        return deletecomp
    elif deletecomp.is_deleted == True:
        return deletecomp

# end of comp routes
