import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email, address):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    return "Contact added successfully!"

def view_contacts():
    contacts = load_contacts()
    return contacts if contacts else "No contacts found."

def search_contact(query):
    contacts = load_contacts()
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    return results if results else "No matching contact found."

def update_contact(name, new_phone=None, new_email=None, new_address=None):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            save_contacts(contacts)
            return "Contact updated successfully!"
    return "Contact not found."

def delete_contact(name):
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        return "Contact deleted successfully!"
    return "Contact not found."

def main():
    print("Contact Management System is ready.")

if __name__ == "__main__":
    main()