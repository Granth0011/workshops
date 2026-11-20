import csv
from os import name
import matplotlib.pyplot as plt
import numpy as np
def pychart(dataa):
    subject=["Python","Mathematics","Physics","English","Chemistry"]
    mini=dataa.index(min(dataa))
    x=[0,0,0,0,0]
    x[mini]=0.1
    plt.pie(dataa,labels=subject,explode=tuple(x),autopct='%1.1f%%',shadow=True)
    plt.title("Marks Distribution")
    plt.show()

def class_average(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row
        
        total_class_average = 0
        total_students = 0
        
        for row in reader:
            # Convert marks to integers
            marks = [int(mark) for mark in row[2:]]
            student_avg = sum(marks) / len(marks)
            
            total_class_average += student_avg
            total_students += 1
            
        return total_class_average / total_students if total_students > 0 else 0

def data(name, file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row
        
        for row in reader:
            # Check if name matches (strip spaces and ignore case)
            if row[1].strip().lower() == name.strip().lower():
                marks = [int(mark) for mark in row[2:]]
                total = sum(marks)
                avg = total / len(marks)
                
                print(f"Roll No.: {row[0]}" , end="     ")
                print(f"Name: {row[1]}")
                print(f"Total Marks: {total}")
                print(f"Average Marks: {avg:.2f}", end="    ")
                print(f"Highest Marks: {max(marks)}", end="     ")
                print(f"Lowest Marks: {min(marks)}",end="   ")
                print(f"Class Average Marks: {class_average(file_path):.2f}")
                print(f"Pass or Fail: {'Pass' if avg >= 40 else 'Fail'}")
                return
        
        print(f"Student '{name}' not found in the records.")

# Set your file path here
file_path = r'D:\coding\college\workshops\project\students_marks.csv'
search_name = input("Enter the Name: ")
data(search_name, file_path)
with open(file_path, "r") as file:
    reader = csv.reader(file) 
    next(reader, None)  # Skip the header row
    for row in reader:
        if row[1].strip().lower() == search_name.strip().lower():
            dataa=list(map(int,row[2:]))
            pychart(dataa)