#Create a shape class which has a property number_of_sides
class shape:

    def __init__(self):

        def __sides__(self,NoOfSides):
            self.NoOfSides = NoOfSides
            print("Number of sides =", NoOfSides)



#Create Triangle class which inherits Shape class. Define Area of triangle

class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height


    def area(self):
        areaOfTraingle = 0.5* self.base * self.height
        print("Area of Triangle is:", areaOfTraingle)


#Create Rectangle class which inherits Shape class. Define Area of Rectangle

class rectangle(shape):
    def __init__ (self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        areaOfRectangle = self.length * self.breadth
        print("Area of rectangle is:",areaOfRectangle)


#Create Square class which inherits Rectangle class. 

class square(rectangle):
    def __init__ (self,length):
        self.length = length
        

    def area(self):
        areaOfSquare = self.length * self.length
        print("Area of square is:",areaOfSquare)

    
#Create Circle class which inherits Shape class. 

    class circle(shape):
        def __init__ (self,radius):
            self.radius = radius
       

        def area(self):
            areaOfCircle = π * self.radius * self.radius
            print("Area of circle is:",areaOfCircle)


#Define Area and perimeter of circle.
    def area(self):
        def __init__ (self,radius):
            self.radius = radius
        perimeterOfCircle = 2 * π * self.radius
        print("perimeter of circle is:", perimeterOfCircle )
