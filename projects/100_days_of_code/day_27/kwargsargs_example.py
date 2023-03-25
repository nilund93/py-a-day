

def add(*args):
    """
        add takes infinite amount of arguments
    """
    # for n in args:
    #     print(n)
    
    sum_of_args = 0
    for n in args:
        sum_of_args += n
        
    print(sum_of_args)
        
def calculate(n, **kwargs):
    # creates a dictionary of keyword arguments
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


class Car:
    def __init__(self, **kw) -> None:
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
        
        
if __name__ == "__main__":
    add(4, 5, 6, 12, 43)
    add(1, 2, 3, 4)
    
    calculate(2, add=3, multiply=5)
    
    # program will crash if we dont provice make and model (UNLESS WE USE .get IN  CONSTRUCTOR)
    my_car = Car(make="Nissan", model="GT-R")
    print(my_car.model)
    print(my_car.make)
