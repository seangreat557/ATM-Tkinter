# ATM
# ver_0.3.2

# LOGS #
#Hapus Password saat sudah masuk

# ver_0.4.0

# in progress - adjusting fullscreen windows for expected 16:9 ratio screen.

#ver_0.5.0
# Hapus Password saat sudah masuk
# Membuat UI untuk Setor Tunai
# Tarik sama Setor Tunai sudah berfungsi

#ver_0.6.0
# Password dalam bentuk bintang
# Ditambah Jam dibawah
# Layout dioptimize untuk fullscreen
# Implementasi Transfer Antar Akun

# ver_0.6.5
# Fixed The layout for Fauzans Menu

# ver_0.7.0
# fix the clock: import time --> import datetime
# Change logo to ITB logo

import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
from time import gmtime, strftime
import datetime

LARGEFONT =("Verdana", 45, 'bold')

Total_Saldo = 100000
Total_Saldo2 = 100000
Total_Saldo3 = 100000
Total_Saldo4 = 100000
Total_Saldo5 = 100000
  
class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
         
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Uang':tk.IntVar()}
        self.shared_data2 = {'Uang2':tk.IntVar()}
        self.shared_data3 = {'Uang3':tk.IntVar()}
        self.shared_data4 = {'Uang4':tk.IntVar()}
        self.shared_data5 = {'Uang5':tk.IntVar()}
         
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        self.frames = {}  
  
        for F in (Start, Main, Page1, Page2, Page3, Transfer, Main2, Page12, Page22, Page32, Transfer2,
                  Main3, Page13, Page23, Page33, Transfer3, Main4, Page14, Page24, Page34, Transfer4,
                  Main5, Page15, Page25, Page35, Transfer5):
  
            frame = F(container, self)
  
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Start)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
  
class Start(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        self.controller.title('ATM')
        self.controller.state('zoomed')

        # Add The ITB Logo Here
        self.controller.iconphoto(False,tk.PhotoImage(file=''))

        label = ttk.Label(self, text="ATM", font = ('Verdana',60,'bold'), 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 1, padx = 450, pady = 10)

        Space = ttk.Label(self, text='', background='blue')
        Space.grid(row =0, column = 0, padx = 45, pady = 100)

        label2 = ttk.Label(self, text="Masukkan PIN Anda", 
                            font= ('Verdana',40), foreground = 'white', background = 'blue')
        label2.grid(row = 1, column = 1, padx = 10, pady =20)
        
        # my_username = tk.StringVar()
        # Username = tk.Entry(self, textvariable = my_username, font=('Verdana',12), width = 30, background= 'white')
        # Username.focus_set()
        # Username.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        my_pass = tk.StringVar()
        password = tk.Entry(self, textvariable=my_pass, font=('Verdana',18), width = 30, background= 'white')
        password.grid(row = 3, column = 1, padx = 10, pady = 1)

        def handle_focus_in(_):
            password.configure(fg='black',show='*')
            
        password.bind('<FocusIn>',handle_focus_in)

        def check():
            if my_pass.get() == '123':
                my_pass.set('')
                Wrong['text'] = ''
                controller.show_frame(Main)
            elif my_pass.get() == '234':
                my_pass.set('')
                Wrong['text'] = ''
                controller.show_frame(Main2)
            elif my_pass.get() == '345':
                my_pass.set('')
                Wrong['text'] = ''
                controller.show_frame(Main3)
            elif my_pass.get() == '456':
                my_pass.set('')
                Wrong['text'] = ''
                controller.show_frame(Main4)
            elif my_pass.get() == '567':
                my_pass.set('')
                Wrong['text'] = ''
                controller.show_frame(Main5)
            else:
                my_pass.set('')
                Wrong['text'] = "PIN Anda Tidak Valid"
         
        button1 = ttk.Button(self,text = "Confirm", width=10,
        command = lambda : check())
        button1.grid(row = 4, column = 1, padx = 10, pady = 30)

        Wrong = ttk.Label(self, text= "", foreground = 'red', background = 'blue')
        Wrong.grid(row = 5, column = 1 , padx = 10, pady = 10)

        def tick():
            current_time = datetime.datetime.now()
            A = current_time.strftime("%Y-%m-%d %H:%M:%S")
            time_label.config(text=A)
            time_label.after(10,tick)
            
        time_label = ttk.Label(font=('Verdana',20), foreground='black')
        time_label.pack( padx = 10, pady = 10)

        tick()
       

class Main(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent,bg='Blue')
         
        label = ttk.Label(self, text ="Halo Sean", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 2, padx = 10, pady = 10) 

        Space = ttk.Label(self, text = "", background = 'blue')
        Space.grid(row = 0, column = 1, padx = 225, pady = 80)
  
        button1 = ttk.Button(self, text ="Cek Saldo", 
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 150, pady = 100)
  

        button2 = ttk.Button(self, text ="Tarik Tunai",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Setor Tunai",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 1, column = 3, padx = 150, pady = 10)

        button4 = ttk.Button(self, text ="Log Out",
        command = lambda : controller.show_frame(Start))
        button4.grid(row = 3, column = 2,  pady = 20)

        button5 = ttk.Button(self, text = 'Transfer', command = lambda : controller.show_frame(Transfer))
        button5.grid(row = 2, column = 3,  padx= 150 ,pady = 10)

  
        
  
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent,bg='blue')
        label = ttk.Label(self, text ="Saldo", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 4, padx = 10, pady = 10)


        Space = ttk.Label(self, text="", background = 'blue')
        Space.grid(row=0, column= 0, padx = 250, pady = 100)

        global Total_Saldo
        controller.shared_data['Uang'].set(Total_Saldo)

        Saldo = ttk.Label(self, textvariable= controller.shared_data['Uang'], font = LARGEFONT,
                          foreground= 'white', background= 'blue')
        Saldo.grid(row = 1, column = 4, padx = 10, pady = 1)
  
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main))
        button1.grid(row = 3, column = 4, padx = 10, pady = 100)
  
  
class Page2(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='blue')
        label = ttk.Label(self, text ="Masukkan jumlah yang mau ditarik", font = ('Verdana', 35), 
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        def Tarik_Tunai():
            if int(Uang_Masuk.get()) > 0 and int(Uang_Masuk.get()) <= 100000000:
                global Total_Saldo
                if int(Uang_Masuk.get()) <= Total_Saldo:
                    Total_Saldo -= int(Uang_Masuk.get())
                    controller.shared_data['Uang'].set(Total_Saldo)
                    Uang_Masuk.set('')
                    controller.show_frame(Main)
                    Positif['text'] = ''
                else:
                    Positif['text'] = 'Saldo Anda Tidak Cukup'
            elif int(Uang_Masuk.get()) > 100000000:
                Positif['text'] = 'Jumlah Tarikan Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Tarikan Harus Berupa Angka Positif'



        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)
     
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        button2 = ttk.Button(self, text="Tarik",
                             command = lambda : Tarik_Tunai())
        button2.grid(row=3,column = 3, padx = 10, pady = 40)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

        Uang_Masuk = tk.StringVar()
        Tunai = ttk.Entry(self, textvariable = Uang_Masuk, font=('Verdana',18), width = 30, background = 'white')
        Tunai.grid(row=2, column = 3, padx = 10, pady=30)


class Page3(tk.Frame):
     def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent,bg='blue')
        label = ttk.Label(self, text ="Masukkan Jumlah yang mau disetor", font = ('Verdana', 35),
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)

        def Setor_Tunai():
            if int(Setor_Saldo.get()) > 0 and int(Setor_Saldo.get()) <= 100000000:
                global Total_Saldo
                Total_Saldo += int(Setor_Saldo.get())
                controller.shared_data['Uang'].set(Total_Saldo)
                Setor_Saldo.set('')
                controller.show_frame(Main)
                Positif['text'] = ''
            elif int(Setor_Saldo.get()) > 100000000:
                Positif['text'] = 'Jumlah Setoran Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Setoran Harus Berupa Angka Positif'

        Setor_Saldo = tk.StringVar()
        Setor = ttk.Entry(self, textvariable=Setor_Saldo, width= 30, font=('Verdana', 18), background='white')
        Setor.grid(row =2, column =3, padx= 10, pady=30)

        button2 = ttk.Button(self, text ="Setor",
                            command = lambda : Setor_Tunai())
        button2.grid(row = 3, column = 3, padx = 10, pady = 40)

        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

class Transfer(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        Title = ttk.Label(self, text= 'Masukkan nomor rekening',
                           font= ('Verdana', 35), foreground = 'white', background= 'blue' )
        Title.grid(row = 1, column = 1, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=160, pady=80)

        Back = ttk.Button(self, text = 'Back' , command = lambda : controller.show_frame(Main))
        Back.grid(row = 5, column = 1, padx = 10, pady = 10)

        def transfer():
            if No_rekening.get() == '276':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo
                    if int(Jumlah_Transfer.get()) > Total_Saldo:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo2
                        Total_Saldo -= int(Jumlah_Transfer.get())
                        Total_Saldo2 += int(Jumlah_Transfer.get())
                        controller.shared_data['Uang'].set(Total_Saldo)
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main)
            elif No_rekening.get() == '282':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo3
                    if int(Jumlah_Transfer.get()) > Total_Saldo:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo -= int(Jumlah_Transfer.get())
                        Total_Saldo3 += int(Jumlah_Transfer.get())
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        controller.shared_data['Uang'].set(Total_Saldo)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main)
            elif No_rekening.get() == '316':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo4
                    if int(Jumlah_Transfer.get()) > Total_Saldo:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo -= int(Jumlah_Transfer.get())
                        Total_Saldo4 += int(Jumlah_Transfer.get())
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        controller.shared_data['Uang'].set(Total_Saldo)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main)
            elif No_rekening.get() == '351':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo5
                    if int(Jumlah_Transfer.get()) > Total_Saldo:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo -= int(Jumlah_Transfer.get())
                        Total_Saldo5 += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data['Uang'].set(Total_Saldo)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main)
            else:
                Wrong['text'] = 'Nomor Rekening yang Dimasukkin Tidak Valid'


        No_rekening = tk.StringVar()
        Rekening = ttk.Entry(self, textvariable= No_rekening, font=('Verdana',18), width = 30, background = 'white')
        Rekening.grid(row= 2, column = 1, padx = 10, pady = 30)

        Jumlah_Transfer = tk.StringVar()
        Nominal = ttk.Entry(self, textvariable= Jumlah_Transfer, font=('Verdana',18), width = 30, background = 'white')
        Nominal.grid(row= 3, column = 1, padx = 10,)

        Aktif = ttk.Button(self, text = 'Transfer' , command = lambda : transfer())
        Aktif.grid(row = 4, column = 1, padx = 10, pady = 30)

        Wrong = tk.Label(self, text = '', foreground= 'red', background = 'blue')
        Wrong.grid(row = 6, column= 1, pady =10)

class Main2(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Halo Fauzan", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 2, padx = 10, pady = 10) 

        Space = ttk.Label(self, text = "", background = 'blue')
        Space.grid(row = 0, column = 1, padx = 210, pady = 80)
  
        button1 = ttk.Button(self, text ="Cek Saldo", 
        command = lambda : controller.show_frame(Page12))
        button1.grid(row = 1, column = 1, padx = 150, pady = 100)
  

        button2 = ttk.Button(self, text ="Tarik Tunai",
        command = lambda : controller.show_frame(Page22))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Setor Tunai",
        command = lambda : controller.show_frame(Page32))
        button3.grid(row = 1, column = 3, padx = 150, pady = 10)

        button4 = ttk.Button(self, text ="Log Out",
        command = lambda : controller.show_frame(Start))
        button4.grid(row = 3, column = 2,  pady = 20)

        button5 = ttk.Button(self, text = 'Transfer', command = lambda : controller.show_frame(Transfer2))
        button5.grid(row = 2, column = 3,  padx= 150 ,pady = 10)

class Page12(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Saldo", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 4, padx = 10, pady = 10)


        Space = ttk.Label(self, text="", background = 'blue')
        Space.grid(row=0, column= 0, padx = 250, pady = 100)

        global Total_Saldo2
        controller.shared_data2['Uang2'].set(Total_Saldo2)

        Saldo2 = ttk.Label(self, textvariable= controller.shared_data2['Uang2'], font = LARGEFONT,
                          foreground= 'white', background= 'blue')
        Saldo2.grid(row = 2, column = 4, padx = 10, pady = 1)
  
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main2))
        button1.grid(row = 3, column = 4, padx = 10, pady = 100)

class Page22(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan jumlah yang mau ditarik", font = ('Verdana', 35), 
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        def Tarik_Tunai():
            if int(Uang_Masuk.get()) > 0 and int(Uang_Masuk.get()) <= 100000000:
                global Total_Saldo2
                if int(Uang_Masuk.get()) <= Total_Saldo2:
                    Total_Saldo2 -= int(Uang_Masuk.get())
                    controller.shared_data2['Uang2'].set(Total_Saldo2)
                    Uang_Masuk.set('')
                    controller.show_frame(Main2)
                    Positif['text'] = ''
                else:
                    Positif['text'] = 'Saldo Anda Tidak Cukup'
            elif int(Uang_Masuk.get()) > 100000000:
                Positif['text'] = 'Jumlah Tarikan Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Tarikan Harus Berupa Angka Positif'

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)
     
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main2))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        button2 = ttk.Button(self, text="Tarik",
                             command = lambda : Tarik_Tunai())
        button2.grid(row=3,column = 3, padx = 10, pady = 40)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

        Uang_Masuk = tk.StringVar()
        Tunai = ttk.Entry(self, textvariable = Uang_Masuk, font=('Verdana',18), width = 30, background = 'white')
        Tunai.grid(row=2, column = 3, padx = 10, pady=30)

class Page32(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan Jumlah yang mau disetor", font = ('Verdana', 35),
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)

        def Setor_Tunai():
            if int(Setor_Saldo.get()) > 0 and int(Setor_Saldo.get()) <= 100000000:
                global Total_Saldo2
                Total_Saldo2 += int(Setor_Saldo.get())
                controller.shared_data2['Uang2'].set(Total_Saldo2)
                Setor_Saldo.set('')
                controller.show_frame(Main2)
                Positif['text'] = ''
            elif int(Setor_Saldo.get()) > 100000000:
                Positif['text'] = 'Jumlah Setoran Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Setoran Harus Berupa Angka Positif'

        Setor_Saldo = tk.StringVar()
        Setor = ttk.Entry(self, textvariable=Setor_Saldo, width= 30, font=('Verdana', 18), background='white')
        Setor.grid(row =2, column =3, padx= 10, pady=30)

        button2 = ttk.Button(self, text ="Setor",
                            command = lambda : Setor_Tunai())
        button2.grid(row = 3, column = 3, padx = 10, pady = 40)

        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main2))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

class Transfer2(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        Title = ttk.Label(self, text= 'Masukkan nomor rekening',
                           font= ('Verdana', 35), foreground = 'white', background= 'blue' )
        Title.grid(row = 1, column = 1, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=160, pady=80)

        Back = ttk.Button(self, text = 'Back' , command = lambda : controller.show_frame(Main2))
        Back.grid(row = 5, column = 1, padx = 10, pady = 10)

        def transfer():
            if No_rekening.get() == '275':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo2
                    if int(Jumlah_Transfer.get()) > Total_Saldo2:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo
                        Total_Saldo2 -= int(Jumlah_Transfer.get())
                        Total_Saldo += int(Jumlah_Transfer.get())
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        controller.shared_data['Uang'].set(Total_Saldo)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main2)
            elif No_rekening.get() == '282':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo3
                    if int(Jumlah_Transfer.get()) > Total_Saldo2:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo2 -= int(Jumlah_Transfer.get())
                        Total_Saldo3 += int(Jumlah_Transfer.get())
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main2)
            elif No_rekening.get() == '316':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo4
                    if int(Jumlah_Transfer.get()) > Total_Saldo2:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo2 -= int(Jumlah_Transfer.get())
                        Total_Saldo4 += int(Jumlah_Transfer.get())
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main2)
            elif No_rekening.get() == '351':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo5
                    if int(Jumlah_Transfer.get()) > Total_Saldo2:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo2 -= int(Jumlah_Transfer.get())
                        Total_Saldo5 += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main2)
            else:
                Wrong['text'] = 'Nomor Rekening yang Dimasukkin Tidak Valid'


        No_rekening = tk.StringVar()
        Rekening = ttk.Entry(self, textvariable= No_rekening, font=('Verdana',18), width = 30, background = 'white')
        Rekening.grid(row= 2, column = 1, padx = 10, pady = 30)

        Jumlah_Transfer = tk.StringVar()
        Nominal = ttk.Entry(self, textvariable= Jumlah_Transfer, font=('Verdana',18), width = 30, background = 'white')
        Nominal.grid(row= 3, column = 1, padx = 10,)

        Aktif = ttk.Button(self, text = 'Transfer' , command = lambda : transfer())
        Aktif.grid(row = 4, column = 1, padx = 10, pady = 30)

        Wrong = tk.Label(self, text = '', foreground= 'red', background = 'blue')
        Wrong.grid(row = 6, column= 1, pady =10)

class Main3(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Halo Haykal", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 2, padx = 10, pady = 10) 

        Space = ttk.Label(self, text = "", background = 'blue')
        Space.grid(row = 0, column = 1, padx = 225, pady = 80)
  
        button1 = ttk.Button(self, text ="Cek Saldo", 
        command = lambda : controller.show_frame(Page13))
        button1.grid(row = 1, column = 1, padx = 150, pady = 100)
  

        button2 = ttk.Button(self, text ="Tarik Tunai",
        command = lambda : controller.show_frame(Page23))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Setor Tunai",
        command = lambda : controller.show_frame(Page33))
        button3.grid(row = 1, column = 3, padx = 150, pady = 10)

        button4 = ttk.Button(self, text ="Log Out",
        command = lambda : controller.show_frame(Start))
        button4.grid(row = 3, column = 2,  pady = 20)

        button5 = ttk.Button(self, text = 'Transfer', command = lambda : controller.show_frame(Transfer3))
        button5.grid(row = 2, column = 3,  padx= 150 ,pady = 10)

class Page13(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Saldo", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 4, padx = 10, pady = 10)


        Space = ttk.Label(self, text="", background = 'blue')
        Space.grid(row=0, column= 0, padx = 250, pady = 100)

        global Total_Saldo
        controller.shared_data3['Uang3'].set(Total_Saldo3)

        Saldo = ttk.Label(self, textvariable= controller.shared_data3['Uang3'], font = LARGEFONT,
                          foreground= 'white', background= 'blue')
        Saldo.grid(row = 1, column = 4, padx = 10, pady = 1)
  
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main3))
        button1.grid(row = 3, column = 4, padx = 10, pady = 100)

class Page23(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan jumlah yang mau ditarik", font = ('Verdana', 35), 
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        def Tarik_Tunai():
            if int(Uang_Masuk.get()) > 0 and int(Uang_Masuk.get()) <= 100000000:
                global Total_Saldo3
                if int(Uang_Masuk.get()) <= Total_Saldo3:
                    Total_Saldo3 -= int(Uang_Masuk.get())
                    controller.shared_data3['Uang3'].set(Total_Saldo3)
                    Uang_Masuk.set('')
                    controller.show_frame(Main3)
                    Positif['text'] = ''
                else:
                    Positif['text'] = 'Saldo Anda Tidak Cukup'
            elif int(Uang_Masuk.get()) > 100000000:
                Positif['text'] = 'Jumlah Tarikan Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Tarikan Harus Berupa Angka Positif'

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)
     
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main3))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        button2 = ttk.Button(self, text="Tarik",
                             command = lambda : Tarik_Tunai())
        button2.grid(row=3,column = 3, padx = 10, pady = 40)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

        Uang_Masuk = tk.StringVar()
        Tunai = ttk.Entry(self, textvariable = Uang_Masuk, font=('Verdana',18), width = 30, background = 'white')
        Tunai.grid(row=2, column = 3, padx = 10, pady=30)

class Page33(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan Jumlah yang mau disetor", font = ('Verdana', 35),
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)

        def Setor_Tunai():
            if int(Setor_Saldo.get()) > 0 and int(Setor_Saldo.get()) <= 100000000:
                global Total_Saldo3
                Total_Saldo3 += int(Setor_Saldo.get())
                controller.shared_data3['Uang3'].set(Total_Saldo3)
                Setor_Saldo.set('')
                controller.show_frame(Main3)
                Positif['text'] = ''
            elif int(Setor_Saldo.get()) > 100000000:
                Positif['text'] = 'Jumlah Setoran Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Setoran Harus Berupa Angka Positif'

        Setor_Saldo = tk.StringVar()
        Setor = ttk.Entry(self, textvariable=Setor_Saldo, width= 30, font=('Verdana', 18), background='white')
        Setor.grid(row =2, column =3, padx= 10, pady=30)

        button2 = ttk.Button(self, text ="Setor",
                            command = lambda : Setor_Tunai())
        button2.grid(row = 3, column = 3, padx = 10, pady = 40)

        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main3))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

class Transfer3(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        Title = ttk.Label(self, text= 'Masukkan nomor rekening',
                           font= ('Verdana', 35), foreground = 'white', background= 'blue' )
        Title.grid(row = 1, column = 1, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=160, pady=80)

        Back = ttk.Button(self, text = 'Back' , command = lambda : controller.show_frame(Main3))
        Back.grid(row = 5, column = 1, padx = 10, pady = 10)

        def transfer():
            if No_rekening.get() == '275':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo3
                    if int(Jumlah_Transfer.get()) > Total_Saldo3:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo
                        Total_Saldo3 -= int(Jumlah_Transfer.get())
                        Total_Saldo += int(Jumlah_Transfer.get())
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        controller.shared_data['Uang'].set(Total_Saldo)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main3)
            elif No_rekening.get() == '276':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    if int(Jumlah_Transfer.get()) > Total_Saldo3:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo2
                        Total_Saldo3 -= int(Jumlah_Transfer.get())
                        Total_Saldo2 += int(Jumlah_Transfer.get())
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main3)
            elif No_rekening.get() == '316':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo4
                    if int(Jumlah_Transfer.get()) > Total_Saldo3:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo3 -= int(Jumlah_Transfer.get())
                        Total_Saldo4 += int(Jumlah_Transfer.get())
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main3)
            elif No_rekening.get() == '351':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo5
                    if int(Jumlah_Transfer.get()) > Total_Saldo3:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo3 -= int(Jumlah_Transfer.get())
                        Total_Saldo5 += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main3)
            else:
                Wrong['text'] = 'Nomor Rekening yang Dimasukkin Tidak Valid'


        No_rekening = tk.StringVar()
        Rekening = ttk.Entry(self, textvariable= No_rekening, font=('Verdana',18), width = 30, background = 'white')
        Rekening.grid(row= 2, column = 1, padx = 10, pady = 30)

        Jumlah_Transfer = tk.StringVar()
        Nominal = ttk.Entry(self, textvariable= Jumlah_Transfer, font=('Verdana',18), width = 30, background = 'white')
        Nominal.grid(row= 3, column = 1, padx = 10,)

        Aktif = ttk.Button(self, text = 'Transfer' , command = lambda : transfer())
        Aktif.grid(row = 4, column = 1, padx = 10, pady = 30)

        Wrong = tk.Label(self, text = '', foreground= 'red', background = 'blue')
        Wrong.grid(row = 6, column= 1, pady =10)

class Main4(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Halo Sulthan", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 2, padx = 10, pady = 10) 

        Space = ttk.Label(self, text = "", background = 'blue')
        Space.grid(row = 0, column = 1, padx = 200, pady = 80)
  
        button1 = ttk.Button(self, text ="Cek Saldo", 
        command = lambda : controller.show_frame(Page14))
        button1.grid(row = 1, column = 1, padx = 150, pady = 100)
  

        button2 = ttk.Button(self, text ="Tarik Tunai",
        command = lambda : controller.show_frame(Page24))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Setor Tunai",
        command = lambda : controller.show_frame(Page34))
        button3.grid(row = 1, column = 3, padx = 150, pady = 10)

        button4 = ttk.Button(self, text ="Log Out",
        command = lambda : controller.show_frame(Start))
        button4.grid(row = 3, column = 2,  pady = 20)

        button5 = ttk.Button(self, text = 'Transfer', command = lambda : controller.show_frame(Transfer4))
        button5.grid(row = 2, column = 3,  padx= 150 ,pady = 10)

class Page14(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Saldo", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        Space = ttk.Label(self, text="", background = 'blue')
        Space.grid(row=0, column= 0, padx = 250, pady = 100)

        global Total_Saldo
        controller.shared_data4['Uang4'].set(Total_Saldo4)

        Saldo = ttk.Label(self, textvariable= controller.shared_data4['Uang4'], font = LARGEFONT,
                          foreground= 'white', background= 'blue')
        Saldo.grid(row = 1, column = 4, padx = 10, pady = 1)
  
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main4))
        button1.grid(row = 3, column = 4, padx = 10, pady = 100)

class Page24(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan jumlah yang mau ditarik", font = ('Verdana', 35), 
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        def Tarik_Tunai():
            if int(Uang_Masuk.get()) > 0 and int(Uang_Masuk.get()) <= 100000000:
                global Total_Saldo4
                if int(Uang_Masuk.get()) <= Total_Saldo4:
                    Total_Saldo4 -= int(Uang_Masuk.get())
                    controller.shared_data4['Uang4'].set(Total_Saldo4)
                    Uang_Masuk.set('')
                    controller.show_frame(Main4)
                    Positif['text'] = ''
                else:
                    Positif['text'] = 'Saldo Anda Tidak Cukup'
            elif int(Uang_Masuk.get()) > 100000000:
                Positif['text'] = 'Jumlah Tarikan Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Tarikan Harus Berupa Angka Positif'

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)
     
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main4))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        button2 = ttk.Button(self, text="Tarik",
                             command = lambda : Tarik_Tunai())
        button2.grid(row=3,column = 3, padx = 10, pady = 40)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

        Uang_Masuk = tk.StringVar()
        Tunai = ttk.Entry(self, textvariable = Uang_Masuk, font=('Verdana',18), width = 30, background = 'white')
        Tunai.grid(row=2, column = 3, padx = 10, pady=30)

class Page34(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan Jumlah yang mau disetor", font = ('Verdana', 35),
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)

        def Setor_Tunai():
            if int(Setor_Saldo.get()) > 0 and int(Setor_Saldo.get()) <= 100000000:
                global Total_Saldo4
                Total_Saldo4 += int(Setor_Saldo.get())
                controller.shared_data4['Uang4'].set(Total_Saldo4)
                Setor_Saldo.set('')
                controller.show_frame(Main4)
                Positif['text'] = ''
            elif int(Setor_Saldo.get()) > 100000000:
                Positif['text'] = 'Jumlah Setoran Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Setoran Harus Berupa Angka Positif'

        Setor_Saldo = tk.StringVar()
        Setor = ttk.Entry(self, textvariable=Setor_Saldo, width= 30, font=('Verdana', 18), background='white')
        Setor.grid(row =2, column =3, padx= 10, pady=30)

        button2 = ttk.Button(self, text ="Setor",
                            command = lambda : Setor_Tunai())
        button2.grid(row = 3, column = 3, padx = 10, pady = 40)

        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main4))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

class Transfer4(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        Title = ttk.Label(self, text= 'Masukkan nomor rekening',
                           font= ('Verdana', 35), foreground = 'white', background= 'blue' )
        Title.grid(row = 1, column = 1, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=160, pady=80)

        Back = ttk.Button(self, text = 'Back' , command = lambda : controller.show_frame(Main4))
        Back.grid(row = 5, column = 1, padx = 10, pady = 10)

        def transfer():
            if No_rekening.get() == '275':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo4
                    if int(Jumlah_Transfer.get()) > Total_Saldo4:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo
                        Total_Saldo4 -= int(Jumlah_Transfer.get())
                        Total_Saldo += int(Jumlah_Transfer.get())
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        controller.shared_data['Uang'].set(Total_Saldo)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main4)
            elif No_rekening.get() == '276':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    if int(Jumlah_Transfer.get()) > Total_Saldo4:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo2
                        Total_Saldo4 -= int(Jumlah_Transfer.get())
                        Total_Saldo2 += int(Jumlah_Transfer.get())
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main4)
            elif No_rekening.get() == '282':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    if int(Jumlah_Transfer.get()) > Total_Saldo4:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo3
                        Total_Saldo4 -= int(Jumlah_Transfer.get())
                        Total_Saldo3 += int(Jumlah_Transfer.get())
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main4)
            elif No_rekening.get() == '351':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo5
                    if int(Jumlah_Transfer.get()) > Total_Saldo4:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        Total_Saldo4 -= int(Jumlah_Transfer.get())
                        Total_Saldo5 += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main4)
            else:
                Wrong['text'] = 'Nomor Rekening yang Dimasukkin Tidak Valid'


        No_rekening = tk.StringVar()
        Rekening = ttk.Entry(self, textvariable= No_rekening, font=('Verdana',18), width = 30, background = 'white')
        Rekening.grid(row= 2, column = 1, padx = 10, pady = 30)

        Jumlah_Transfer = tk.StringVar()
        Nominal = ttk.Entry(self, textvariable= Jumlah_Transfer, font=('Verdana',18), width = 30, background = 'white')
        Nominal.grid(row= 3, column = 1, padx = 10,)

        Aktif = ttk.Button(self, text = 'Transfer' , command = lambda : transfer())
        Aktif.grid(row = 4, column = 1, padx = 10, pady = 30)

        Wrong = tk.Label(self, text = '', foreground= 'red', background = 'blue')
        Wrong.grid(row = 6, column= 1, pady =10)

class Main5(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Halo Najwan", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 2, padx = 10, pady = 10) 

        Space = ttk.Label(self, text = "", background = 'blue')
        Space.grid(row = 0, column = 1, padx = 200, pady = 80)
  
        button1 = ttk.Button(self, text ="Cek Saldo", 
        command = lambda : controller.show_frame(Page15))
        button1.grid(row = 1, column = 1, padx = 150, pady = 100)
  

        button2 = ttk.Button(self, text ="Tarik Tunai",
        command = lambda : controller.show_frame(Page25))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Setor Tunai",
        command = lambda : controller.show_frame(Page35))
        button3.grid(row = 1, column = 3, padx = 150, pady = 10)

        button4 = ttk.Button(self, text ="Log Out",
        command = lambda : controller.show_frame(Start))
        button4.grid(row = 3, column = 2,  pady = 20)

        button5 = ttk.Button(self, text = 'Transfer', command = lambda : controller.show_frame(Transfer5))
        button5.grid(row = 2, column = 3,  padx= 150 ,pady = 10)

class Page15(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Saldo", font = LARGEFONT, 
                          foreground = 'white', background= 'blue')
        label.grid(row = 0, column = 4, padx = 10, pady = 10)


        Space = ttk.Label(self, text="", background = 'blue')
        Space.grid(row=0, column= 0, padx = 250, pady = 100)

        global Total_Saldo5
        controller.shared_data5['Uang5'].set(Total_Saldo5)

        Saldo = ttk.Label(self, textvariable= controller.shared_data5['Uang5'], font = LARGEFONT,
                          foreground= 'white', background= 'blue')
        Saldo.grid(row = 1, column = 4, padx = 10, pady = 1)
  
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main5))
        button1.grid(row = 3, column = 4, padx = 10, pady = 100)

class Page25(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan jumlah yang mau ditarik", font = ('Verdana', 35), 
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        def Tarik_Tunai():
            if int(Uang_Masuk.get()) > 0 and int(Uang_Masuk.get()) <= 100000000:
                global Total_Saldo5
                if int(Uang_Masuk.get()) <= Total_Saldo5:
                    Total_Saldo5 -= int(Uang_Masuk.get())
                    controller.shared_data5['Uang5'].set(Total_Saldo5)
                    Uang_Masuk.set('')
                    controller.show_frame(Main5)
                    Positif['text'] = ''
                else:
                    Positif['text'] = 'Saldo Anda Tidak Cukup'
            elif int(Uang_Masuk.get()) > 100000000:
                Positif['text'] = 'Jumlah Tarikan Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Tarikan Harus Berupa Angka Positif'

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)
     
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main5))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        button2 = ttk.Button(self, text="Tarik",
                             command = lambda : Tarik_Tunai())
        button2.grid(row=3,column = 3, padx = 10, pady = 40)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

        Uang_Masuk = tk.StringVar()
        Tunai = ttk.Entry(self, textvariable = Uang_Masuk, font=('Verdana',18), width = 30, background = 'white')
        Tunai.grid(row=2, column = 3, padx = 10, pady=30)

class Page35(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        label = ttk.Label(self, text ="Masukkan Jumlah yang mau disetor", font = ('Verdana', 35),
                          foreground = 'white', background= 'blue')
        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=105, pady=80)

        def Setor_Tunai():
            if int(Setor_Saldo.get()) > 0 and int(Setor_Saldo.get()) <= 100000000:
                global Total_Saldo5
                Total_Saldo5 += int(Setor_Saldo.get())
                controller.shared_data5['Uang5'].set(Total_Saldo5)
                Setor_Saldo.set('')
                controller.show_frame(Main5)
                Positif['text'] = ''
            elif int(Setor_Saldo.get()) > 100000000:
                Positif['text'] = 'Jumlah Setoran Tidak Bisa Lebih dari 100 juta'
            else:
                Positif['text'] = 'Jumlah Setoran Harus Berupa Angka Positif'

        Setor_Saldo = tk.StringVar()
        Setor = ttk.Entry(self, textvariable=Setor_Saldo, width= 30, font=('Verdana', 18), background='white')
        Setor.grid(row =2, column =3, padx= 10, pady=30)

        button2 = ttk.Button(self, text ="Setor",
                            command = lambda : Setor_Tunai())
        button2.grid(row = 3, column = 3, padx = 10, pady = 40)

        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Main5))
        button1.grid(row = 4, column = 3, padx = 10, pady = 0)

        Positif = ttk.Label(self, text="", foreground = 'red', background = 'blue')
        Positif.grid(row = 5, column = 3 , padx = 10, pady = 10)

class Transfer5(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent,bg='blue')
        self.controller = controller

        Title = ttk.Label(self, text= 'Masukkan nomor rekening',
                           font= ('Verdana', 35), foreground = 'white', background= 'blue' )
        Title.grid(row = 1, column = 1, padx = 10, pady = 10)

        space = ttk.Label(self, text= "", background='blue')
        space.grid(row=1, column=0, padx=160, pady=80)

        Back = ttk.Button(self, text = 'Back' , command = lambda : controller.show_frame(Main5))
        Back.grid(row = 5, column = 1, padx = 10, pady = 10)

        def transfer():
            if No_rekening.get() == '275':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    global Total_Saldo5
                    if int(Jumlah_Transfer.get()) > Total_Saldo5:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo
                        Total_Saldo5 -= int(Jumlah_Transfer.get())
                        Total_Saldo += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data['Uang'].set(Total_Saldo)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main5)
            elif No_rekening.get() == '276':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    if int(Jumlah_Transfer.get()) > Total_Saldo5:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo2
                        Total_Saldo5 -= int(Jumlah_Transfer.get())
                        Total_Saldo2 += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data2['Uang2'].set(Total_Saldo2)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main5)
            elif No_rekening.get() == '282':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    if int(Jumlah_Transfer.get()) > Total_Saldo5:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo3
                        Total_Saldo5 -= int(Jumlah_Transfer.get())
                        Total_Saldo3 += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data3['Uang3'].set(Total_Saldo3)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main5)
            elif No_rekening.get() == '316':
                if int(Jumlah_Transfer.get()) <= 0:
                    Wrong['text'] = 'Jumlah Transfer Harus Positif'
                elif int(Jumlah_Transfer.get()) > 100000000:
                    Wrong['text'] = 'Jumlah Transfer Tidak Bisa Lebih dari 100 Juta'
                elif int(Jumlah_Transfer.get()) > 0 and int(Jumlah_Transfer.get()) <= 100000000:
                    if int(Jumlah_Transfer.get()) > Total_Saldo5:
                        Wrong['text'] = 'Saldo Anda Tidak Cukup'
                    else:
                        global Total_Saldo4
                        Total_Saldo5 -= int(Jumlah_Transfer.get())
                        Total_Saldo4 += int(Jumlah_Transfer.get())
                        controller.shared_data5['Uang5'].set(Total_Saldo5)
                        controller.shared_data4['Uang4'].set(Total_Saldo4)
                        No_rekening.set('')
                        Jumlah_Transfer.set('')
                        Wrong['text'] = ''
                        controller.show_frame(Main5)
            else:
                Wrong['text'] = 'Nomor Rekening yang Dimasukkin Tidak Valid'


        No_rekening = tk.StringVar()
        Rekening = ttk.Entry(self, textvariable= No_rekening, font=('Verdana',18), width = 30, background = 'white')
        Rekening.grid(row= 2, column = 1, padx = 10, pady = 30)

        Jumlah_Transfer = tk.StringVar()
        Nominal = ttk.Entry(self, textvariable= Jumlah_Transfer, font=('Verdana',18), width = 30, background = 'white')
        Nominal.grid(row= 3, column = 1, padx = 10,)

        Aktif = ttk.Button(self, text = 'Transfer' , command = lambda : transfer())
        Aktif.grid(row = 4, column = 1, padx = 10, pady = 30)

        Wrong = tk.Label(self, text = '', foreground= 'red', background = 'blue')
        Wrong.grid(row = 6, column= 1, pady =10)

app = tkinterApp()

app.mainloop()
