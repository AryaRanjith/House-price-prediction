import sys

places = {
    ("Thampanoor", "TVM"): 5,
    ("Thampanoor", "Varkala"): 45,
    ("Thampanoor", "Kollam"): 70,
    ("Thampanoor", "Kottayam"): 90,
    ("TVM", "Kollam"): 75,
    ("TVM", "Varkala"): 50,
    ("Kollam", "Alappuzha"): 50,
}

cabs = {
    "EV": (10, 40),
    "Sedan": (15, 60),
    "SUV": (20, 80)
}
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == admin_username and self.password == admin_password:
            print("Admin login successful")
            return True
        else:
            print("Invalid login")
            return False

    def add_cab(self, cabs):
        cab_type = input("Enter cab type: ")
        base_fare = int(input("Enter base fare per km: "))
        speed = int(input("Enter speed (km/h): "))
        cabs[cab_type] = (base_fare, speed)
        print(f"{cab_type} cab added successfully!")

    def view_cabs(self, cabs):
        print("\n--- Available Cabs ---")
        for i, j in cabs.items():
            base_fare, speed = j
            print(f"Cab: {i}, Base fare: {base_fare}, Speed: {speed} km/h")

    def remove_cab(self, cabs):
        cab_type = input("Enter cab type to remove: ")
        if cab_type in cabs:
            del cabs[cab_type]
            print(f"{cab_type} removed successfully")
        else:
            print("Cab type not found.")

    def add_route(self, places):
        place1 = input("Enter starting place: ")
        place2 = input("Enter destination place: ")
        distance = int(input("Enter distance in km: "))
        if (place1, place2) in places:
            print("Route already present")
        else:
            places[(place1, place2)] = distance
            print(f"Route {place1} -> {place2} added")

    def view_routes(self, places):
        print("\nAvailable Routes:")
        for place, dist in places.items():
            start = place[0]
            end = place[1]
            print(f"{start} -> {end} : {dist}")

    def remove_route(self, places):
        place1 = input("Enter starting place: ")
        place2 = input("Enter destination place: ")
        if (place1, place2) in places:
            del places[(place1, place2)]
            print("Route removed successfully")
        elif (place2, place1) in places:
            del places[(place2, place1)]
            print("Route removed successfully")
        else:
            print("Route not found")

    def update_fare(self):
        cab_type = input("Enter cab type to update fare: ")
        if cab_type in cabs:
            new_fare = int(input("Enter new base fare per km: "))
            base_fare, speed = cabs[cab_type]
            cabs[cab_type] = (new_fare, speed)
            print(f"Base fare for {cab_type} updated successfully")
        else:
            print("Cab type not found.")

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        if self.email == enter_email and self.password == enter_password:
            print("Login successful")
            return True
        else:
            print("Invalid credentials")
            return False
class Cab:
    def __init__(self, cab_type, base_fare, speed):
        self.cab_type = cab_type
        self.base_fare = base_fare
        self.speed = speed


class Ride(Cab):
    def __init__(self, cab_type, base_fare, speed):
        super().__init__(cab_type, base_fare, speed)
        self.fare = 0

    def get_distance(self, place1, place2):
        return places.get((place1, place2)) or places.get((place2, place1))

    def calculate_fare(self, distance):
        return distance * self.base_fare

    def book_now(self):
        pickup = input("\nEnter pickup location: ")
        destination = input("Enter destination: ")

        start_to_pickup = self.get_distance("Thampanoor", pickup)
        pickup_to_dest = self.get_distance(pickup, destination)

        if not start_to_pickup or not pickup_to_dest:
            print("Route not found")
            sys.exit()

        cab_arrival_time = (start_to_pickup / self.speed) * 60
        ride_time = (pickup_to_dest / self.speed) * 60

        self.fare = self.calculate_fare(pickup_to_dest)

        print(f"\n===Booking Confirmed ({self.cab_type})===")
        print(f"\nCab will reach you in {cab_arrival_time} minutes")
        print(f"Cab starting from Thampanoor -> {pickup}")
        print(f"\nRide from {pickup} -> {destination}")
        print(f"Estimated Ride Time: {ride_time} minutes")
        print(f"\n===Fare: ₹{self.fare}===")

    def schedule_later(self):
        pickup = input("\nEnter the pickup Location: ")
        destination = input("Enter the destination: ")
        pickup_time = input("Enter pickup time (HH:MM): ")

        pickup_to_dest = self.get_distance(pickup, destination)

        if not pickup_to_dest:
            print("Route not available.")
            sys.exit()

        self.fare = self.calculate_fare(pickup_to_dest)

        print(f"\n===Booking Confirmed!!===")
        print(f"Ride scheduled for {pickup_time}")
        print(f"Cab type: {self.cab_type}")
        print(f"\nFrom: {pickup} -> {destination}")
        print(f"\nEstimated fare: ₹{self.fare}")
class Payment:
    def __init__(self, amount):
        self.__amount = amount  # Encapsulation (private variable)

    def make_payment(self):
        mode = input("Enter Payment Mode (Cash/Card/UPI): ")
        if mode not in ["UPI", "Cash", "Card"]:
            print("Invalid payment method")
            sys.exit()
        else:
            print(f"Payment of ₹{self.__amount} made via {mode}. Payment Successful")
class Rating:
    def give_rating(self):
        rating = int(input("Rate your ride (1-5): "))

        if 1 <= rating <= 5:
            print(f"You rated this ride {rating}/5")
            print("THANK YOU")
        else:
            print("Invalid rating. Please rate between 1 and 5.")


print("=== Welcome to Cab Booking System ===")

print("1. Admin Login")
print("2. User Login")

choice = int(input("Enter your choice: "))

if choice == 1:

    admin_username = input("Enter username: ")
    admin_password = input("Enter password: ")

    admin = Admin("admin@123", "2345")

    if admin.login():

        while True:

            print("\n--- Admin Menu ---")
            print("1. Add cab")
            print("2. View cabs")
            print("3. Remove cab")
            print("4. Add route")
            print("5. Remove route")
            print("6. View route")
            print("7. Update fare")

            choice = int(input("Enter choice: "))

            if choice == 1:
                admin.add_cab(cabs)

            elif choice == 2:
                admin.view_cabs(cabs)

            elif choice == 3:
                admin.remove_cab(cabs)

            elif choice == 4:
                admin.add_route(places)

            elif choice == 5:
                admin.remove_route(places)

            elif choice == 6:
                admin.view_routes(places)

            elif choice == 7:
                admin.update_fare()

            else:
                print("Invalid choice.")
                sys.exit()

elif choice == 2:

    user = User("Arya", "arya@gmail.com", "1234")

    enter_email = input("Enter Email: ")
    enter_password = input("Enter Password: ")

    if user.login():

        print("\nAvailable Cab Types:\n1. EV\n2. Sedan\n3. SUV")

        choice = input("\nEnter choice: ")

        if choice == "1":
            ride = Ride("EV", 10, 40)

        elif choice == "2":
            ride = Ride("Sedan", 15, 50)

        elif choice == "3":
            ride = Ride("SUV", 20, 60)

        else:
            print("Invalid choice")
            sys.exit()

        print("\n1. Book Now\n2. Schedule Later")

        option = input("Enter choice: ")

        if option == "1":
            ride.book_now()

        elif option == "2":
            ride.schedule_later()

        else:
            print("Invalid choice")
            sys.exit()

        pay = Payment(ride.fare)
        pay.make_payment()

        rate = Rating()
        rate.give_rating()

        print("\nRide Completed, Thank you for booking with our cab!")

else:
    print("Invalid choice")
    sys.exit()