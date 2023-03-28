#FileNotFound
# with open("a_file") as file:
#     file.read()

# #KeyError
# a_dict = {"key": "value"}
# value = a_dict["wrong_key"]

#IndexError
#int_list = [3, 4, 5]
#print(int_list[4])

# TypeError
# text="abc"
# print(text + 5)

# try: #something that might cause an exception
# except: # do this if there WAS an exception
# else: # do this if there were no exceptions
# finally: # do this no matter what happens
a_dictionary = {"key":"value"}
try:
    file = open("a_file.txt", "r")
    print(a_dictionary["no_key"])
except FileNotFoundError as f:
    print(f)
    print("No such file found. Creating it now.")
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as e:
    print(e)
    print("adding value to that key since it was missing")    
    a_dictionary["no_key"] = "ok then"
else:
    print(file.read())
    print(a_dictionary["no_key"])
finally:
    file.close()
    raise TypeError("I made up this error.")