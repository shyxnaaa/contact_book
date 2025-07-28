import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print("Contact added.")

def find_contact(contacts, query):
    return [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]

def update_contact(contacts):
    query = input("Search name or phone to update: ").strip()
    matches = find_contact(contacts, query)
    if not matches:
        print("No contact found.")
        return
    for idx, c in enumerate(matches):
        print(f"{idx+1}. {c}")
    choice = int(input("Select contact number to update: ")) - 1
    if 0 <= choice < len(matches):
        contact = matches[choice]
        contact['name'] = input(f"New name [{contact['name']}]: ") or contact['name']
        contact['phone'] = input(f"New phone [{contact['phone']}]: ") or contact['phone']
        contact['email'] = input(f"New email [{contact['email']}]: ") or contact['email']
        print("Contact updated.")
    else:
        print("Invalid selection.")

def delete_contact(contacts):
    query = input("Search name or phone to delete: ").strip()
    matches = find_contact(contacts, query)
    if not matches:
        print("No contact found.")
        return
    for idx, c in enumerate(matches):
        print(f"{idx+1}. {c}")
    choice = int(input("Select contact number to delete: ")) - 1
    if 0 <= choice < len(matches):
        contacts.remove(matches[choice])
        print("Contact deleted.")
    else:
        print("Invalid selection.")

def search_contacts(contacts):
    query = input("Search name or phone: ").strip()
    matches = find_contact(contacts, query)
    if matches:
        for c in matches:
            print(c)
    else:
        print("No contact found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact\n2. Update Contact\n3. Delete Contact\n4. Search Contact\n5. List All\n6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            update_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            for c in contacts:
                print(c)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()