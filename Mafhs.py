import math
x1 = float(input("First x-coordinate: "))
y1 = float(input("First y-coordinate: "))
x2 = float(input("Second x-coordinate: "))
y2 = float(input("Secondy-coordinate: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distnace between the two points is {distance}")