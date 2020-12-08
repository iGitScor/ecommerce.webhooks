from pydantic import BaseModel
from typing import List, Any
from datetime import datetime

from domain.address import WooAddress

class Collection(BaseModel):
    href: str


class Links(BaseModel):
    links_self: List[Collection]
    collection: List[Collection]


class WooCustomer(BaseModel):
    id: int
    date_created: datetime
    date_created_gmt: datetime
    date_modified: datetime
    date_modified_gmt: datetime
    email: str
    first_name: str
    last_name: str
    role: str
    username: str
    billing: WooAddress
    shipping: WooAddress
    is_paying_customer: bool
    avatar_url: str
    meta_data: List[Any]
    _links: Links