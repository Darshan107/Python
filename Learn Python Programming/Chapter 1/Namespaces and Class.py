class Bikes:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
    def brake(self):
        print("Brakinggg!!!")

red_bike = Bikes('Red', 'Carbon Fiber')
blue_bike = Bikes('Blue', 'Steel Fiber')

print(red_bike.colour)              # Red
print(blue_bike.colour)             # Blue
print(red_bike.frame_material)      # Carbon Fiber
print(blue_bike.frame_material)     # Steel Fiber

red_bike.brake()                    # Brakinggg!!!
