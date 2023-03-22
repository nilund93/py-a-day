#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

names: list = []
with open("mail_merge/Input/Names/invited_names.txt", mode="r", encoding="utf-8") as f:
    names = [name.strip("\n") for name in f.readlines()] # jag är en fakking gud
print(names)

template: list = ""
with open("mail_merge/Input/Letters/starting_letter.txt", mode="r", encoding="utf-8") as f:
    template = f.readlines()
print(template)

for name in names:
    with open(f"mail_merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w", encoding="utf-8") as f:
        letter = template.copy()
        letter[0] = letter[0].replace("[name]", name)
        for line in letter:
            f.write(line)