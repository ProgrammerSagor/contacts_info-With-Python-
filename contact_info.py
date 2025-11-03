# Simple Contact Book
# Author: Sagor
# Date: 2025-11-03

contacts = []

def show_contacts():
    if not contacts:
        print("\nNo contacts found. Add some!\n")
    else:
        print("\nContacts List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Contact '{name}' added successfully!\n")

def delete_contact():
    show_contacts()
    if contacts:
        try:
            num = int(input("Enter contact number to delete: "))
            if 1 <= num <= len(contacts):
                removed = contacts.pop(num - 1)
                print(f"Contact '{removed['name']}' deleted successfully!\n")
            else:
                print("Invalid contact number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def main():
    while True:
        print("=== Contact Book ===")
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

