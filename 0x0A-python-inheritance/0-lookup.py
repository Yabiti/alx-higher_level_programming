class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passsengers = []
    def add_passengers(self, name):
        self.passengers.append(name)