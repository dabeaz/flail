from flail import _
from dataclasses import dataclass
from abc import abstractmethod, ABC
import attr

# Add different chain fixtures
_.d = dataclass
_.a = abstractmethod

# Examples
@_._._._._.d
class Coordinates:
    x : float
    y : float

class Connection(ABC):
    @_._.a
    def open(self):
        ...
    @_.__.a
    def close(self):
        ...
    @_._.a
    def read(self, maxbytes):
        ...
    @_.__.a
    def write(self, data):
        ...

