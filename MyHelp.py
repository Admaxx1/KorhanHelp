from tkinter import *

FONT = ('Arial',30)

def KCODE():
    pass

def ShowAPISETTINGS():



    entry1 = Entry(wn,font=FONT)
    entry2 = Entry(wn,font=FONT)
    LabelApi = Label(wn,text='Enter API: ',font=FONT)
    LabelSecret = Label(wn, text = 'Secret: ',font=FONT)
    buttonSubmit = Button(wn, font=FONT,text='SUBIMT',command=KCODE)
    entry1.delete(0,END)
    entry2.delete(0,END)


    
    
    def showDropDownMenu1():

        
        
        def hideIT():
            entry1.place_forget()
            entry2.place_forget()
            LabelApi.place_forget()
            LabelSecret.place_forget()

            buttonSubmit.place_forget()
            buttonAPIsettings.config(command=showDropDownMenu1)

        buttonAPIsettings.config(command=hideIT)
         
        entry1.place(x = 360, y= 290)
        entry2.place(x = 360, y= 350)
        LabelApi.place(x= 200, y=290)
        LabelSecret.place(x= 200,y=350)
        buttonSubmit.place(x=360,y =410)

    def HIDEAPISETTINGS():
        buttonSettings.config(command=ShowAPISETTINGS)

        
        entry1.place_forget()
        entry2.place_forget()
        buttonAPIsettings.place_forget()
        buttonSubmit.place_forget()
        LabelApi.place_forget()
        LabelSecret.place_forget()

    buttonSettings.config(command=HIDEAPISETTINGS)

    buttonAPIsettings = Button(wn,text='API Settings',font=FONT,command=showDropDownMenu1)
    buttonAPIsettings.place(x=360,y=230)
    
wn = Tk()
wn.geometry('1000x700')
wn.config(bg='white')
frame = Frame(wn)
frame.pack()
framePlace = Frame(wn)
framePlace.pack()


myImage = PhotoImage(file='/Users/uptri/Desktop/PYTHON/CryptoGuessing game/KorhanHelp/settings.png')
buttonSettings = Button(wn,image=myImage,command=ShowAPISETTINGS,borderwidth=0)
buttonSettings.place(x=965,y=0)

wn.mainloop()