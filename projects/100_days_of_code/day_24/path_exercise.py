# reads file on desktop with absolute path
with open(r"C:\Users\nicla\Desktop\kekw.txt", mode="r", encoding="utf-8") as f:
    print(f.read())
    
# reads file in day 23-folder with relative path
with open(r"..\day_23\test.txt", mode="r", encoding="utf-8") as f:
    print(f.read())
