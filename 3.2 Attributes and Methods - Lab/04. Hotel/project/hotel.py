
class Hotel:
    rooms = []
    guests = 0
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def from_stars(cls, stars_count):
        hotel_name = f'{stars_count} stars Hotel'
        return Hotel(hotel_name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people): 
        room = [x for x in self.rooms if x.number == room_number][0] 
        result = room.take_room(people)
        if result:
            return result
        self.guests += people     

    def free_room(self, room_number): 
        room = [x for x in self.rooms if x.number == room_number][0]
        result = room.free_room()
        if result:
            return result   
        self.guests -= room.guests
       
       
        
    def print_status(self):
        free_rooms = ', '.join([str(x.number) for x in self.rooms if not x.is_taken])
        busy_rooms = ', '.join([str(x.number) for x in self.rooms if x.is_taken])      
        print(f'Hotel {self.name} has {self.guests} total guests')
        if free_rooms:
            print(f'Free rooms: {free_rooms}')
        if busy_rooms:    
            print(f'Taken rooms: {busy_rooms}')
             
                





