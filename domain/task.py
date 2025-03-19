from dataclasses import dataclass
import dataclasses


@dataclass
class Task:
    id: int
    title: str
    description: str

    def to_upper(self):
        return Task(id=self.id, title=self.title.upper(), description=self.description.upper())

    def to_dict(self):
        return dataclasses.asdict(self)
