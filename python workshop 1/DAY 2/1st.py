my_tuple = (1, 2, [3, 4])
my_tuple[2].append(5)
print(my_tuple)

tup=(1, 2,3, 4, 5)
lis=list(tup)

schedule=(("hackathon",10),("Quiz",12),("Robo-Race",15))
x=[i[0] for i in schedule]
print("|".join(x))