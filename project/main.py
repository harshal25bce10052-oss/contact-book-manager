import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as f:
                # Load JSON data from the file
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # Handle cases where the file exists but is empty or corrupted
            return []
    return []

def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE, 'w') as f:
            # Write the contacts list as formatted JSON to the file
            json.dump(contacts, f, indent=4)
    except IOError:
        print("\n[ERROR] Could not save data to file. Check file permissions.")

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name (required): ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()

    if not name:
        print("[ERROR] Name cannot be empty. Contact not added.")
        return

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"\nSUCCESS: Contact '{name}' added and saved.")

def view_contacts(contacts):
    if not contacts:
        print("\n[INFO] The contact book is currently empty.")
        return

    print("\n--- Contact List ---")
    for index, contact in enumerate(contacts):
        print(f"[{index + 1}]")
        print(f"  Name:  {contact['name']}")
        print(f"  Phone: {contact['phone'] if contact['phone'] else 'N/A'}")
        print(f"  Email: {contact['email'] if contact['email'] else 'N/A'}")
        print("-" * 20)
    print(f"Total Contacts: {len(contacts)}")

def search_contacts(contacts):
    if not contacts:
        print("\n[INFO] The contact book is empty, nothing to search.")
        return

    query = input("\nEnter search query (Name, Phone, or Email): ").strip().lower()
    if not query:
        print("[INFO] Search query was empty.")
        return

    results = []
    for contact in contacts:
        # Check if the query is in any of the contact's values
        if (query in contact['name'].lower() or
            query in contact['phone'].lower() or
            query in contact['email'].lower()):
            results.append(contact)

    if results:
        print(f"\n--- Search Results for '{query}' ({len(results)} found) ---")
        for index, contact in enumerate(results):
            print(f"  Result {index + 1}: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
    else:
        print(f"\n[INFO] No contacts found matching '{query}'.")

def delete_contact(contacts):
    if not contacts:
        print("\n[INFO] No contacts to delete.")
        return

    # First, show the current list so the user knows which index to pick
    view_contacts(contacts)

    try:
        index_to_delete = int(input("\nEnter the number/index of the contact to delete: ")) - 1
    except ValueError:
        print("\n[ERROR] Invalid input. Please enter a valid number.")
        return

    if 0 <= index_to_delete < len(contacts):
        deleted_contact = contacts.pop(index_to_delete)
        save_contacts(contacts)
        print(f"\nSUCCESS: Contact '{deleted_contact['name']}' has been deleted.")
    else:
        print("\n[ERROR] Invalid contact number. Deletion failed.")


def display_menu():
    print("\n==================================")
    print("  PYTHON CONTACT BOOK MANAGER (v1)")
    print("==================================")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    print("----------------------------------")

def main():
    contacts = load_contacts()
    print("Welcome to the Console Contact Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("\nThank you for using the Contact Manager. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":

    main()
