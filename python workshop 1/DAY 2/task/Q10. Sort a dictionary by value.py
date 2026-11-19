marks = {'Riya': 86, 'Arjun': 92, 'Sana': 78, 'Dev': 92}
by_name = sorted(marks.items(), key=lambda item: item[0])
by_marks = sorted(marks.items(), key=lambda item: item[1], reverse=True)
print("By name:", by_name)
print("By marks:", by_marks)
