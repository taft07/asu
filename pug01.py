from graph import *
penColor(0,0,255)
x=y=20
point(x,y)
penColor("blue")
brushColor("yellow")
rectangle(x + 10, y + 5, x + 100, y + 200)
penColor("cyan")
brushColor("magenta")
polygon([(10, 10), (50, 50), (10, 50), (10, 10)])
print([x, y])
x = y = 60
brushColor("red")
for i in range(5):
    circle(x, y, 20)
    x += 60

run()