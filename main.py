import customtkinter


def work():
    res = int(entr.get())
    import back_end
    btt = back_end.shet(res)
    lab_2.configure(text=f"Время пути до плутона {btt} лет")


win = customtkinter.CTk()
win.title("Эксперимент")
win.geometry("500x500")

lab = customtkinter.CTkLabel(win, text="Впиши скорость в киллометрах в секунду \nи узнай время пути до плутона",
                             font=("Arial Bold", 24))
lab.place(relx=0.02, rely=0.10)

lab_2 = customtkinter.CTkLabel(win, text="", font=("Arial Bold", 15))
lab_2.place(relx=0.25, rely=0.60)

entr = customtkinter.CTkEntry(win, width=200, height=35)
entr.place(relx=0.30, rely=0.30)

btn = customtkinter.CTkButton(win, text="Обработать", command=work, font=("Arial Bold", 25))
btn.place(relx=0.34, rely=0.40)


win.mainloop()