class Passenger:
    def __init__(self, name, current_location, destination, date):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.date = date

    def get_passenger_info(self):
        print(f"{self.name} is flying from {self.current_location} to {self.destination} on {self.date}.")

    def get_weight_allowance(self) -> int:
        return 20


class FirstClassPassenger(Passenger):
    def __init__(self, name, current_location, destination, date, weight, lounge_access):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.lounge_access = lounge_access

    def set_weight(self, weight):
        self.weight = weight

    def access_lounge(self):
        if self.lounge_access:
            print(f"{self.name} can access the lounge.")
        else:
            print(f"{self.name} cannot access the lounge.")

    def get_weight_allowance(self) -> int:
        return 40


class PremiumPassenger(Passenger):
    def __init__(self, name, current_location, destination, date, weight, priority_boarding):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.priority_boarding = priority_boarding

    def set_weight(self, weight):
        self.weight = weight

    def get_priority_boarding(self):
        if self.priority_boarding:
            print(f"{self.name} has priority boarding.")
        else:
            print(f"{self.name} does not have priority boarding.")

    def get_weight_allowance(self) -> int:
        return 30


class EconomyPassenger(Passenger):
    pass

economy = EconomyPassenger("Alice", "Kigali", "Nairobi", "2026-11-10")
first = FirstClassPassenger("Brian", "Kigali", "Dubai", "2026-11-12", 25, True)
premium = PremiumPassenger("Bruno", "Kigali", "London", "2026-11-15", 18, True)

economy.get_passenger_info()
print("Allowance:", economy.get_weight_allowance(), "kg")

first.get_passenger_info()
print("Allowance:", first.get_weight_allowance(), "kg")
first.access_lounge()

premium.get_passenger_info()
print("Allowance:", premium.get_weight_allowance(), "kg")
premium.get_priority_boarding()
