fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")
    
try:
    make_pie(4)
except IndexError as e:
    print(e)
    print("That is not a correct index.")
    print("Fruit pie")