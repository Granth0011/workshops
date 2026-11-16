seating_grid=[
    [101,102,103],
    [104,105,106],
    [107,108,109]
]
x=[seat for row in seating_grid for seat in row if seat%2==0]
print(x)