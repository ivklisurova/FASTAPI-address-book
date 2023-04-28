from fastapi import APIRouter, Depends, Request, Path
from fastapi import status

from routers.schemas import AddressBase, UpdateAddressBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_address
from core.functions import calculate_distance
from typing_extensions import Annotated


router = APIRouter(
    prefix='/location',
    tags=['address book']
)


# Create -> POST
@router.post('', status_code=status.HTTP_201_CREATED)
async def create_location_record(request: AddressBase, db: Session = Depends(get_db)):
    return db_address.create_location(db, request)


# Retrieve all addresses -> GET
@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_location_records(db: Session = Depends(get_db)):
    return db_address.get_all_locations(db)


# Retrieve address -> GET
@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_location_record(id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)):
    return db_address.get_location(id, db)


# Retrieve the addresses that are within a given distance and location coordinates -> GET
@router.get("/point/pointdistances")
async def get_locations_by_distance(my_lat: float, my_long: float, given_distance: float, request: Request,
                                    db: Session = Depends(get_db)):
    current_location = (my_lat, my_long)
    all_records = db_address.get_all_locations(db)
    locations_in_range = []
    for place in all_records:
        destination = (place.latitude, place.longitude)
        if calculate_distance(current_location, destination) <= given_distance:
            locations_in_range.append(place)

    return locations_in_range


# Update -> PATCH
@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_partially_location_record(id: Annotated[int, Path(title="The ID of the item to get")], request: UpdateAddressBase, db: Session = Depends(get_db)):
    db_address.update_location(id, request, db)
    return {"message": f"Location with id {id} successfully Updated"}


# Delete -> DELETE

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_location_record(id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)):
    return db_address.delete_location(id, db)
