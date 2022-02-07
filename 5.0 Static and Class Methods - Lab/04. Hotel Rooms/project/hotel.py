# from room import Room
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        check_room = [x for x in self.rooms if x.number == room_number][0]
        result = check_room.take_room(people)
        if result is None:
            self.guests += people

    def free_room(self, room_number):
        check_room = [x for x in self.rooms if x.number == room_number]
        if len(check_room) > 0:
            self.guests -= check_room[0].guests
            check_room[0].free_room()

    def status(self):
        return f'Hotel {self.name} has {self.guests} total guests\n\
Free rooms: {", ".join([str(x.number) for x in self.rooms if not x.is_taken])}\n\
Taken rooms: {", ".join([str(x.number) for x in self.rooms if  x.is_taken])}'




