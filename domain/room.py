
import dataclasses
import uuid


@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    lat: float
    long: float


    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return dataclasses.asdict(self)



