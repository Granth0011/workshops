import csv
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# File path global variable
FILE_PATH = r'D:\coding\college\workshops\project\students_marks.csv'

def pychart(marks):
    subjects = ["Python", "Mathematics", "Physics", "English", "Chemistry"]
    mini = marks.index(min(marks))
    x = [0, 0, 0, 0, 0]
    x[mini] = 0.1
    
    plt.figure(figsize=(6, 5))
    plt.pie(marks, labels=subjects, explode=tuple(x), autopct='%1.1f%%', shadow=True)
    plt.title("Marks Distribution")
    plt.show()

def class_average(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            
            total_class_average = 0
            total_students = 0
            
            for row in reader:
                marks = [int(mark) for mark in row[2:]]
                student_avg = sum(marks) / len(marks)
                total_class_average += student_avg
                total_students += 1
                
            return total_class_average / total_students if total_students > 0 else 0
    except FileNotFoundError:
        return 0

def search_student():
    name = entry_name.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Please enter a student name!")
        return

    try:
        with open(FILE_PATH, "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            
            for row in reader:
                if row[1].strip().lower() == name.lower():
                    marks = [int(mark) for mark in row[2:]]
                    total = sum(marks)
                    avg = total / len(marks)
                    c_avg = class_average(FILE_PATH)
                    status = 'Pass' if avg >= 40 else 'Fail'
                    
                    # Update GUI Labels
                    result_text.set(
                        f"Roll No.: {row[0]} \n"
                        f"Name: {row[1]} \n"
                        f"---------------------------\n"
                        f"Total Marks: {total} \n"
                        f"Average Marks: {avg:.2f} \n"
                        f"Highest Marks: {max(marks)} \n"
                        f"Lowest Marks: {min(marks)} \n"
                        f"---------------------------\n"
                        f"Class Average: {c_avg:.2f} \n"
                        f"Status: {status}"
                    )
                    
                    # Show Pie Chart
                    pychart(marks)
                    return
            
            # If loop finishes and student is not found
            result_text.set("")
            messagebox.showerror("Not Found", f"Student '{name}' not found in the records.")
            
    except FileNotFoundError:
        messagebox.showerror("File Error", "CSV file not found! Please check the file path.")

# ==========================
# GUI SETUP (Tkinter)
# ==========================
root = tk.Tk()
root.title("Student Marks Dashboard")
root.geometry("600x700")
root.config(bg="#f4f4f4")

# Heading Label
tk.Label(root, text="Student Result Search", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=20)

# Input Frame
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter Name:", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, padx=5)
entry_name = tk.Entry(input_frame, font=("Arial", 12), width=20)
entry_name.grid(row=0, column=1, padx=5)

# Search Button
search_btn = tk.Button(root, text="Search & Show Chart", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=search_student)
search_btn.pack(pady=15)

# Result Display Area
result_text = tk.StringVar()
result_text.set("Enter a name and click search to see results.")

result_label = tk.Label(root, textvariable=result_text, font=("Courier", 12), bg="white", relief="solid", justify="left", width=35, height=12)
result_label.pack(pady=10)

# Run the Application
root.mainloop()