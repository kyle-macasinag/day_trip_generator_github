import random
from tkinter import Y


def randomize(input):
    d4 = (random.randint(0,3))
    result = input[d4]
    return result

def destination():
    location_not_picked = True
    
    while location_not_picked == True:
        location = randomize(locations) #LOCATIONS
        location_answer = input(f"Does {location} sound good to you? Y/N: ")
        if location_answer == "Y":
            print("Very good.  I'll save this for you.")
            location_not_picked = False
            return location
        elif location_answer != "Y":
            print("Let's try that again!")
 

def movement():
    transit_not_picked = True
    while transit_not_picked == True:
        transit = randomize(transportation) #TRANSIT
        transit_answer = input(f"Would you like to take a/an {transit} to get there? Y/N:")
        if transit_answer == "Y":
            print("You got it!")
            transit_not_picked = False
            return transit
        elif transit_answer != "Y":
            print("Again!")

def restaurants():
    restaurant_not_chosen = True
    go_to = travel
    while restaurant_not_chosen == True:
        if go_to == "Tampa, FL":
            t_restaurant = randomize(tampa_restaurants) #Restaurant
            t_restaurant_choice = input(f"Would you like to try {t_restaurant}? Y/N: ")
            if t_restaurant_choice == "Y":
                print("Bon Appetit")
                restaurant_not_chosen = False
                return t_restaurant
            elif t_restaurant_choice != "Y":
                print("Let's try that again!")
        elif go_to == "Munich, DE":
            m_restaurant = randomize(munich_restaurants)
            m_restaurant_choice = input(f"Would you like to try { m_restaurant}? Y/N: ")
            if m_restaurant_choice == "Y":
                print("Bon Appetite")
                restaurant_not_chosen = False
                return m_restaurant
            elif m_restaurant != Y:
                print("Let's try again!")
        elif go_to == "Erbil, IQ":
            e_restaurant = randomize(erbil_restaurants)
            e_restaurant_choice = input(f"Would you like to try { e_restaurant}? Y/N: ")
            if e_restaurant_choice == "Y":
                print ("Bon Appetite")
                restaurant_not_chosen = False
                return e_restaurant
            elif e_restaurant_choice != "Y":
                print("let's try that again!")
        elif go_to == "Fairbanks, AK":
            f_restaurant = randomize(fairbanks_restaurants)
            f_restaurant_choice = input(f"Would you like to try { f_restaurant}? Y/N ")
            if f_restaurant_choice == "Y":
                print("Bon Appetite")
                restaurant_not_chosen = False
                return f_restaurant
            elif f_restaurant_choice != "Y":
                print("Let's try that again!")
pass

def things_to_do():
    excursion_not_chosen = True
    go_to = travel
    while excursion_not_chosen == True:
        if go_to == "Tampa, FL":
            t_excursion = randomize(tampa_entertainment)
            t_excursion_choice = input(f"Would you like to visit {t_excursion}? Y/N: ")
            if t_excursion_choice == "Y":
                print("Have fun with that!")
                excursion_not_chosen = False
                return t_excursion
            elif t_excursion != "Y":
                print("We'll try that again!")
        elif go_to == "Munich, DE":
            m_excursion = randomize(munich_entertainment)
            m_excursion_choice = input(f"Would you like to visit {m_excursion}? Y/N: ")
            if m_excursion_choice == "Y":
                print("Have fun with that!")
                excursion_not_chosen = False
                return m_excursion
            elif m_excursion_choice != "Y":
                print("We'll try that again!")
        elif go_to == "Erbil, IQ":
            e_excursion = randomize(erbil_entertainment)
            e_excursion_choice = input(f"Would you like to visit {e_excursion}? Y/N: ")
            if e_excursion_choice == "Y":
                print("Have fun with that!")
                excursion_not_chosen = False
                return t_excursion
            elif e_excursion_choice != "Y":
                print("We'll try that again!")
        elif go_to == "Fairbanks, AK":
            f_excursion = randomize(fairbanks_entertainment)
            f_excursion_choice = input(f"Would you like to visit {f_excursion}? Y/N: ")
            if f_excursion_choice == "Y":
                print("Have fun with that!")
                excursion_not_chosen = False
                return f_excursion
            elif f_excursion_choice != "Y":
                print("We'll try that again!")


def all_together():
          print(f"Okay, we have you set for a trip to {travel}, arriving by {means_of_transport}.  You will eat at {choice_of_restaurant}, and you excursion will be {activities}.")
          final_confirmation = False
          edit = input("Would you like to change your destination, transportation, restaurant, or excursion? Y/N:")
          while final_confirmation == False:
                if edit == "Y":
                  print("Wunderbar! Have fun on your trip!")
                  final_confirmation = True
                elif edit == "N":
                    print(f"Okay {username}, let's work together to come up with another plan!")
                    retry()
                else:
                    print('Invalid input.  Please state "Y" or "N"' )  

             
    
         
def retry():
    review = input(f"Your selections were, {travel}, {means_of_transport}, {choice_of_restaurant}, and {activities}.  What would you like to change?")
    if review == travel:
        print("Pass Go")
    elif review == means_of_transport:
        print ("Vroom")
    elif review == choice_of_restaurant:
        print ("Tasty")
    elif review == activities:
        print("BORED")

   


transportation = ["rental car", "train", "airline", "bus"]

locations = ["Tampa, FL", "Munich, DE", "Erbil, IQ", "Fairbanks, AK"]

tampa_restaurants = ["J.Alexander's", "First Watch", "Skipper's Smokehouse and Oyster Bar", "Golden Corral"]

tampa_entertainment = ["Busch Gardens", "Tampa Museum of Art", "SS American Victory", "Florida Museum of Photographic Arts"]

munich_restaurants = ["Hofbrauhaus", "Wirsthaus In Der Au", "Trattoria Da Fausto", "Brasserie OskarMaria"]

munich_entertainment = ["Englischer Garten", "Walking Tour of Nazism", "Maximilianeum Tour", "Dachau Memorial"]

erbil_restaurants = ["Al Bustan Lebanese", "DC Steakhouse", "Basilico", "Zahle"]

erbil_entertainment = ["Erbil Citadel", "Sami Abdulrahman Park", "Erbil Civilisation Museum", "English Village"]

fairbanks_restaurants = ["Shogun's", "AK Buffet", "Denny's", "Mcdonald's"]

fairbanks_entertainment = ["Chena Hot Springs", "Denali National Park", "Chena Lake", "Driving the Dalton Highway"]


username = input("Hello, what would you like me to call you?" )
print(f"Okay {username}, we are going to plan a trip for you!")

print("First, let's plan a destination!")


travel = destination()

means_of_transport = movement()

choice_of_restaurant = restaurants()

activities = things_to_do()

all_together()