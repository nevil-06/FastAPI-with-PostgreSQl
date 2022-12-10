from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses  import JSONResponse
from app.entry.schema import EntryTable, EntryResponse
from app.entry.model import EntryDetails
from app.utils.db_session_create import get_db
from sqlalchemy.orm import Session
from typing import List

entryRouter = APIRouter()


#get all entries that are not deleted
@entryRouter.get('/entries/all', status_code = status.HTTP_200_OK, response_model= List[EntryResponse])
def get_all_entry(db: Session = Depends(get_db)):
    comps = db.query(EntryDetails).filter(EntryDetails.is_deleted != True).all()
    return comps


#get 1 entry that is not deleted
@entryRouter.get('/entry/{entry_id}', status_code= status.HTTP_200_OK, response_model= EntryResponse)
def get_entry(entry_id: str, db: Session = Depends(get_db)):
    entry = db.query(EntryDetails).filter(EntryDetails.entry_id == entry_id, EntryDetails.is_deleted != True).first()
    if entry:
        return entry



#get entries that are deleted
@entryRouter.get('/entries/del', status_code = status.HTTP_200_OK, response_model= List[EntryResponse])
def get_all_deleted_entry(db: Session = Depends(get_db)):
    comps = db.query(EntryDetails).filter(EntryDetails.is_deleted == True).all()
    return comps


#admin function to see full data #testing done
@entryRouter.get('/admin/entries/all')
def admin_get_all(db: Session = Depends(get_db)):
        entries = db.query(EntryDetails).filter(EntryDetails.is_deleted != True).all()
        return entries


#create                   
@entryRouter.post('/entries', status_code = status.HTTP_201_CREATED)
def create_entry(entry: EntryTable, db: Session = Depends(get_db)):
    db_entry = db.query(EntryDetails).filter(EntryDetails.name == entry.name).first()
    
    if db_entry is not None:
        return {f"message":"Entry already exists"}

    new_entry = EntryDetails(
    name = entry.name,
    status =entry.status,
    country = entry.country,
    state = entry.state,
    comp_id = entry.comp_id)

    db.add(new_entry)
    db.commit()
    return new_entry


#update entry that are available
@entryRouter.put('/entry/{entry_id}',status_code = status.HTTP_202_ACCEPTED, response_model= EntryResponse)
def update_entry(entry_id: str, entry: EntryTable, db: Session = Depends(get_db)):
    updateentry = db.query(EntryDetails).filter(EntryDetails.entry_id == entry_id).first()
    if updateentry:
        updateentry.update(entry.dict())
        db.add(updateentry)
        db.commit()
        return updateentry
    else:
        return {"message": f"Entry details for id: {entry_id} is deleted so cannot update"}
    


#delete
@entryRouter.delete('/entry/{entry_id}', response_model= EntryResponse)
def delete_entry(entry_id: str, db: Session = Depends(get_db)):
    deleteentry = db.query(EntryDetails).filter(EntryDetails.entry_id == entry_id).first()

    if deleteentry.is_deleted != True:
        deleteentry.is_deleted = True
        db.commit()
        return deleteentry
    elif deleteentry.is_deleted == True:
        return deleteentry

# end of entry routes
