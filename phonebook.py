import json
import os
from enum import Enum

class Action(Enum):
    PRINT= 0
    ADD = 1
    DELETE =2
    SEARCH =3
    EXIT =5
    SAVE =7

data= []

def firstMenu():
    print("Hello and welcome to your phonebook.  you have to following options : A to add contacts, P to print all contact, D to delete,s to search, X to exit")
    for x in  Action: print(f'{x.value} - {x.name}')
    return Action(int(input ("your selection")))


    

def secMenu():
    while(True):
        result = firstMenu()
        if result == Action.PRINT : readAndPrintJSON()
        # if result ==Action.DELETE : contact_name = input("Enter the name of the contact to delete: "), deleteContact(contact_name)

        if result == Action.ADD : 
            name = input("Please insert name: ")
            tel = input("Please insert Telephone Number: ")
            data.append({"name": name, "tel": tel})
            userInput()
        if result == Action.EXIT : return

def readAndPrintJSON():
    
    global data
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as json_file:
            data = json.load(json_file)
    else:
        print("JSON file doesn't exist.")



def userInput():  
    with open("user_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def deleteContact(name_to_delete):
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as json_file:
            data = json.load(json_file)

        # Find and remove the contact by name
        updated_data = [contact for contact in data if contact["name"] != name_to_delete]

        with open("user_data.json", "w") as json_file:
            json.dump(updated_data, json_file, indent=4)
            print(f"Contact '{name_to_delete}' deleted successfully.")
    else:
        print("JSON file doesn't exist.")        
