employees = [
    "Amit",
    "Rahul",
    "Priya",
    "Neha",
    "Vikas",
    "Sneha",
    "Arjun",
    "Kavita",
    "Rohit",
    "Pooja"
]

salaries = [
    45000,
    55000,
    60000,
    40000,
    75000,
    50000,
    85000,
    65000,
    70000,
    48000
]
x=input()
if x not in employees:
    print("chal be")
else:
    z=employees.index(x)
    print("NAME: ",x , "Salary: ",salaries[z])