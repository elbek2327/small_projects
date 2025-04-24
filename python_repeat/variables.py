
def slicing():
    """Slicing via arrays"""
    numbers = [1,2,3,4,5,6,7,8,9,10]
    # print(numbers[1::2]) #Output [2,4,6,8,10]
    # print(numbers[1:1])# None
    # print(numbers[1::3])#[2,5,8] 3tadan tashlab ketadi
    # print(numbers[1::4]) #4tadan otadi

# slicing()


# Variables Objectga boglangan data saqlovchilar
def types():
    x=5
    y='Sam'
    # Casting
    z=int(7)
    
    
    
    
    print(type(x))
    print(type(y))
# types()

# Single or double quotes
def sin_doub():
    x="Something" #Double quote
    x='Something' #single quote
    print(x)
# sin_doub() # Something


# Many values to multiple variables
def multiple_variables():
    x,y,z = '1-chi', '2-chi', '3-chi'
    print(x)
    print(y)
    print(z)
# multiple_variables()


def one_value_to_multiple_variables():
    x = y = z = "Hammasi (all)"
    print(x)
    print(y)
    print(z)
# one_value_to_multiple_variables()

# Unpacking collections (from tuple or whatever)
def unpacking_collections():
    animals = ["lion", "jaguar", "elephant"]
    x,y,z=animals
    print(x)
    print(y)
    print(z)
# unpacking_collections()

"""Global Variables"""

# x = "wonder full" #Global variable

def somethingfunc():
    print("Something is " +   x)
# somethingfunc()

def localvariable():
    x="Great"
    print("It is not " + x)
# localvariable()
    
X = "Global"
def globalfunc():
    global X
    # X = 'very good'
    print('very ' + X)
# globalfunc() # very Global


    