import json
import os
from enum import Enum

class Actions(Enum):
    PRINT= 0
    ADD = 1
    DELETE =2
    SEARCH =3
    EXIT =5
    SAVE =7

contacts = []

def readAndPrintJSON():
    
    global contacts
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as json_file:
            contacts = json.load(json_file)
    else:
        print("JSON file doesn't exist.")


def display_menu() : 
    for x in Actions: print(f'{x.value}- {x.name})')
    return Actions(int(input("your selection ")))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while(True):
        user_selection =display_menu()
        if user_selection == Actions.PRINT : print( contacts)
        if user_selection == Actions.ADD : contacts.append({"name":input("please enter your name"),"tel":input("enter your tel num")})
        if user_selection == Actions.DELETE: 
            del_contact()
        if user_selection == Actions.SEARCH : find_contact()
        if user_selection == Actions.EXIT: return
        if user_selection == Actions.SAVE: saveToJSON()
       
        print(f"your selection is: {Actions( user_selection).name} ")

def saveToJSON():
    with open("user_data.json", "w") as json_file:json.dump(contacts, json_file, indent=4)

def find_contact():
    found = False
    found_contact=""
    search = input("give me name to search ")
    for contact in contacts:
        if contact["name"] == search:
            found = True
            found_contact = contact
    if found :
        print(found_contact)
        return found_contact
    return None

def del_contact():
    contact =find_contact()
    if contact != None:
        contacts.remove(contact)
        print("del" , contact)
    else:
        print("no such contact")

if __name__ == '__main__':
    clear_screen()
    readAndPrintJSON()
    menu()
    print("Thank u 4 using my program")
