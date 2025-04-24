def list_type():
    """starts with ["","","",]"""
    phones = ["samsung", "Apple", "Huawei"]
    print(type(phones))
    print(phones) #['samsung', 'Apple', 'Huawei']
# list_type()



def tuple_type():
    """("","","",)"""
    fruits = ("Banana", "Orange", "Apricot")
    print(fruits) #('Banana', 'Orange', 'Apricot')
    print(type(fruits)) #<class 'tuple'>
# tuple_type() 


def range_type():
    """Use "range" to use it"""
    y=range(7)
    print(type(y)) #<class 'range'>
    print(y) # (0,7)
# range_type()


def dict_type():
    data = {"name":"Eleven",
            "age":18}
    print(type(data)) #<class 'dict'>
    print(data) #{'name': 'Eleven', 'age': 18}
# dict_type()



def set_type():
    fruits = {"Mango db", "Json db", "something db"}
    print(type(fruits)) #<class 'set'>
    print(fruits) #{'Mango db', 'Json db', 'something db'}
# set_type()


def frozenset_type():
    books = frozenset({"drama", "comedy", "fantastic"})
    print(type(books)) #class 'frozenset'
    print(books) #frozenset({'fantastic', 'drama', 'comedy'})
# frozenset_type()

def bytes_type():
    x = b"Hello"
    print(type(x)) #<class 'bytes'>
    print(x) # b'Hello'
# bytes_type()

def bytearray_type():
    lenghts=bytearray(5)
    print(type(lenghts)) #<class 'bytearray'>
    print(lenghts) #bytearray(b'\x00\x00\x00\x00\x00')
# bytearray_type()


def memoryview_type():
    x = memoryview(bytes(5))
    print(type(x)) #class 'memoryview'
    print(x) #<memory at 0x0000020E79726080>
# memoryview_type()

def random_number_generate():
    import random
    print(random.randrange(1,100))
# print(random_number_generate())#agar () siz memory location agar () bn random number


def string_array():
    a = "welcome world baby"
    print(a[0])
    print(len(a)) #lenght uzunligini korsatadi len18 ekan
# string_array() #index 0 dan boshlanadi

def string_looping():
    my_word = "This is a loop"
    while True:
        for x in my_word:
            print(x)
# string_looping() #


def check_string():
    something = "Har doim buxgalteriya kerak boladi"
    print("doim" in something) #True ichida mavjud
# check_string() 


def slicing_string():
    slice_word = "Bolib tasha"
    print(slice_word[2:6]) # bu yerda 0 dan boshlangani hisobiga 2 dan 5 gacha oladi 6 kirmaydi
    print(slice_word[:8]) #slice from beginning
    print(slice_word[3:]) # slice from given index to end
    print(slice_word[-9:-4]) # negative slicing orqa indexdan boshladb
# slicing_string()

def modifying_strings():
    uber = " Uber is a taxi"
    print(uber.strip()) # removed space from beginning
    
    replacing = "Google "
    print(replacing.replace("g","h"))#Goohle

    print(uber.split(" ")) # slice by space

# modifying_strings()


def changing_range_lists():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)
# print(changing_range_lists())

def inserting_items():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist.insert(0,'cucumber')#['cucumber', 'apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
    print(thislist)
# inserting_items()

def extending_list():
    """tuple dict, set, bn ketaveradi"""
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    fructo_tuple = ("Limon", "Dragon Fruit") #hammasini oldi
    fructo_set = {"giganazavr","nimadir"} #hammasini oldi
    fructo_dict = dict({"title":"something"}) #valueni oldi faqat
    thislist.extend(tropical) #merged two of them
    thislist.extend(fructo_set)
    thislist.extend(fructo_tuple)
    thislist.extend(fructo_dict)
    
    thislist.remove('giganazavr') #giganazavrni olib tashladi
    thislist.pop(1) #index da 1 ni olib tashladi
    thislist.pop() # last itemni olib tashladi
    
    del thislist[0] # index bn apple ni olib tashladi
    #del thislist # toliq listni yoqlaydi
    
    # clear()
    # thislist.clear() #clears the list not deletes it
    # print(thislist)
    
    for x in thislist:
        # print(x)
        pass 
    for i in range(len(thislist)):
        # print(i) # index larinin chiqaradi
        pass
    
    i=0
    while i<len(thislist):
        # print(thislist[i]) # indexi bn ozini birga chiqaradi
        i += 1
    
    # thislist.sort(reverse=True)
    thislist.sort(key=str.lower)
    print(thislist)
    
    
# extending_list()


def list_comprehension():
    """List comprehension is for making coding faster"""
    numbers = [1,2,3,4,5,6,7] 
    
    # With list comprehension
    # new_numbers = [number ** 2 for number in numbers] 
    
    # Without list comprehension
    new_numbers = []
    for number in numbers:
        new_numbers.append(number**2)
        
        
    print(new_numbers)

# list_comprehension()

def list_comprehension_2():
    animals = ['dog', 'cat', 'wolf', 'cow']
    
    for animal in animals:
        if animal =='cat':
            print("There is a cat",)
        else:
            print(animal)

# list_comprehension_2()

def list_copy():
    thisislist=["banana","dragon fruit","apple"]
    # mylist=thisislist.copy() #using copy()
    # mylist =list(thisislist) #using list()
    # mylist = thisislist[:] # using slicing
    print(mylist)
# list_copy()

def list_joining():
    list1 = ["cat", "dog", "wolf"]
    list2 = [1,2,3]
    # list3 = list1+list2 #joining 1
    # print(list3)
    
    # for x in list2:
        # list1.append(x)
    
    # print(list1)
    
    list1.extend(list2)
    print(list1)
    
# list_joining()



"""Tuple beginning ("",) immutable(does not have append)"""
def tuple_data():
    mytuple=("something", "what")
    # print(mytuple)
    # print(type(mytuple))
    # print(mytuple[1]) #access by index
# tuple_data()

def tuple_change():
    """convert tuple to list to change it"""
    sometuple = ("apple", "orange", "apricot") #tuple
    
    listed_tuple=list(sometuple) # changing it to list
    
    listed_tuple[0]="papaya" # adding something
    
    x=tuple(listed_tuple) # reverting it to tuple again
    print(sometuple) # same as before
    print(listed_tuple) # 0 index changed
# tuple_change()

def tuple_add():
    animals = ("dog", "wolf", "cat",)
    
    y = list(animals)
    
    y.append("impostor")
    
    thisistuple = tuple(y)
    print(thisistuple) # impostor added
# tuple_add()

def tuple_add_2():
    tuple1=("something",)
    tuple2=("somehow",)
    
    tuple1 += tuple2 #merging two of them
    
    print(tuple1)
# tuple_add_2()

def remove_from_tuple():
    animals = ("dog", "cat", "wolf",)
    list_animals = list(animals)
    
    list_animals.remove("wolf")
    
    animals=tuple(list_animals) # apply it
    
    
    # del animals # deleted
    print(animals)
    print(list_animals)
# remove_from_tuple()

def unpacking_tuple():
    smartphones = ("Samsung", "Apple", "Huawei")
    
    (Black,White,Green) = smartphones
    
    print(Black) # Samsung
    print(type(Black)) # str
    print(White)
    print(Green)
# unpacking_tuple()
def unpacking_tuple_astericks():
    """using * thing"""
    smartphones = ("Samsung", "Apple", "Huawei", "Redmi", "Xiaomi")

    # (Black,White,*Green) = smartphones
    (Black,*White,Green) = smartphones
    
    print(Black) # Samsung
    # print(type(Black)) # str
    print(White)
    print(type(Green)) # list
    print(Green)
# unpacking_tuple_astericks()

def multiply_tuples():
    fruits = ("apple", "banana", "cherry")
    mytuple = fruits * 2

    print(mytuple) # multiplies twice 2()times
# multiply_tuples()
def tuple_count():
    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

    x = thistuple.count(5) # funksiyani ichidagi 2 ta 5 ni topish

    print(x)
# tuple_count()

def tuple_index():
    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

    x = thistuple.index(8) # ichida mavjud raqamlardan qaysilarida bor bolsa pozitsiyasini korsatadi

    print(x)
# tuple_index()


