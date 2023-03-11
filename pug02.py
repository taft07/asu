from graph import *

penColor("blue")
brushColor("yellow")
rectangle(0, 0, 400, 600)
brushColor("blue")
x = y = 20  # начальное расположенин квадрата
a = 10      # сторона квадрата
square = rectangle(x, y, x + a, y + a)
def keyPressed(event):
    if event.keycode == VK_LEFT:
        move(square, x - 5, y)
    if event.keycode == VK_RIGHT:
        move(square, x + 5, y)
    if event.keycode == VK_DOWN:
        move(square, x, y + 5)
    if event.keycode == VK_UP:
        move(square, x, y - 5)
    if event.keycode == VK_ESCAPE:
        exit()
onTimer(keyPressed, 50)
penColor("blue")
brushColor("yellow")
rectangle(0, 0, 400, 600)
brushColor("blue")
square = rectangle(x, y, x + a, y + a)
print([square])
run()