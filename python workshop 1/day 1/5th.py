#  2 teams are given add tem
team1=input().split()
team2=input().split()
team=team1+team2
attendence=["p"]*5
if "chirag" in team:
    print("chirag hai? yes")
else:
    print("chirag hai? No")
if "esha" in team:
    print("esha hai? yes")
else:
    print("esha hai? No")
print(team)