from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Word to vector GUI")
        self.pack(fill=BOTH, expand=1)
        self.kw_lab=Label(self,text="Keyword: ")
        self.kw_lab.place(x=300, y=10)
        #selfkw_lab.pack(side="top")
        
        kw_ent=Entry(self, width=30)
        kw_ent.place(x=360, y=10)
        
        sen=[]
        n=int(input('Number of sentences: '))
        for i in range (0,n):
            self.num_lab=Label(self,text=('{0}. '.format(i+1)))
            self.num_lab.place(x=40, y=40+30*i)
            sen.append(Entry(self, width = 110))
            sen[i].place(x=60, y=40+30*i)
        #self.btn = Button(self, text="New sentence", 
                                #command=lambda:self.wrt_sntnc(i,txt))
        #self.btn.place(x=370, y=40)
        #sen_txt[i]=txt
        #sen[0].config(bg="Red")
        self.conf_btn=Button(self, text="Confirm sentences",command=lambda:self.get_sen(sen,n,kw_ent))
        self.conf_btn.place(x=350,y=70+i*30)

    def get_sen(self,sen,n,kw_ent):

        sen_txt=[]
        kw=StringVar()
        kw=(kw_ent.get()).lower()
        i=0
        self.conf_lab=Label(self,text=(""))
        for j in range(0,n):
            sen_txt.append((sen[j].get().lower()))
            #sen_txt[j]=sen_txt.lower()
            
            
        for k in range(0,n):
            if(kw in sen_txt[k] or sen_txt[k]==""):
                sen[k].config(bg="White")
                
                
            else:                
                sen[k].config(bg="Pink")
                i=1
                
        print(sen_txt)
        if(i==0):
            self.conf_lab=Label(self,text=("Confirmed"))
            self.conf_lab.place(x=370, y=90+n*30)


root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()
