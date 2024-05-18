from pydantic import BaseModel
from schemas import Schemas

class UserInDB(Schemas.User):
    id: str

    

