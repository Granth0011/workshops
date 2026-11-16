# record=eval(input("Enter a list of records: "))
record=[
    "  aNITA sharma , anita@gmail.com , 20 ",
    "rohan mehta, rohan@yahoo.in, 19",
    "  KAVYA RAO, kavya.rao@gmail.com, twenty "
]

for i in record:
    name,email,age=i.split(",")
    name=name.strip().capitalize()
    email=email.strip().lower()
    age=age.strip()
    print(f"Name: {name}, Email: {email}, Age: {age}")   