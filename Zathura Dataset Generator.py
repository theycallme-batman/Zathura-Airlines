#pip install indian-names
#pip install random-word
#pip install random
#pip install pandas
#pip install faker


#imports
import pandas as pd
import indian_names
import random
from random_word import RandomWords
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()


def generate_aadhar_number():
    return ' '.join(''.join(map(str,random.sample(range(10), 4))) for x in range(3))


def generate_passport_number():
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = random.choices(alphabets)[0]
    number =letter + str(random.randint(1,9)) + str(random.randint(0,9))\
                + ''.join(map(str,random.sample(range(10),4))) + str(random.randint(1,9)) 
    return number


def generate_phone_number():
    phone_number = ''
    
    #first number should be between 6-9
    phone_number += (str(random.randint(6,9)))
    
    for i in range(1, 10): 
        phone_number += (str(random.randint(0, 9))) 
        
    return phone_number

def generate_email(choices):
    number_choice = [''.join(map(str,random.sample(range(10),x))) for x in range(2,5)]
    domain_choice = ['gmail.com','yahoo.com','hotmail.com']
    return random.choices(choices,weights = [0.5,0.3,0.1,0.1])[0] + '.' + random.choices(choices,weights = [0.3,0.5,0.1,0.1])[0] + random.choice(number_choice) + '@' + random.choice(domain_choice)

class Passenger:
    def __init__(self):
        gender = random.choice(["male","female"])
        self.first_name = indian_names.get_first_name(gender)
        self.last_name = indian_names.get_last_name()
        self.age = random.randint(5, 80)
        if(self.age > 18):
            self.gender = random.choices([gender,"Others"],weights = [0.95,0.05])[0]
        else:
            self.gender = gender
        if(self.age < 15):
            self.contact_number = ""
            self.email_id = ""
            self.last_name = ""
        else: 
            self.contact_number = generate_phone_number()
            self.email_id = generate_email([self.first_name,self.last_name,RandomWords().get_random_word(),RandomWords().get_random_word()])
        self.aadhar_number = generate_aadhar_number()
        self.passport_number = random.choice([generate_passport_number(),""])


class Airplanes:
    def __init__(self,airplane_type,airplane_name,frequency):
        if(airplane_type == 'Boeing 777X'):
            self.fuel_capacity = 350410 #lbs
            self.seats = 384
            self.classes = {
                            "Economy" : { "seat_type" : "D"   ,"seats": 160 ,"window_seats": 30},
                            "Premium_Economy": { "seat_type" : "C" ,"seats": 104 , "window_seats": 25 } ,
                            "Business" : { "seat_type" : "B"   ,"seats": 70,"window_seats": 20} ,
                            "First_class": { "seat_type" : "A"   ,"seats": 50,"window_seats": 15}
                           }
            self.range = 16190 #km
            self.window_seats = 90
            self.base_price = 5000
        elif(airplane_type == 'Airbus A220'):
            self.fuel_capacity = 21805 
            self.seats = 160
            self.classes = {
                            "Economy" : { "seat_type" : "D"   ,"seats": 100 ,"window_seats": 30  },
                            "Premium_Economy": { "seat_type" : "C"   ,"seats": 60,"window_seats": 20}
                            }
            self.range = 6390 #km
            self.window_seats = 50
            self.base_price = 3000
        elif(airplane_type == 'Airbus A320'):
            self.fuel_capacity = 27200
            self.seats = 186
            self.range = 6150
            self.classes = {
                            "Economy" : { "seat_type" : "D"   ,"seats": 70 ,"window_seats": 20},
                            "Premium_Economy": { "seat_type" : "C" ,"seats": 50 , "window_seats": 20 } ,
                            "Business" : { "seat_type" : "B"   ,"seats": 40,"window_seats": 10} ,
                            "First_class": { "seat_type" : "A"   ,"seats": 26,"window_seats": 10}
                           }
            self.window_seats = 60
            self.base_price = 3500
            
        self.name = airplane_name
        self.airplane_id = airplane_name[:3] + '-' + airplane_type[:3]
        self.type = airplane_type
        self.current_fuel = 0
        self.frequency = frequency

class Airport:
    def __init__(self,airport_name):
        self.name = airport_name
        self.code = airport_name[:3].upper()
        self.airplanes = set()


class Flight:
    def __init__(self,airplane,source_airport,destination_airport,flight_id,start_time,hour):
        curr_airplane = airplane   #We will pick each plane and check whether it wants to go or no
                
        #current airplane data
        self.id = flight_id
        self.total_seats  = curr_airplane.seats  
        self.flight_code = curr_airplane.airplane_id
        self.classes = curr_airplane.classes
        self.base_price = curr_airplane.base_price
        self.departure_time = random.choice([(start_time + timedelta(minutes= - random.randint(0,3)))
                                             ,(start_time + timedelta(minutes= random.randint(0,15)))])
        self.arrival_time = random.choice([(self.departure_time + timedelta(hours=hour) + timedelta(minutes = -random.randint(0,15))) \
                                           ,(self.departure_time + timedelta(hours=hour) + timedelta(minutes = random.randint(0,15)))])
        self.source = source_airport
        self.destination = destination_airport
        self.passengers = [] 
        self.status = None
        self.comments = None
       
        
    def get_flight_data(self):
        return {
            "id" : self.id
            ,"flight_code" : self.flight_code
            ,"source" : self.source
            ,"destination" : self.destination
            ,"departure_time" : self.departure_time
            ,"arrival_time" : self.arrival_time
            ,"passenger_data" : self.passengers
            ,"total_seats" : self.total_seats      
        }
        
    def fill_flight(self):
        base_price = self.base_price
        flight_classes = self.classes
        for flight_class in list(flight_classes.keys()):
            total_seats = flight_classes[flight_class]["seats"]
            window_seats = flight_classes[flight_class]["window_seats"]
            seat_type = flight_classes[flight_class]["seat_type"]
            while total_seats > 0:
                boarding = random.choices(["Yes","No"],weights = [0.9,0.1])[0]
                if(boarding):
                        cash = base_price
                        if(seat_type == 'A'):
                            cash += base_price*0.4
                        elif(seat_type == 'B'):
                            cash += base_price*0.3
                        elif(seat_type == 'C'):
                            cash += base_price*0.2
    
                        seat_number = seat_type +'-'+ str(total_seats)
                        
                        window = random.choices(["Yes","No"],weights = [0.4,0.6])[0]
                        if(window_seats > 0 and window):
                            seat_number = seat_number + '(W)'
                            cash += base_price * 0.1
                            window_seats -= 1
                        
                        passenger = Passenger()
                        
                        passenger_data = {
                            "first_name" : passenger.first_name
                            ,"last_name" : passenger.last_name
                            ,"age" : passenger.age
                            ,"gender" : passenger.gender
                            ,"contact_number" : passenger.contact_number
                            ,"email_id" : passenger.email_id
                            ,"aadhar_number" : passenger.aadhar_number
                            ,"passport_number" : passenger.passport_number
                            ,"seat": seat_number
                            ,"fare" : cash    
                        }
                            
                        self.passengers.append(passenger_data)                     
                            
                total_seats -= 1
                print(f'Loading...{total_seats}')
        
        

class Zathura:
    
    #Constructor
    def __init__(self):
        
        #Initialization the harcoded value + data structures
        self.global_flight_id = 100001  
        self.aircraft_models = {
            'Boeing 777X': ['Garuda', 'Vimana', 'Vayu', 'Ananta'],
            'Airbus A220': ['Agni', 'Astra', 'Vajra'],
            'Airbus A320': ['Rudra', 'Marut']
        }
        self.airports = ["Mumbai","Delhi","Pune","Banglore","Hydrebad"]
        self.airport_data = {}
        self.flights_data = []
        self.airplane_data = []
        self.airplane_initials = {
            'Garuda' : {'frequency' : '1357' ,'source' : 'Pune', 'destination' : 'Delhi' , 'timings' :[7,12,17,23], 'index': 0, 'hours' : 2} , 
            'Vimana' : {'frequency' : '1357' ,'source' : 'Mumbai', 'destination' : 'Delhi', 'timings' :[6,12,18] , 'index' : 0,'hours' : 2 } ,
            'Vayu' : {'frequency' : '246' ,'source' : 'Hydrebad', 'destination' : 'Delhi', 'timings' :[9,13,19,23] , 'index' : 0, 'hours' : 3},
            'Ananta' : {'frequency' : '246' ,'source' : 'Delhi', 'destination' : 'Banglore','timings' :[6,11,17] , 'index' : 0,'hours' : 4} ,
            'Agni': {'frequency' : '12345' ,'source' : 'Banglore', 'destination' : 'Pune','timings' :[5,10,15,20] , 'index' : 0,'hours' : 3 },
            'Astra' : {'frequency' : '12345' ,'source' : 'Banglore', 'destination' : 'Mumbai','timings' :[7,12,17,23] , 'index' : 0,'hours' : 3},
            'Vajra' : {'frequency' : '123456' ,'source' : 'Pune', 'destination' : 'Hydrebad','timings' :[6,11,16,21] , 'index' : 0,'hours' : 2} ,
            'Rudra' : {'frequency' : '123456' ,'source' : 'Mumbai', 'destination' : 'Hydrebad','timings' :[12,17] , 'index' : 0,'hours' : 2},
            'Marut' : {'frequency' : '123456' ,'source' : 'Mumbai', 'destination' : 'Pune','timings' :[6,12,18] , 'index' : 0,'hours' : 1}
        }
        self.start_date = datetime.strptime('2024-02-25', "%Y-%m-%d") 
        self.end_date = datetime.strptime('2024-02-25', "%Y-%m-%d") 
     
    
    #Setting airport data
    def set_airport_data(self):
        for airport in self.airports:
            self.airport_data[airport] = (Airport(airport)) 
            
    #Setting airplane_data
    def set_airplane_data(self):
        for model in self.aircraft_models:
                for model_name in self.aircraft_models[model]:
                        self.airplane_data.append(Airplanes(model,model_name,self.airplane_initials[model_name]['frequency']))
           
    #Setting airplanes to a initial airport
    def set_inital_airplanes_to_airports(self):
        for airplane in self.airplane_data:
            airport = self.airplane_initials[airplane.name]['source']
            self.airport_data[airport].airplanes.add(airplane)
    
    #Schedule flights
    def schedule_flights(self):
        while self.start_date <= self.end_date:
            
            curr_weekday = self.start_date.weekday()+1
            print(curr_weekday)
            
            #trackers are used to remove and add airplanes from source to destination airport
            destination_tracker = { airport_name : set() for airport_name in self.airports}
            source_tracker = { airport_name : set() for airport_name in self.airports}

            
            flag = True
            
            #Will go through all airports and schedule flight for each airplane present in the airport
            for airport in self.airports:

                source_airport = airport          
                source_airport_data = self.airport_data[source_airport] 
                source_airplanes = source_airport_data.airplanes

                #running for each airplane
                
                
                
                for airplane in source_airplanes:

                    print(airplane.name)
                    freq = self.airplane_initials[airplane.name]['frequency']
                    
                    size = len(self.airplane_initials[airplane.name]['timings'])
                    index = self.airplane_initials[airplane.name]['index']
                    
                    if(str(curr_weekday) in freq and index < size):
                        flag = False
                        
                        hour = self.airplane_initials[airplane.name]['hours']
                        time = self.airplane_initials[airplane.name]['timings'][index]
                        
                        #finding destination
                        destination_airport = self.airplane_initials[airplane.name]['destination']
                        print(f"{airplane.name} => {self.airplane_initials[airplane.name]} => {self.airplane_initials[airplane.name]['destination']}")
                        #scheduling_flight
                        flight = Flight(airplane,source_airport,destination_airport,self.global_flight_id,(self.start_date + timedelta(hours = time)),hour)
                        flight.fill_flight()
                        self.flights_data.append(flight.get_flight_data())

                        self.airplane_initials[airplane.name]['index'] += 1

                        #managing trackers
                        print(destination_airport)
                        source_tracker[source_airport].add(airplane)
                        destination_tracker[destination_airport].add(airplane)

                        self.airplane_initials[airplane.name]['destination'] = self.airplane_initials[airplane.name]['source']
                        self.airplane_initials[airplane.name]['source'] = destination_airport

                        self.global_flight_id += 1
                        
            #fixing trackers for the next run
            for airport in self.airports:
                self.airport_data[airport].airplanes = self.airport_data[airport].airplanes | destination_tracker[airport]
                self.airport_data[airport].airplanes = self.airport_data[airport].airplanes - source_tracker[airport]
                
            if(flag): 
                self.start_date = self.start_date + timedelta(days = 1)
                for airplane in self.airplane_data:
                    self.airplane_initials[airplane.name]['index'] = 0
                

    def get_print(self):
        for airport in self.airports:
            curr_airport = self.airport_data[airport]
            print(f"{curr_airport.name}- ")
            for ap in curr_airport.airplanes:
                print(f" \t\t {ap.name}")
                
                
    def show_data(self):
        flight_schedules_df = pd.DataFrame(self.flights_data)
        display(flight_schedules_df)
        

if __name__ == '__main__':
    zathura = Zathura()
    zathura.set_airplane_data()
    zathura.set_airport_data()
    print("Abc")
    zathura.set_inital_airplanes_to_airports()
    zathura.get_print()

    zathura.schedule_flights()
    zathura.get_print()

    df = pd.DataFrame(zathura.flights_data)
    print(df)