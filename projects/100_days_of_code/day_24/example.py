# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write mode overwrites the file
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# append mode adds to the end of the file    
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")    