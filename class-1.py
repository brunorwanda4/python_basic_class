class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date

    def get_passenger_info (self):
        print("Name:", self.name)
        print("From:", self.location)
        print("To:", self.destination)
        print("Date:", self.date)
