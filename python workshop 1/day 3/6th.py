from functools import reduce
employees = [
    (101, "Amit", 85000, "CEO", None, "Management"),
    (102, "Rahul", 70000, "CTO", 101, "IT"),
    (103, "Priya", 65000, "CFO", 101, "Finance"),
    (104, "Neha", 55000, "HR Manager", 101, "HR"),
    (105, "Karan", 60000, "IT Manager", 102, "IT"),
    (106, "Sneha", 45000, "Developer", 105, "IT"),
    (107, "Rohit", 40000, "Developer", 105, "IT"),
    (108, "Pooja", 50000, "Data Analyst", 102, "IT"),
    (109, "Vikas", 48000, "Accountant", 103, "Finance"),
    (110, "Anjali", 42000, "Accountant", 103, "Finance"),
    (111, "Meena", 38000, "HR Executive", 104, "HR"),
    (112, "Arjun", 35000, "HR Executive", 104, "HR"),
    (113, "Sahil", 52000, "Marketing Manager", 101, "Marketing"),
    (114, "Divya", 32000, "Marketing Executive", 113, "Marketing"),
    (115, "Varun", 30000, "Marketing Executive", 113, "Marketing")
]

print("Total IT Salary:",end="")
print(reduce(lambda a, b: a + b,map(lambda e: e[2], filter(lambda e: e[5] == "IT", employees))))

print("Employees under Neha:",end="")
print(list(map(lambda e: e[1], filter(lambda e: e[4] == 104, employees))))

print("Highest Paid Marketing Employee:",end="")
print(reduce(lambda e1, e2: e1 if e1[2] > e2[2] else e2,filter(lambda e: e[5] == "Marketing", employees))[1])