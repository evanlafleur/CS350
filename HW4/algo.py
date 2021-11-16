#search a list of strings for a specific string

from tkinter import *

window = Tk()

window.title("Brute Force String Matching")
window.geometry('700x700')

lbl1 = Label(window, font = "Verdana 12 bold" , text = "Enter Phrase to search")
lbl2 = Label(window, font = "Verdana 12 bold", text = "Enter Search String")
lbl3 = Label(window, font = "Verdana 20 bold", text = "0")
phrase = Entry(window, width = 10)
string_to_search = Entry(window, width = 10)

lbl1.grid(column = 0, row = 0)
lbl2.grid(column = 1, row = 0)
phrase.grid(column = 0, row = 1)
string_to_search.grid(column = 1, row =1 )



def string_search(string, sub_str):
    for i in range(len(string) - len(sub_str) + 1):
        index = i
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
            if index-i == len(sub_str):
                return i
            return -1

def clicked():
    string = phrase.get()
    sub_str = string_to_search.get()

    res = string_search(string, sub_str)
    lbl3.configure(text = res) 

btn = Button(window, text = "MATCH", command = clicked)

btn.grid(column = 0, row = 3)

lbl3.grid(column = 0, row = 4)

window.mainloop()



