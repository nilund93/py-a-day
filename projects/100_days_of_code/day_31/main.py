from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
eng_to_fr = {}

def import_words():
    dictionary_file_df = pandas.DataFrame(pandas.read_csv("data/french_words.csv"))
    eng_to_fr = {french.French:french.English for (_, french) in dictionary_file_df.iterrows()}
    print(eng_to_fr)

if __name__ == "__main__":
    import_words()
    
    window = Tk()
    window.title("Flashcards for French")
    window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
    
    canvas = Canvas(width=800, height=526)
    card_front_image = PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=card_front_image)
    canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
    canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)
    
    cross_image = PhotoImage(file="images/wrong.png")
    unknown_button = Button(image=cross_image)
    unknown_button.grid(row=1, column=0)
    
    check_image = PhotoImage(file="images/right.png")
    known_button = Button(image=check_image)
    known_button.grid(row=1, column=1)
    
    
    # card_back_image = PhotoImage(file="images/card_back.png")
    
    # my_image = PhotoImage(file="path/to/image_file.png")
    # button = Button(image=my_image, highlightthickness=0)
    
    window.mainloop()