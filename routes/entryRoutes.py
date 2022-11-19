

from fastapi import APIRouter, HTTPException 
#import compModel
from typing import List
from models.entryModel import EntryDetails,EntryTable
from database import SessionLocal
#from pydantic import BaseModel

db=SessionLocal()

entryRouter = APIRouter()


#get all entries
@entryRouter.get('/entries',status_code=200)
def get_all_entry():
    comps = db.query(EntryDetails).all()

    return comps



#get 1 entry
@entryRouter.get('/entry/{entry_id}',status_code=200)
def get_entry(entry_id:int):
    entry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()
    return entry



#create                   
@entryRouter.post('/entries',status_code=201)
def create_enrty(entry:EntryTable):
    db_entry = db.query(EntryDetails).filter(EntryDetails.name==entry.name).first()
    if db_entry is not None:
        raise HTTPException(status_code=400,detail="Entry already exists")

    new_entry = EntryDetails(
        entry_id = entry.entry_id,
        name = entry.name,
        status =entry.status,
        country = entry.country,
        state = entry.state,
        is_deleted = entry.is_deleted,
        created_at = entry.created_at,
        updated_at = entry.updated_at,
        comp_id = entry.comp_id
    )

    db.add(new_entry)
    db.commit()

    return {"message":"new entry is added successfully"}
    


#update
@entryRouter.put('/entry/{entry_id}',status_code=200)
def update_entry(entry_id:int,entry:EntryTable):
    updateentry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()
    updateentry.name = entry.name
    updateentry.status = entry.status
    updateentry.country = entry.country
    updateentry.state = entry.state
    updateentry.is_deleted = entry.is_deleted
    updateentry.created_at = entry.created_at
    updateentry.updated_at = entry.updated_at
    updateentry.comp_id = entry.comp_id

    db.commit()

    return {"message":"entry is updated successfully"}



#delete
@entryRouter.delete('/entry/{entry_id}')
def delete_entry(entry_id:int):
    deleteentry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()

    if deleteentry is None:
        raise HTTPException(status_code=404, detail="entry not found to delete")
    db.delete(deleteentry)
    db.commit()
    return {"message":"entry with {entry_id} is deleted successfully"}

# end of entry routes
