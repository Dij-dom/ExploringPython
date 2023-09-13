def add_contact(phonebook, name, phone_number, email):
    if name not in phonebook:
        phonebook[name] = (phone_number, email)
        print(f"Contact '{name}' added successfully.")
    else:
        print(f"Contact '{name}' already exists in the phonebook.")

def search_contact(phonebook, name):
    if name in phonebook:
        phone_number, email = phonebook[name]
        print("\nContact Information:")
        print(f"Name: {name}")
        print(f"Phone Number: {phone_number}")
        print(f"Email: {email}")
        # for i in phonebook:
        #     print(phone)
    else:
        print(f"Contact '{name}' not found in the phonebook.")

def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found in the phonebook.")
def display_phonebook(phonebook):
    print("\nPhonebook Entries:")
    for name, (phone_number, email) in phonebook.items():
        print(f"Name: {name}")
        print(f"Phone Number: {phone_number}")
        print(f"Email: {email}")
        print()


phonebook = {}
while True:
    print("\nWelcome to Phonebook Organizer" + "\n1. Add Contact" + "\n2. Search Contact"+ "\n3. Delete Contact" + "\n4. Display Phonebook" + "\n5. Exit")
    ch = input("Enter your choice: \n")
    if ch =="1":
        name = input("Enter Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        add_contact(phonebook, name, phone_number, email)
    elif ch == "2":
        name = input("Enter Name to Search: ")
        search_contact(phonebook, name)
    elif ch == "3":
        name = input("Enter Name to Delete: ")
        delete_contact(phonebook, name)
    elif ch == "4":
        display_phonebook(phonebook)
    elif ch == "5":
        break
    else:
        print("Invalid choice. Try again.")


#In this program, the phonebook is implemented as a dictionary where each key represents a contact's name, and the corresponding value is a tuple containing the contact's phone number and email address. The program provides options to add contacts, search for contacts, delete contacts, display the phonebook, and exit the phonebook organizer.