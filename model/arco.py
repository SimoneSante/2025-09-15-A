from dataclasses import dataclass
from model.piloti import Pilota

@dataclass
class Arco:
    o1: Pilota
    o2: Pilota
    peso: int

    def __hash__(self):
        return hash(self.peso)

    def __eq__(self,other):
        return self.driverId == other.driverId