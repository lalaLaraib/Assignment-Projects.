"""
This program allows the user to create a phonebook, display saved contacts, 
and search for a contact by name. Users can add names with corresponding 
phone numbers and look up specific contacts.
"""

def get_phone_numbers():
    phone_book = {}
    while True:
        user_name = input("Enter Name (or press enter to exit): ")
        if user_name == "":
            break
        user_number = input("Enter Number (or press enter to exit): ")
        phone_book[user_name] = user_number
    return phone_book

def display_phone_book(phonebook):
    for name, number in phonebook.items():
        print(f"{name}: {number}")

def search_contacts(phonebook):
    while True:
       user_search = input("Enter the name you want to search (or press enter to exit): ")
       if user_search == "":
           break
       if user_search not in phonebook:
           print(f"{user_search} is not found in phonebook.")
       else:
           print(phonebook[user_search])
phoone_book = get_phone_numbers()       
display_phone_book(phoone_book)
search_contacts(phoone_book)    
               
 