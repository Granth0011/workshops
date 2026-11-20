import json
with open("d://coding//college//workshops//python workshop 1//day 5//1st//employees.json", "r") as file:
    employees = json.load(file)
for e in employees:
    print(e["ename"]+"   "+str(e["salary"])+"   "+e["designation"])



