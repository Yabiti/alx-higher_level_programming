class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passsengers = []
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seata(self):
        return self.capacity - len(self.passsengers)
        