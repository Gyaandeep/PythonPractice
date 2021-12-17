class Point:

    def __init__(self,x,y):
        print("Constructor is called")
        self.x = x
        self.y = y

    def falls_in_rectangle(self,lowleft,upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def falls_in_rectangle2(self,rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False



    def distance_from_point(self,a,b):
        distance = ((self.x-a)**2 + (self.y-b)**2)**0.5
        return distance

    def distance_from_point2(self,obj):
          distance = ((self.x-obj.x)**2 + (self.y-obj.y)**2)**0.5
          print(distance)


class Rectangle:
    
    def __init__(self,lowleft,upright):
        self.lowleft = lowleft
        self.upright = upright


point1 = Point(4,6)
reclow = Point(1,2)
recup = Point(11,12)

rectangle1 = Rectangle(reclow,recup)
print(rectangle1.lowleft.x)
print(rectangle1.upright.x)
print(point1.falls_in_rectangle2(rectangle1))









#3 Calculating distance between two points using both object. 
#point1 = Point(4,5)
#point2 = Point(6,7)
#point1.distance_from_point2(point2)
#point2.distance_from_point2(point2)
# Here we are calculating using function
# *** Can we calculate distance between two points object by simply point1 - point2
# Refer this above in future.




#2 Example 2 to test distance calculation using indivisual two points
#2 Here we are creating a point object and passing indivisual two cordinates
#2 Why we are not creating a two points and calculate the distance between them.  
# point1 = Point(4,5)
# print(point1.distance_from_point(8,9))
# point2 = Point(7,8)
# print(point2.distance_from_point(7,8))




#1 Trying to understand object working   

#1 point1 = Point(5,6)
#1 point2 = (Point(5,6).y)
#1 print(type(point1))
#1 print((point1))
#1 print(type(point2))
#1 num1 = int(2)
#1 print(type(num1))