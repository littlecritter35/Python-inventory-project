"""Create an automobile class that will be used by a dealership as a vehicle inventory program.  
The following attributes should be present in your automobile class:

private string make
private string model
private string color
private int year
private int mileage
Your program should have appropriate methods such as:

add a new vehicle
remove a vehicle"""

class Car:
    #Class attributes
    make_counter = {} 
    """this is to store how many of each make there is on the lot, incrementing by 1 each time a new make is added to the lot."""

    vehicles_on_lot = {}
    """This will store each vehicle as a key:value pair, where the key is the model + a unique number ID, and the value is the 
    model, color, year, and mileage.
    Example: 'Toyota1' : ['Camry', 'Blue', 2012, 13000]"""
     

    def __init__(self, make = '', model = '', color = '', year = 0, mileage = 0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def _increment_make(self):
        if self.make in Car.make_counter: 
            Car.make_counter[self.make] += 1
            """If this is not the first time the particular make has been added to the inventory, then the value associated with the 
            make key will increase by 1"""
        else:
            Car.make_counter[self.make] = 1
            """If this is the first time the particular make has been added to the inventory, then the value associated with the make will
            be added to the dictionary at a value of 1"""
    
    def _add_vehicle(self):
        """Every time a new vehicle is added, the vehicle's make increments the Car.make_counter, and a new key is dynamically created
        using self.make and the make's value in Car.make_counter"""
        self._increment_make()
        dict_key = self.make + str(Car.make_counter[self.make])
        Car.vehicles_on_lot[dict_key] = [self.model, self.color, self.year, self.mileage]
        print('Vehicle added.\n\n')
    
    # class methods. Don't need to create a new instance when called
    def _del_vehicle(cls, key_to_del): 
        if key_to_del in cls.vehicles_on_lot:
            del cls.vehicles_on_lot[key_to_del]
            print('Vehicle successfully removed from inventory.\n\n')
        else:
            print('Vehicle not found.\n\n')

    def _search_by_value(cls, search_criteria):
        keys = [key for key, val in Car.vehicles_on_lot.items() if val == search_criteria]
        return keys

# Function created outside of main program
def get_user_input():
    user_input = input(f'{menu}Enter command: ').strip()
    return user_input 

menu = ('(1) Add a new car to lot.\n'  # this will run _add_vehicle
    '(2) Remove vehicle from lot.\n'  # this will delete a vehicle from the lot
    '(3) Search lot by in-house vehicle ID or by vehicle specs.\n'  # searches the lot based on either key or value
    '(4) Print inventory.\n' # prints the full inventory
    '(5) Exit.\n\n') # quits program

if __name__ == "__main__":
    
    user_input = get_user_input()

    if user_input == '5':
        quit
        """def __init__(self, make = '', model = '', color = '', year = 0, mileage = 0):"""
    while user_input != '5':
        if user_input == '1':
            new_car = Car()
            print("Please enter the following information about the new vehicle:")
            new_car.make = input('Make: ').strip().title()
            new_car.model = input('Model: ').strip().title()
            new_car.color = input('Color: ').strip().title()
            new_car.year = int(input('Year: '))
            new_car.mileage = int(input('Number of miles: '))
            new_car._add_vehicle()
            user_input = get_user_input()

        elif user_input == '2':
            key_to_del = input('Please enter the inventory ID of the vehicle: ')
            Car._del_vehicle(Car, key_to_del)
            user_input = get_user_input()

        elif user_input == '3':
            is_key_known = input('Is the vehicle inventory ID known, yes or no? ').strip().lower()
            if is_key_known == 'yes':
                key_search = input('Enter vehicle inventory ID: ')
                print(f'The vehicle specs for {key_search} are {Car.vehicles_on_lot.get(key_search)}\n\n')
                user_input = get_user_input()
            elif is_key_known == 'no':
                print('Please enter the following')
                model_search = input('Model: ').strip().title()
                color_search = input('Color: ').strip().title()
                year_search = int(input('Model year: '))
                miles_search = int(input('Mileage: '))
                value_search = [model_search, color_search, year_search, miles_search]
                print(f'The vehicle inventory ID(s) matching this search is/are {Car._search_by_value(Car, value_search)}\n\n')
                user_input = get_user_input()

        elif user_input == '4':
            for key, value in Car.vehicles_on_lot.items():
                print(key, value)
            
            print('\n\n')
            user_input = get_user_input()

        else:
            print('Invalid input, please try again.\n\n')
            user_input = get_user_input()

"""Further development possibilities: figure out a way to turn each key into a barcode that is printable along with the information 
about the vehicle so that it can be attached to the physical vehicle on the lot and used to pull up the vehicle information in the inventory.
This would allow for even quicker search times, and whoever is processing the vehicle for sale does not need to search for the vehicle using
the search method above. 

I would also want to fine tune the search by value function so that you can choose which value to search by, and it would return the keys for
all the key/value pairs in the inventory dictionary. For instance, if someone knew that they wanted a vehicle with 50,000 miles or less, or if
they just really loved the idea of a blue car. The only catch is with the current set up, I don't think you could search by make. Perhaps, 
another option for in the future would be to have nested dictionaries, where the outermost keys would be vehicle brands and their paired values
would be the dictionaries that I currently have. 

But that is all for another time ^_^ """