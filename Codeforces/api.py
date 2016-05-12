from test.test_urllib import urlopen
import json
import time
from CustomeException import myexception
def Datecovertion(Time):
    a=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(Time))
    return a
def Timeconverstion(Duration):
    hr=int(Duration/3600);
    Duration%=3600
    mn=int(Duration/60)
    sc=Duration%60
    a=str(hr)+":"+str(mn)+":"+str(sc)
    return a
class API:
    def __init__(self,url):
        self.url=url
        try:
            self.rowdata=urlopen(url)
        except:
            raise myexception("Internet connection Failed")
    def getdata(self):
        try:
            self.data=self.rowdata.read()
            self.decodeData=self.data.decode("utf-8", errors="replace")
            self.jdata=json.loads(self.decodeData)
        except:
            raise myexception("Data can't read")
        if(type(self.jdata)!=dict):raise myexception("Invalid Data")
        return self.jdata

class ContestList:
    def __init__(self,Dict,type="Gym"):
        contestlist=Dict['result']
        self.List=list()
        for x in contestlist:
            contest=dict()
            contest['type']=type
            contest['id']=x['id']
            contest['name']=x['name']
            contest['phase']=x['phase']
            contest['duration']=Timeconverstion(x['durationSeconds'])
            contest['start']="NULL"
            if 'startTimeSeconds' in x:contest['start']=Datecovertion(x['startTimeSeconds'])
            self.List.append(contest)
    def getdata(self):
        return self.List
            