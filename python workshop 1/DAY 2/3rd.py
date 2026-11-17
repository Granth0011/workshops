employess=(("nikhil",20000),("neha",12000),("jatin",15000))

print(f"{sum(tuple([i[1] for i in employess]))//len(employess):.2f}")