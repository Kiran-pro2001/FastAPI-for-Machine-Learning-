from pydantic import BaseModel, Field, StrictInt
from typing import Optional


# enforcing the validation 
class Employee(BaseModel):
    id : int  = Field(..., gt=0, title="Employee Id")  # required - ... -- elipses  , gt=0  -- greater then 0, 
    name : str = Field(..., min_length=3, max_length=30)
    department : str = Field(..., min_length=3, max_length=30)
    age : Optional[StrictInt] = Field(default=None, ge=21)    # now it's an optional value, if user not give any value, the value will be None ,  ge= 21 -- greater than equal to 21
    
