import csv

# File name where contacts will be stored
CONTACTS_FILE = 'contacts.csv'

# Function to load contacts from the file
def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    except FileNotFoundError:
        with open(CONTACTS_FILE, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
    return contacts

# Function to save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(contacts)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

# Function to search for a contact by name
def search_contact(contacts):
    name = input("Enter name to search: ")
    found_contacts = [contact for contact in contacts if contact['Name'].lower() == name.lower()]
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    else:
        print("Contact not found.")

# Function to update a contact
def update_contact(contacts):
    name = input("Enter name of the contact to update: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contact['Phone'] = input(f"Enter new phone number (current: {contact['Phone']}): ")
            contact['Email'] = input(f"Enter new email (current: {contact['Email']}): ")
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter name of the contact to delete: ")
    new_contacts = [contact for contact in contacts if contact['Name'].lower() != name.lower()]
    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu function
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()