from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
eng_to_fr = {}
this_word = None

def import_words():
    try:
        dictionary_file_df = pandas.DataFrame(pandas.read_csv("data/words_to_learn.csv"))
    except FileNotFoundError:
        dictionary_file_df = pandas.DataFrame(pandas.read_csv("data/french_words.csv"))
    eng_to_fr = dictionary_file_df.to_dict(orient="records")#{french.French:french.English for (_, french) in dictionary_file_df.iterrows()}
    return eng_to_fr

def pick_word(word_dict=import_words()):
    global this_word
    picked_word = choice(word_dict)
    this_word = picked_word
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(current_word, text=picked_word["French"], fill="black")
    canvas.itemconfig(image, image=card_front_image)
    window.after(4000, flip_card)

def flip_card():
    
    canvas.itemconfig(current_word, text=this_word["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(image, image=card_back_image)

def is_known():
    global this_word
    eng_to_fr.remove(this_word)
    data = pandas.DataFrame(eng_to_fr)
    data.tocsv("data/words_to_learn.csv", index=False)
    pick_word()
    

if __name__ == "__main__":
    import_words()
    
    window = Tk()
    window.title("Flashcards for French")
    window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
    
    canvas = Canvas(width=800, height=526)
    card_front_image = PhotoImage(file="images/card_front.png")
    image = canvas.create_image(400, 263, image=card_front_image)
    title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
    current_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)
    
    cross_image = PhotoImage(file="images/wrong.png")
    unknown_button = Button(image=cross_image, command=pick_word)
    unknown_button.grid(row=1, column=0)
    
    check_image = PhotoImage(file="images/right.png")
    known_button = Button(image=check_image, command=is_known)
    known_button.grid(row=1, column=1)
    
    card_back_image = PhotoImage(file="images/card_back.png")
    
    
    pick_word()    
    # card_back_image = PhotoImage(file="images/card_back.png")
    
    # my_image = PhotoImage(file="path/to/image_file.png")
    # button = Button(image=my_image, highlightthickness=0)
    
    window.mainloop()