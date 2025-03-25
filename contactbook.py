import os

# Define the filename where contacts will be stored
FILE_NAME = "C:\\Users\\arjun\\Desktop\\pioneer projects\\contact_book\\contactbook.txt"

# Function to load contacts from the file
def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts[name] = {'phone': phone, 'email': email}
    return contacts

# Function to save contacts to the file
def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        for name, details in contacts.items():
            file.write(f"{name},{details['phone']},{details['email']}\n")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ")
    if name in contacts:
        print(f"Contact with the name {name} already exists.")
    else:
        phone = input("Enter the phone number: ")
        email = input("Enter the email: ")
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        print(f"Contact for {name} added successfully.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

# Function to search for a contact
def search_contact(contacts):
    name = input("Enter the contact name to search for: ")
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
    else:
        print(f"No contact found with the name {name}.")

# Function to display the main menu
def display_menu():
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Exit")

# Main function to run the contact book application
def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
