with open("file1.txt", "r", encoding="utf-8") as f:
    file_one = f.readlines()

with open("file2.txt", "r", encoding="utf-8") as f:
    file_two = f.readlines()
    
result = [int(number) for number in file_one if number in file_two]