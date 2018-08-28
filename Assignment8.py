# Q.1


class Circle:

    def __init__(self, radius=0):
        self.radius = radius

    def get_area(self):
        pi = 3.14
        return pi*(self.radius*self.radius)

    def get_circumference(self):
        pi = 3.14
        return 2*pi*self.radius


r = int(input('enter the radius of the circle: '))
var = Circle(r)
print('The area of circle with radius %d is %.2f' % (r, var.get_area()))
print('The circumference of circle with radius %d is %.2f' % (r, var.get_circumference()))

# Q.2 


class Student:
    age = 0
    marks = 0

    def __init__(self, name, rno):
        self.name = name
        self.rno = rno

    def set_age(self, age=0):
        self.age = age

    def set_marks(self, marks=0):
        self.marks = marks

    def display(self):
        print('Name: {}, RollNo: {}, Age: {}, Marks: {}'.format(self.name, self.rno, self.age, self.marks))


x = input('enter the name of student: ')
y = int(input('enter the roll number of student: '))
s1 = Student(x, y)
s1.set_age(int(input('Enter the age: ')))
s1.set_marks(int(input('enter the marks: ')))
s1.display()

# Q.3

class Temperature:
    far = 0
    cel = 0

    def far_to_cel(self, far1=0):
        self.cel = far1 - 32
        self.cel *= 5
        self.cel /= 9
        return self.cel

    def cel_to_far(self, cel1=0):
        self.far = cel1 * 9
        self.far /= 5
        self.far += 32
        return self.far


test = 0
t = Temperature()
while test != 3:
    test = int(input('enter choice if you want to enter temperature in 1 for fahrenheit or 2 for Celsius or 3 to terminate program: '))
    if test == 1:
        far = int(input('enter temp in fahrenheit: '))
        print('The temperature %d F in celsius is %.2f C' % (far, t.far_to_cel(far)))
    elif test == 2:
        cel = int(input('enter the temp in celsius: '))
        print('The temperature %d C in celsius is %.2f F' % (cel, t.cel_to_far(cel)))
    elif test == 3:
        print('Program terminated')
        break
    else:
        print('Invalid Input')

# Q.4

class MovieDetails:
    Mov = list()

    def __init__(self, artName, YoR, Rat):
        self.Aname = artName
        self.RelYear = YoR
        self.ratings = Rat

    def Add(self):
        self.NewMov = {'Artist': self.Aname, 'Release Year': self.RelYear, 'Ratings': self.ratings}
        self.Mov.append(self.NewMov)

    def Display(self):
        for i in range(0, len(self.Mov)):
            print("The Artist of the Movie is {}".format(self.Mov[i]['Artist']))
            print("The Year of Release is {}".format(self.Mov[i]['Release Year']))
            print("The Ratings are {}".format(self.Mov[i]['Ratings']))


AJA = MovieDetails('ajay devgan', '1998', '5')
AJA.Add()
D1 = MovieDetails('Rithik Roshan', '2004', '4')
D1.Add()
D1.Display()


# Q.5

class Animal:
    def animal_attribute(self):
        self.Color = 'Yellow with Brown Stripes'
        self.legs = 4
        self.Endangered = 'Endangered'
        print(self.Color, self.legs, self.Endangered, sep = "\n")


class Tiger(Animal):
    def Yellow(self):
        pass


Tig = Tiger()
Tig.animal_attribute()


# Q.6

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'


class B(A):
    def g(self):
        return 'B'


a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())



# Q.7


class Shape:
    length = 0
    brdth = 0

    def GetMeas(self):
        self.length = int(input("Enter The Length Of the Shape "))
        self.brdth = int(input("Enter The Breadth of the Shape "))
        return self.length, self.brdth

    def Area(self, leng, brd):
        self.Ar = leng*brd
        print(self.Ar)


class Rectangle(Shape):
    def __init__(self):
        pass


class Square(Shape):
    def __init__(self):
        pass


Sq = Square()
Rc = Rectangle()
sh = Shape()

ln, brd = sh.GetMeas()
if ln == brd:
    Sq.Area(ln, brd)
else:
    Rc.Area(ln, brd)
