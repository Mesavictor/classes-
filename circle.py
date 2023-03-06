class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius**2
        print("Area of the circle=",area)
    def perimeter(self):
        perimeter=2*3.14*self.radius
        print("perimeter of the circle=",perimeter)
radius=float(input("Enter the radius: "))
pi=Circle(radius)
pi.area()
pi.perimeter()