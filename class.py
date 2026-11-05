class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date

    def get_passenger_info(self):
        print("Name:", self.name)
        print("From:", self.location)
        print("To:", self.destination)
        print("Date:", self.date)

    def get_weight_allowance(self):
        print("Normal weight allowance")


class EconomyPassenger(Passenger):
    pass


class FirstClassPassenger(Passenger):
    def __init__(self, name, location, destination, date, weight, lounge_access):
        super().__init__(name, location, destination, date)
        self.weight = weight
        self.lounge_access = lounge_access

    def set_weight(self):
        print("Weight:", self.weight, "kg")

    def access_lounge(self):
        print("Lounge Access:", self.lounge_access)


class PremiumPassenger(Passenger):
    def __init__(self, name, location, destination, date, weight, priority_boarding):
        super().__init__(name, location, destination, date)
        self.weight = weight
        self.priority_boarding = priority_boarding

    def set_weight(self):
        print("Weight:", self.weight, "kg")

    def get_priority_boarding(self):
        print("Priority Boarding:", self.priority_boarding)


print("Economy Passenger")
p1 = EconomyPassenger("John", "Kigali", "Nairobi", "10 July")
p1.get_passenger_info()

print("\nFirst Class Passenger")
p2 = FirstClassPassenger("Alice", "Kigali", "London", "15 July", 40, "Yes")
p2.get_passenger_info()
p2.set_weight()
p2.access_lounge()

print("\nPremium Passenger")
p3 = PremiumPassenger("David", "Kigali", "Dubai", "20 July", 35, "Yes")
p3.get_passenger_info()
p3.set_weight()
p3.get_priority_boarding()
