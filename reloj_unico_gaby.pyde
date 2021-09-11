a = 0
b = 0
c = 0
def setup ():
    size (250, 250)
def draw():
    background(150)
    global a
    global b
    global c
    square(17, a, 50)
    if a > height:
       a = 0
    else:
       a = map(second(), 0, 59, 0, height)
    circle(125, b, 60)
    if b > height:
       b = 0
    else:
       b = map(minute(), 0, 59, 0, height)
    square(192, c, 50)
    if c > height:
       c = 0
    else:
       c = map(hour(), 0, 59, 0, height)
