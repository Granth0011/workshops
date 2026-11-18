crr=["nikhil shri","nishtha gupta","amit arora","neha sahdev pandit"]
print(["".join([i.split()[0][0].upper(),".",i.split()[1].capitalize()]) for i in crr])
print(["".join([j[0].upper()+"."for j in i.split()[:-1]])+i.split()[-1].capitalize() for i in crr])
