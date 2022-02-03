class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def rent_dvd(self, customer_id, dvd_id):
        dvd = [x for x in self.dvds if dvd_id == x.id][0]
        client = [x for x in self.customers if customer_id == x.id][0]
        if dvd.is_rented:
            if dvd not in client.rented_dvds:
                return f'DVD is already rented'
            return f'{client.name} has already rented {dvd.name}'
        if client.age < dvd.age_restriction:
            return f'{client.name} should be at least {dvd.age_restriction} to rent this movie'
        client.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{client.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        dvd = [x for x in self.dvds if dvd_id == x.id][0]
        client = [x for x in self.customers if customer_id == x.id][0]
        if dvd not in client.rented_dvds:
            return f'{client.name} does not have that DVD'
        client.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f'{client.name} has successfully returned {dvd.name}'

    def __repr__(self):
        client = [x for x in self.customers]
        dvd = [x for x in self.dvds]
        result = ''
        for j in client:
            result += f'{j.__repr__()}\n'
        for i in dvd:
            result += f'{i.__repr__()}\n'
        return result

    def add_customer(self, customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)

