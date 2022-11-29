from fastapi import APIRouter, HTTPException 
from entry.entry_schema import EntryDetails
from entry.entry_model import EntryTable
from database_files.database import SessionLocal

db=SessionLocal()


entryRouter = APIRouter()


#get all entries
@entryRouter.get('/entries', status_code=200)
def get_all_entry():
    comps = db.query(EntryDetails).all()

    return comps



#get 1 entry
@entryRouter.get('/entry/{entry_id}', status_code=200)
def get_entry(entry_id:int):
    entry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()

    return entry



#create                   
@entryRouter.post('/entries', status_code=201)
def create_entry(entry:EntryTable):
    db_entry = db.query(EntryDetails).filter(EntryDetails.name==entry.name).first()
    
    if db_entry is not None:
        raise HTTPException(status_code=400,detail="Entry already exists")
    else:
        new_entry = EntryDetails(
        entry_id = entry.entry_id,
        name = entry.name,
        status =entry.status,
        country = entry.country,
        state = entry.state,
        
        comp_id = entry.comp_id
    )

    db.add(new_entry)
    db.commit()

    return {f"message":"new entry is added successfully"}
    


#update
@entryRouter.put('/entry/{entry_id}',status_code=200)
def update_entry(entry_id:int,entry:EntryTable):
    updateentry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()
    if updateentry:
        updateentry.update(entry.dict())
        updateentry.updated_at = entry.updated_at

        db.add(updateentry)
        db.commit()

    return {f"message":"entry with id: {entry_id} is updated successfully"}



#delete
@entryRouter.delete('/entry/{entry_id}')
def delete_entry(entry_id:int):
    deleteentry = db.query(EntryDetails).filter(EntryDetails.entry_id==entry_id).first()

    if deleteentry is None:
        raise HTTPException(status_code=404, detail="entry not found to delete")
    else:
        db.delete(deleteentry)
        
    db.commit()
    return {"message":"entry with {entry_id} is deleted successfully"}

# end of entry routes









################################## UNWANTED CODE #############################################
'''  updateentry.is_deleted = entry.is_deleted
    updateentry.created_at = entry.created_at
    updateentry.updated_at = entry.updated_at





'''