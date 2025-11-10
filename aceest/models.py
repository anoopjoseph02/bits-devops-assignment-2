from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Gym:
    id: int
    name: str
    members: List[str] = field(default_factory=list)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'members': self.members}

    def add_member(self, name: str):
        self.members.append(name)

sessions: Dict[int, Gym] = {}
_next = 1

def _next_id():
    global _next
    r = _next
    _next += 1
    return r

class GymFactory:
    @staticmethod
    def create(name: str) -> Gym:
        gid = _next_id()
        g = Gym(gid, name)
        sessions[gid] = g
        return g

Gym.create = GymFactory.create
