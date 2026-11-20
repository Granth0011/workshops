import json

class InvalidContactException(Exception):
    pass
class DuplicateContactException(Exception):
    pass
class ContactNotFoundException(Exception):
    pass

def load_contacts(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty list if the file is missing or completely blank
        return []

def save_contacts(path, contacts):
    # Simply overwrite the file with the current contacts list
    with open(path, "w") as file:
        json.dump(contacts, file, indent=4)

def get_contact_by_name(contacts, name):
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            return i, contact
    raise ContactNotFoundException("Contact not found")

def add_contact(contacts, name, phone, email):
    pass

def update_contact(contacts, name, phone, email):
    pass

def search_contacts(contacts, search_term):
    pass


# Define the path
file = "D:\\coding\\college\\workshops\\python workshop 1\\day 5\\contact-master\\contacts.json"

# Load existing contacts first (creates an empty list if file doesn't exist)
current_contacts = load_contacts(file)

# The new contact you want to add
new_contact = {
    "name": "John Doe",
    "phone": "123-456-7890",
    "email": "john.doe@example.com"
}

# Append the new dictionary to your list of contacts
current_contacts.append(new_contact)

# Save the updated list back to the file
save_contacts(file, current_contacts)