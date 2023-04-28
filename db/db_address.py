from fastapi import HTTPException, status
from routers.schemas import AddressBase, UpdateAddressBase
from sqlalchemy.orm.session import Session
from db.models import DBAddress


def create_location(db: Session, request: AddressBase):
    new_address = DBAddress(
        country=request.country,
        city=request.city,
        street_name=request.street_name,
        street_number=request.street_number,
        postal_code=request.postal_code,
        latitude=request.latitude,
        longitude=request.longitude
    )
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


def get_all_locations(db: Session):
    return db.query(DBAddress).all()


def get_location(id: int, db: Session):
    location = db.query(DBAddress).filter(DBAddress.id==id).first()
    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Location with id {id} not found')
    return location


def delete_location(id: int, db: Session):
    location = db.query(DBAddress).filter(DBAddress.id==id).first()
    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Address with id {id} not found')
    db.delete(location)
    db.commit()
    return 'ok'


def update_location(id: int, request: UpdateAddressBase, db: Session):
    location = get_location(id, db)
    db.query(DBAddress).filter(DBAddress.id==id).update(request.dict(exclude_none=True))
    db.commit()
    db.refresh(location)
    return location
