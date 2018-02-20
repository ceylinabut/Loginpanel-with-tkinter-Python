rom tkinter import *

giris = Tk()
giris.title("Welcome")
giris.geometry("201x250+350+150")
giris.resizable(FALSE,FALSE)
giris.config(bg="orange")

logo = PhotoImage(file="logo.gif")

logo2 = Label(giris,image=logo)
logo2.grid(column=1,row=1)
def nextt():
    main = Tk()
    main.title("Userpanel")
    main.geometry("187x75+350+150")
    main.resizable(FALSE,FALSE)
    main.config(bg="#CCFF00")

    username = Label(main,bg="yellow",fg="black",text="Username")
    username.grid(column=1,row=1)

    username2 = Entry(main)
    username2.grid(column=2,row=1)

    password = Label(main,bg="yellow",fg="black",text="Password")
    password.grid(column=1,row=2)

    password2 = Entry(main)
    password2.grid(column=2,row=2)

    def kontrol():
        if username2.get()=="Your Username":
            if password2.get()=="Your Password":
                true = Tk()
                true.title("Controlpanel")
                true.geometry("230x50+350+150")
                true.resizable(FALSE,FALSE)

                true2 = Label(true,bg="green",fg="white",text="Access_Confirmed")
                true2.pack()

                giris.destroy()
                
                main.destroy()
            else:
                false = Tk()
                false.title("Controlpanel")
                false.geometry("230x50+350+150")
                false.resizable(FALSE,FALSE)

                false2 = Label(false,bg="red",fg="white",text="Access_Denied")
                false2.pack()

                giris.destroy()
                
                main.destroy()
        else:
            false = Tk()
            false.title("Controlpanel")
            false.geometry("230x50+350+150")
            false.resizable(FALSE,FALSE)

            false2 = Label(false,bg="red",fg="white",text="Access_Denied")
            false2.pack()

            giris.destroy()
            
            main.destroy()

    onay = Button(main,bg="yellow",fg="black",text="OKEY",command=kontrol)
    onay.grid(column=2,row=3)
    
    

    

yeni = Button(giris,bg="black",fg="#9CFAFF",text="SKİP",command=nextt)
yeni.grid(column=1,row=2)


mainloop()
