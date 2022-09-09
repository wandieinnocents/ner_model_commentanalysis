import tkinter as tk
# python -m spacy download en_core_web_sm
import spacy
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
import easygui

# Top level window
frame = tk.Tk()
frame.title("NER Comments Analysis , Python")
frame.geometry("700x350")


# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    doc = nlp(inp)
    # work with other
    for entity in doc.ents:
        # print(entity.text, entity.label_)
        # add message box here or dialog box
        # display single entity at a time in dialogue

        easygui.msgbox((entity.text, entity.label_), title="Click OK to View Next Entity")
        # big_list = (entity.text, entity.label_)
        # text = '\n'.join(big_list)
        # easygui.textbox(text=text)





    # lbl.config(text="Provided Input: " + str(doc))
    # display the entities
    lbl.config(text="Comment Entities: " + str(entity.text) + " : " +  str( entity.label_))


# TextBox Creation
# dimentions of the box for capturing input
inputtxt = tk.Text(frame,width=80, height=15)


inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text="Display result", command=printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()