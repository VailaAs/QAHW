percent = 0.1
def bank(x,y):
    for i in range(y):
        x = x + (x+percent)
    return print(round(x))
bank(1000, 10)