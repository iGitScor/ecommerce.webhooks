from pydantic import BaseModel
from typing import Optional

class WooAddress(BaseModel):
    first_name: str
    last_name: str
    company: str
    address_1: str
    address_2: str
    city: str
    state: str
    postcode: int
    country: str
    email: Optional[str]
    phone: Optional[str]