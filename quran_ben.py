from distutils.sysconfig import customize_compiler
from tkinter import *
from tkinter.ttk import *
import requests
from tkinter.scrolledtext import *
import random
from customtkinter import *
set_appearance_mode("Dark")

root = CTk()
root.title("Quran")
root.geometry('800x700')

frame1 = CTkFrame(root, padx = 5, pady = 5, corner_radius=20, width =600)
frame1.place(relx = 0, rely = 0.1, relheight = 0.65, relwidth = 1)

instruc = Label(root, text = "Click to get a random Bangla translation of a ruku")
instruc.place(relx = 0.25, rely = 0.85)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

txt = Text(frame1, wrap=WORD) # wrap=CHAR, wrap=NONE
txt.pack(expand=1, fill=BOTH,padx=5)

txt.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)


def get_ruku():
    txt.delete('1.0', END)
    ruku = random.randint(1,557)
    
    url = f"http://api.alquran.cloud/v1/ruku/{ruku}/bn.bengali"
    r = requests.get(url)
    
    output = r.json()


    ayahs = output["data"]["ayahs"]

    surah_name = output["data"]["ayahs"][0]["surah"]["englishName"]
    txt.insert(END, f"  Surah Name :{surah_name}\n")
    ruku_num = ruku
    txt.insert(END, f"  Ruku number :{ruku_num}\n")
    for i in range(0,len(ayahs)):
        current_ayah = output["data"]["ayahs"][i]["text"]
        ayah_no = output["data"]["ayahs"][i]["number"]
        txt.insert(END, f"{ayah_no}. {current_ayah}\n")

        

b1 = CTkButton(root, text = "Get ruku", corner_radius=8, fg_color=("lightblue"), text_font =("Railway", 13), command = get_ruku)
b1.place(relx= 0.4, rely= 0.9)

root.mainloop()
