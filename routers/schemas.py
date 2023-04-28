from pydantic import BaseModel
from typing import Optional


class AddressBase(BaseModel):
    country: str
    city: str
    street_name: str
    street_number: int
    postal_code: str
    latitude: float
    longitude: float


class UpdateAddressBase(BaseModel):
    street_name: Optional[str]
    street_number: Optional[int]
    postal_code: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
