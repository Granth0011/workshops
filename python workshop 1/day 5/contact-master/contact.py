import json
import re
EMAIL_RG = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_RG = r"^[6-9][0-9]{9}$"
Name_RG = r"^[a-zA-Z\s]+$"
class InvalidContactException(Exception):
    pass
class DuplicateContactException(Exception):
    pass
class ContactNotFoundException(Exception):
    pass

#loading all the contacts from the file
def load_contacts(path):
    try:
      with open(path, "r") as f:
        contacts = json.load(f)
        return contacts
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return []

def clean_and_validate_phone(phone):
    phone = phone.strip()
    if not re.fullmatch(PHONE_RG,phone):
        raise InvalidContactException(f"Invalid phone number: {phone}")
    return phone
def clean_and_validate_email(email):
    email = email.strip()
    if not re.fullmatch(EMAIL_RG,email):
        raise InvalidContactException(f"Invalid email: {email}")
    return email

#save all the contacts in the file.
def save_contact(contacts, path):
    with open(path, "w") as file:
        json.dump(contacts, file, indent=4)

#get the index of the contact with the mentioned name
def get_contact_by_name(contacts , name):
    for i , contact in enumerate(contacts):
        if contact["name"].strip().lower() == name.strip().lower():
            return i
    return -1

def add_contact(contacts , name , email , phone):
    name=name.strip()
    if not name:
        raise InvalidContactException("Name is required")
    if not email:
        raise InvalidContactException("Email is required")
    if not phone:
        raise InvalidContactException("Phone is required")
    if get_contact_by_name(contacts, name) != -1:
        raise DuplicateContactException(f"Contact with name {name} already exists")
    email=clean_and_validate_email(email)
    phone=clean_and_validate_phone(phone)
    contacts.append({"name":name, "email":email, "phone":phone})
    return contacts

def update_contact(contacts , name , email , phone):
    i=get_contact_by_name(contacts, name)
    if i==-1:
        raise ContactNotFoundException(f"Contact with name {name} not found")
    email = clean_and_validate_email(email)
    phone = clean_and_validate_phone(phone)
    contacts[i]["email"] = email
    contacts[i]["phone"] = phone
    return contacts

def delete_contact(contacts , name):
    i = get_contact_by_name(contacts, name)
    if i == -1:
        raise ContactNotFoundException(f"Contact with name {name} not found")
    return contacts.pop(i)

def search_contact(contacts , search_term):
    pass


def main(path="contacts.json"):
    contacts = load_contacts(path)
    print(f"contact book loaded {len(contacts)} are presecent")
    MENU="1. Add contact  2. Update contact  3. Delete contact  4.Exit"
    while True:
       print("\n"+MENU)
       choice=int(input("Enter your choice: "))
       try:
        if choice==1:
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone: ")
            add_contact(contacts , name , email , phone)
            save_contact(contacts, path)
        elif choice==2:
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone: ")
            update_contact(contacts , name , email , phone)
            save_contact(contacts, path)
        elif choice==3:
            name = input("Enter contact name: ")
            delete_contact(contacts , name)
            save_contact(contacts, path)
        elif choice==4:
            break
        else:
            print("invalid choice")
       except InvalidContactException as e:
           print(e)
       except DuplicateContactException as e:
           print(e)
       except ContactNotFoundException as e:
           print(e)
main(path="contacts.json")