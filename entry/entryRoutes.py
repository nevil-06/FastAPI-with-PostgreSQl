from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses  import JSONResponse
from entry.entry_schema import EntryDetails
from entry.entry_model import EntryTable
from database_files.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List

entryRouter = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        return db
    except:
        print("Can not get the DB.")
    


#get all entries that are not deleted
@entryRouter.get('/entries/all', status_code=200)
def get_all_entry(db: Session = Depends(get_db)):
    comps = db.query(EntryDetails).filter(EntryDetails.is_deleted!=True).all()
    return comps



#get 1 entry that is not deleted
@entryRouter.get('/entry/{entry_id}', status_code=200)
def get_entry(entry_id:str,db: Session = Depends(get_db)):
    entry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id, EntryDetails.is_deleted!=True).first()
    if entry:
        return {
            "entry_id" : entry.entry_id,
            "name" : entry.name,
            "status" : entry.status,
            "country" : entry.country,
            "state" :  entry.state,
            "is_deleted" : entry.is_deleted,
            "created_at" : entry.created_at,
            "updated_at" : entry.updated_at,
            "comp_id" : entry.comp_id
            }




#get entries that are deleted
@entryRouter.get('/entries/del', status_code=200)
def get_all_deleted_entry(db: Session = Depends(get_db)):
    comps = db.query(EntryDetails).filter(EntryDetails.is_deleted==True).all()

    return comps

getattr

#create                   
@entryRouter.post('/entries', status_code=201, response_model=EntryTable)
def create_entry(entry:EntryTable,db: Session = Depends(get_db)):
    db_entry = db.query(EntryDetails).filter(EntryDetails.name==entry.name).first()
    
    if db_entry is not None:
        raise HTTPException(status_code=400,detail="Entry already exists")
    else:
        new_entry = EntryDetails(
        name = entry.name,
        status =entry.status,
        country = entry.country,
        state = entry.state,
        comp_id = entry.comp_id
    )

    db.add(new_entry)
    db.commit()
    return new_entry
    # return {"name" :  new_entry.name,
    #         "status" :new_entry.status,
    #         "country" :new_entry.country,
    #         "state" :new_entry.state,
    #         "comp_id" : new_entry.comp_id
    #         }
    


#update entry that are available
@entryRouter.put('/entry/{entry_id}',status_code=200)
def update_entry(entry_id:str, entry:EntryTable, db: Session = Depends(get_db)):
    updateentry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()
    if updateentry:
        updateentry.update(entry.dict())
        json_compatible_item_data = jsonable_encoder(updateentry)
         
        db.add(updateentry)
        db.commit()
        return JSONResponse(content=json_compatible_item_data)
        #return {f"message":"entry with id: {entry_id} is updated successfully"}

    else:
        return {f"message":"entry with id: {entry_id} is deleted so cannot update"}




#delete
@entryRouter.delete('/entry/{entry_id}')
def delete_entry(entry_id:str,db: Session = Depends(get_db)):
    deleteentry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()

    if deleteentry is None:
        raise HTTPException(status_code=404, detail="entry not found to delete")
    else:
        EntryDetails.is_deleted=True
        
    db.commit()
    return {f"entry is deleted successfully and its status is changed to {deleteentry.is_deleted}"}

# end of entry routes









################################## UNWANTED CODE #############################################
'''  updateentry.is_deleted = entry.is_deleted
    updateentry.created_at = entry.created_at
    updateentry.updated_at = entry.updated_at





'''