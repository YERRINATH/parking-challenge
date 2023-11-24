import random
import string

class ParkingLot:
    def __init__(self, square_footage):
        self.square_footage = square_footage
        self.parking_spot_size = 96  # 8x12
        self.spots = []

        # Calculate the number of parking spots based on the square footage
        self.num_spots = square_footage // self.parking_spot_size

        # Initialize the parking lot array with empty values
        for _ in range(self.num_spots):
            self.spots.append(None)

    def park_car(self, car, spot_number):
        if self.spots[spot_number] is not None:
            return f"Car with license plate {car.license_plate} failed to park in spot {spot_number} as it is already occupied."

        else:
            self.spots[spot_number] = car
            return f"Car with license plate {car.license_plate} parked successfully in spot {spot_number}."


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def park(self, parking_lot, spot_number):
        return parking_lot.park_car(self, spot_number)


def main():
    parking_lot_size = int(input('Enter the size of parking lot in sqfeet: '))
    num_of_cars = int(input('Enter the number of cars to park: '))
    parking_lot = ParkingLot(parking_lot_size)

    # Create an array of cars with random license plates
    cars = []
    for i in range(num_of_cars):
        license_plate = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        car = Car(license_plate)
        cars.append(car)

    # Park the cars in the parking lot until the lot is full or all cars are parked
    parked_cars = 0
    for car in cars:
        if parked_cars == parking_lot.num_spots:
            break

        while True:
            spot_number = random.randint(0, parking_lot.num_spots - 1)
            parking_status = car.park(parking_lot, spot_number)
            print(parking_status)

            # If the car successfully parks or fails due to occupancy, break out of the loop
            if parking_status.startswith("Car"):
                parked_cars += 1
                break

            # If the parking lot is full, stop trying to park cars
            if "failed to park in spot" in parking_status:
                break

    # Count the number of available spots after parking all cars
    available_spots = parking_lot.spots.count(None)
    if parked_cars == parking_lot.num_spots:
        print("All available cars have been parked.")
    else:
        print(f"Parking space full. {parked_cars} cars parked.")

    if available_spots > 0:
        print(f"Number of spots still available: {available_spots}")

if __name__ == "__main__":
    main()
