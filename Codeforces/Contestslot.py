from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from api import API, ContestList
from CustomeException import myexception
color={"Purple":"#9932cc",'gray':'#e1d8b9',"violett":"#800080"}
class insert_new_contest:
    def __init__(self,master,D):
        self.ContestType=D['type']
        self.ContestTitle="Title: "+D['name']
        self.ContestDate="Date: "+D['start']
        self.ContestDuration="Duration: "+D['duration']
        self.ContestStatus="Status: "+D['phase']
        self.col=color['violett']
        if(D['phase']!='FINISHED'):self.col=color['Purple']
        self.Typelabel=ttk.Label(master,text=self.ContestType,width=60,padding=0,background=self.col,font=("Arial",12,'bold'))
        self.Titlelabel=ttk.Label(master,text=self.ContestTitle,width=60,background=self.col,font=("Arial",10),wraplength=300)
        self.Datelabel=ttk.Label(master,text=self.ContestDate,width=64,background=self.col,font=("Arial",8),wraplength=300)
        self.Durationlabel=ttk.Label(master,text=self.ContestDuration,width=64,background=self.col,font=("Arial",8),wraplength=300)
        self.Statuslabel=ttk.Label(master,text=self.ContestStatus,width=64,background=self.col,font=("Arial",8),wraplength=300)
        self.breaklabel=ttk.Label(master,text="",width=64,background=color['gray'])
        master.window_create('insert',window=self.Typelabel)
        master.window_create('insert', window=self.Titlelabel)
        master.window_create('insert', window=self.Datelabel)
        master.window_create('insert', window=self.Durationlabel)
        master.window_create('insert', window=self.Statuslabel)
        master.window_create('insert',window=self.breaklabel)