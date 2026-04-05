from pydantic import BaseModel

class UserCreate(BaseModel):
    name : str
    role : str

class RecordCreate(BaseModel):
    user_id : int
    amount : float
    type : str
    category : str
    date : str
    description : str