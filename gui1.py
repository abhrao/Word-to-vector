from tkinter import *

class Window(Frame):

    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()      

    def init_window(self):

        #i=0
        self.master.title("GUI")
        txt = StringVar()
        txt=""
        self.pack(fill=BOTH, expand=1)

        self.button = Button(self, text="New sentence", 
                                command=lambda:self.create_window(txt))
        
        self.button.pack(side="top")
        
        #self.lab_txt[i].pack(side="top")
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label='Exit', command = self.client_exit)

        menu.add_cascade(label='File', menu=file)
        lab = Label(self, text=txt)
        

    def create_window(self,txt):
        t = Toplevel(self)
        t.wm_title("Enter sentence" )
        t.geometry("500x400")
        l = Label(t, text="Sentence: ")
        l.place(x=0, y=0)
        #txt = StringVar()
        sen = Entry(t, width = 70, textvariable = txt)
        sen.place(x=57, y=0)
        btn = Button(t, text="Confirm sentence", command=t.destroy)
        btn.place(x=150,y=30)
        return txt
    
    def client_exit(self):
        exit()

    def close_window():
        self.lab.place(x=0, y=0)
        t.destroy()
'''
    def wrt_sntnc():
        lab_txt=txt.get()
        #i+=1
'''        

root = Tk()
root.geometry("800x600")

app = Window(root)

root.mainloop()
