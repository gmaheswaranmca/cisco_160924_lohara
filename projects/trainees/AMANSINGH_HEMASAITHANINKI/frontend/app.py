import json
import requests
class Flight:
    def __init__(self, flight_number, flight_name, capacity):
        self.url = 'http://localhost:5000'
        self.flight_number = flight_number
        self.flight_name = flight_name
        self.capacity = capacity
        self.seats = {
            'premium': {
                'window': int(capacity * 0.05),
                'middle': int(capacity * 0.02),
                'aisle': int(capacity * 0.03)
            },
            'business': {
                'window': int(capacity * 0.10),
                'middle': int(capacity * 0.05),
                'aisle': int(capacity * 0.05)
            },
            'regular': {
                'window': int(capacity * 0.35),
                'middle': int(capacity * 0.20),
                'aisle': int(capacity * 0.15)
            }
        }
        self.bookings = []

    def __str__(self):
        return f'[Flight Number={self.flight_number}, Flight Name={self.flight_name}, Capacity={self.capacity}, Seats={self.seats}]'

    def __repr__(self):
        return self.__str__()

class Booking:
    def __init__(self, booking_id, flight_number, seat_type, seat_position):
        self.booking_id = booking_id
        self.flight_number = flight_number
        self.seat_type = seat_type
        self.seat_position = seat_position

    def __str__(self):
        return f'[Booking ID={self.booking_id}, Flight Number={self.flight_number}, Seat Type={self.seat_type}, Seat Position={self.seat_position}]'

    def __repr__(self):
        return self.__str__()

flights = []
bookings = []

# Flight management functions
def add_flight(flight_number, flight_name, capacity):
    global flights
    flight = Flight(flight_number, flight_name, capacity)
    flights.append(flight)
    print('Flight added successfully')

def book_ticket(booking_id, flight_number, seat_type, seat_position):
    global flights, bookings
    for flight in flights:
        if flight.flight_number == flight_number:
            if flight.seats[seat_type][seat_position] > 0:
                flight.seats[seat_type][seat_position] -= 1
                booking = Booking(booking_id, flight_number, seat_type, seat_position)
                bookings.append(booking)
                print('Ticket booked successfully')
                print_remaining_seats(flight_number)
            else:
                print(f'No {seat_position} {seat_type} seats available')
            return
    print(f'No such flight number {flight_number}')

def confirm_booking(booking_id):
    global bookings
    for booking in bookings:
        if booking.booking_id == booking_id:
            print(f'Booking confirmed: {booking}')
            return
    print(f'No such booking ID {booking_id}')

def display_flights():
    global flights
    for flight in flights:
        print(flight)

def display_bookings():
    global bookings
    for booking in bookings:
        print(booking)

def update_booking(booking_id, new_seat_type, new_seat_position):
    global bookings, flights
    for booking in bookings:
        if booking.booking_id == booking_id:
            for flight in flights:
                if flight.flight_number == booking.flight_number:
                    if flight.seats[new_seat_type][new_seat_position] > 0:
                        flight.seats[booking.seat_type][booking.seat_position] += 1
                        flight.seats[new_seat_type][new_seat_position] -= 1
                        booking.seat_type = new_seat_type
                        booking.seat_position = new_seat_position
                        print('Booking updated successfully')
                        print_remaining_seats(flight.flight_number)
                    else:
                        print(f'No {new_seat_position} {new_seat_type} seats available')
                    return
    print(f'No such booking ID {booking_id}')

def cancel_booking(booking_id):
    global bookings, flights
    for booking in bookings:
        if booking.booking_id == booking_id:
            for flight in flights:
                if flight.flight_number == booking.flight_number:
                    flight.seats[booking.seat_type][booking.seat_position] += 1
                    bookings.remove(booking)
                    print('Booking canceled successfully')
                    print_remaining_seats(flight.flight_number)
                    return
    print(f'No such booking ID {booking_id}')

def print_remaining_seats(flight_number):
    global flights
    for flight in flights:
        if flight.flight_number == flight_number:
            print(f'Remaining seats for flight {flight_number}: {flight.seats}')
            return

def write_flights_to_json(filename='flights_list.json'):
    global flights
    data = [{'flight_number': flight.flight_number, 'flight_name': flight.flight_name, 'capacity': flight.capacity, 'seats': flight.seats} for flight in flights]

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print(f'Data written to {filename}')

def select_seat_type():
    seat_type = input('Choose seat type (premium/business/regular): ').lower()
    while seat_type not in ['premium', 'business', 'regular']:
        print("Invalid seat type. Please choose 'premium', 'business', or 'regular'.")
        seat_type = input('Choose seat type (premium/business/regular): ').lower()
    return seat_type

def select_seat_position():
    seat_position = input('Choose seat position (window/middle/aisle): ').lower()
    while seat_position not in ['window', 'middle', 'aisle']:
        print("Invalid seat position. Please choose 'window', 'middle', or 'aisle'.")
        seat_position = input('Choose seat position (window/middle/aisle): ').lower()
    return seat_position

# Menu functions
def menu():
    choice = int(input('''1-Add flight
2-Display all flights
3-Book ticket
4-Confirm booking
5-Display all bookings
6-Update booking
7-Cancel booking
8-Save flights to JSON
9-End
Your choice: '''))
    
    if choice == 1:
        flight_number = input('Enter flight number: ')
        flight_name = input('Enter flight name: ')
        capacity = int(input('Enter flight capacity: '))
        add_flight(flight_number, flight_name, capacity)
    elif choice == 2:
        display_flights()
    elif choice == 3:
        booking_id = int(input('Enter booking ID: '))
        flight_number = input('Enter flight number: ')
        seat_type = select_seat_type()
        seat_position = select_seat_position()
        book_ticket(booking_id, flight_number, seat_type, seat_position)
    elif choice == 4:
        booking_id = int(input('Enter booking ID: '))
        confirm_booking(booking_id)
    elif choice == 5:
        display_bookings()
    elif choice == 6:
        booking_id = int(input('Enter booking ID: '))
        new_seat_type = select_seat_type()
        new_seat_position = select_seat_position()
        update_booking(booking_id, new_seat_type, new_seat_position)
    elif choice == 7:
        booking_id = int(input('Enter booking ID: '))
        cancel_booking(booking_id)
    elif choice == 8:
        write_flights_to_json()
    elif choice == 9:
        pass
    else:
        print('Invalid menu')
    
    return choice

def menus():
    choice = menu()
    while choice != 9:
        choice = menu()
    print('Thank you for using the app')

# Initialize the database and run the menu
#airplaneTablesCreate()
menus()