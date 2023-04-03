import customtkinter

win = customtkinter.CTk()
win.title("Эксперимент")
win.geometry("500x500")

lab = customtkinter.CTkLabel(win, text="Впиши скорость в киллометрах \nв секунду и узнай время пути до плутона",
                             font=("Arial Bold", 24))
lab.place(relx=0.02, rely=0.10)

entr = customtkinter.CTkEntry(win, width=200)
entr.place(relx=0.30, rely=0.30)

btn = customtkinter.CTkButton(win, text="Обработать")
btn.place(relx=0.35, rely=0.40)


win.mainloop()