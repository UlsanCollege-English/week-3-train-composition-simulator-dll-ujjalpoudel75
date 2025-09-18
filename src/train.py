class _Car:
    __slots__ = ("id", "prev", "next")
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

class Train:
    def __init__(self):
        self.head = None
        self.tail = None

    def attach_front(self, car_id):
        ...

    def attach_back(self, car_id):
        ...

    def detach_front(self):
        ...

    def detach_back(self):
        ...

    def detach(self, car_id):
        ...

    def to_list(self):
        ...
