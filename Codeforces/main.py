from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from api import API, ContestList
from CustomeException import myexception
from Contestslot import insert_new_contest
color={"Purple":"#9932cc",'gray':'#e1d8b9',"violett":"#800080"}
def setcontest(radio,TextF,check,url,type="Gym"):
    try:
        A=API(url)
        B=ContestList(A.getdata())
        Data=B.getdata()
        Data.sort(key=lambda x:x['id'], reverse=True)
        flag=True
        for x in Data:
            x['type']=type
            if check.get()=='0':
                insert_new_contest(TextF,x)
                flag=False
            elif x['phase']!='FINISHED':
                insert_new_contest(TextF,x)
                flag=False
        if flag:
            messagebox.showinfo(title="codeforces", message="No Upcoming Events")
    except myexception as e:
        messagebox.showerror(title="Codeforces", message=e.value)

class main_frame_setting:
    def __init__(self,master):
        master.geometry("600x580+0+0")
        master.configure(background=color['gray'])
        master.resizable(False,False)

class CodeforcesUI:
    def __init__(self,master):
        main_frame_setting(master)
        self.style=ttk.Style()
        self.style.configure("TFrame", background='#e1d8b9')
        self.style.configure("TRadiobutton", background='#e1d8b9')
        self.style.configure("Header.TLabel", width=30,font=("Arial",15,"bold"),background=color['gray'])
        self.style.configure("TCheckbutton", background=color['gray'])
        self.frame1=ttk.Frame(master)
        self.frame2=ttk.Frame(master)
        self.logo=PhotoImage(file="pic.gif")
        self.frame1.pack()
        self.frame2.pack()
        ttk.Label(self.frame1,image=self.logo).pack()
        self.radio=StringVar()
        self.check=StringVar()
        ttk.Checkbutton(self.frame2,text="only upcoming Events",variable=self.check).grid(row=4,column=1,pady=5)
        self.check.set('1')
        ttk.Radiobutton(self.frame2,text="Contest",variable=self.radio,value="Contest").grid(row=5,column=1,ipadx=5)
        ttk.Radiobutton(self.frame2,text="GYM    ",variable=self.radio,value="Gym").grid(row=6,column=1,ipadx=6)
        ttk.Radiobutton(self.frame2,text="Both    ",variable=self.radio,value="Both").grid(row=7,column=1,ipadx=7)
        ttk.Button(self.frame2,text="press",command=lambda:self.action(self.radio,self.Li,self.check)).grid(row=8,column=1,pady=5)
        self.radio.set("Contest")
        ttk.Label(self.frame2,text="**********Codeforces Events**********",style="Header.TLabel").grid(row=0,column=1,columnspan=5,pady=3)
        self.Li=Text(self.frame2,height=20,width=48)
        self.Li.config(state=DISABLED)
        self.Li.grid(row=3,column=1,padx=5)
        self.scrole=ttk.Scrollbar(self.frame2,orient=VERTICAL,command=self.Li.yview)
        self.scrole.grid(row=3,column=2,sticky="ns")
        self.Li.config(yscrollcommand = self.scrole.set)
    def action(self,radio,TextF,check):
        TextF.config(state=NORMAL)
        TextF.delete(1.0, END)
        TextF.config(state=DISABLED)
        if radio.get()=="Gym":
            setcontest(radio, TextF, check, "http://codeforces.com/api/contest.list?gym=true")
        elif radio.get()=="Contest":
            setcontest(radio, TextF, check, "http://codeforces.com/api/contest.list?gym=false","Contest")
        elif radio.get()=="Both":
            messagebox.showinfo(title="Codeforces", message="This option is under construction")    

def main():
    root=Tk()
    root.title("codeforces")
    app=CodeforcesUI(root)
    root.mainloop()
    
if __name__=="__main__":
    main()
    
