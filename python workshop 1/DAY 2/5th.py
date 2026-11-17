hockey_players = {
    "Manpreet Singh",
    "Harmanpreet Singh",
    "PR Sreejesh",
    "Hardik Singh",
    "Mandeep Singh",
    "Amit Rohidas",
    "Abhishek",
    "Dilpreet Singh"
}

football_players = {
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Neymar",
    "Kylian Mbappe",
    "Erling Haaland",
    "Sunil Chhetri",
    "Manpreet Singh",
    "Hardik Singh"
}

cricket_players = {
    "Virat Kohli",
    "Rohit Sharma",
    "MS Dhoni",
    "Sachin Tendulkar",
    "Jasprit Bumrah",
    "Hardik Pandya",
    "Ravindra Jadeja",
    "Shubman Gill",
    "KL Rahul",
    "Suryakumar Yadav",
    "Babar Azam",
    "Kane Williamson",
    "Joe Root",
    "Ben Stokes",
    "Steve Smith"
}

print(cricket_players)

#find the players who play both hockey and football
s1=hockey_players & football_players 
print(s1)
#get the player who play only football
s1=hockey_players - football_players 
print(s1)
#find the total number of players
s1=hockey_players |  football_players 
print(len(s1))
#find the number of players that play only 1 game.
s1=hockey_players - football_players | football_players-hockey_players
print(len(s1))
