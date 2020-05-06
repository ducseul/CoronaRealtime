import requests, json, time, threading
from worldStatus import WorldStatus
from tkinter import *

class Initial:
    def crawling_api(self):
        response = requests.get("https://api.thevirustracker.com/free-api?global=stats")
        resp = json.loads(response.text)
        data = resp['results'][0]
        worldStatus = WorldStatus(data['total_cases'], data['total_recovered'],  data['total_deaths'], 
        data['total_new_cases_today'], data['total_new_deaths_today'], data['total_affected_countries'])
        return worldStatus

    def btnRefresh_command(self):
        data = self.crawling_api()
        self.lbl_totalCase['text'] = data.formating_Number(data.total_cases)
        self.lbl_totalRecov['text'] = data.formating_Number(data.total_recovered)
        self.lbl_totalDeaths['text'] = data.formating_Number(data.total_deaths)
        self.lbl_NewCase['text'] = data.formating_Number(data.total_new_cases_today)
        self.lbl_NewCase['text'] = data.formating_Number(data.total_new_deaths_today)
        self.lbl_time['text'] = data.updatedTime
        print("===> Refreshed".format(data.updatedTime))
        print(data.toString())
        return data
    
    def btnRefresh_command_overried(self, oldData):
        data = self.crawling_api()
        self.lbl_totalCase['text'] = data.formating_Number(data.total_cases)  + " + " + str(oldData.total_cases - data.total_cases)
        self.lbl_totalRecov['text'] = data.formating_Number(data.total_recovered) + " + " + str(oldData.total_recovered - data.total_recovered)
        self.lbl_totalDeaths['text'] = data.formating_Number(data.total_deaths)  + " + " + str(oldData.total_deaths - data.total_deaths)
        self.lbl_NewCase['text'] = data.formating_Number(data.total_new_cases_today)  + " + " + str(oldData.total_new_cases_today - data.total_new_cases_today)
        self.lbl_NewCase['text'] = data.formating_Number(data.total_new_deaths_today)  + " + " + str(oldData.total_new_deaths_today - data.total_new_deaths_today)
        self.lbl_time['text'] = data.updatedTime
        print("===> Refreshed".format(data.updatedTime))
        print(data.toString())
        return data
    
    def callBack(self):
        flag = False
        oldData = None
        while True:
            if(flag == False):
                time.sleep(30)
                oldData = self.btnRefresh_command()
                flag = True
            else: 
                oldData = self.btnRefresh_command_overried(oldData)
            time.sleep(5*60)

    def configWg(self, widget):
        widget.config(font=("Courier", 16), padx = 15, pady = 15)

    def __init__(self):
        data = self.crawling_api()
        self.root = Tk()
        self.root.title("Corona Updated Realtime!")
        self.root.geometry("850x240")
        self.root.resizable(0, 0)

        self.lbl1 = Label(self.root, text = "Total Cases")
        self.lbl1.grid(row = 0, column = 0)
        self.configWg(self.lbl1)

        self.lbl_totalCase = Label(self.root, text = data.formating_Number(data.total_cases))
        self.lbl_totalCase.grid(row = 0, column = 1)
        self.configWg(self.lbl_totalCase)

        self.lbl2 = Label(self.root, text = "Total Recovered")
        self.lbl2.grid(row = 1, column = 0)
        self.configWg(self.lbl2)

        self.lbl_totalRecov = Label(self.root, text = data.formating_Number(data.total_recovered))
        self.lbl_totalRecov.grid(row = 1, column = 1)
        self.configWg(self.lbl_totalRecov)
            
        self.lbl3 = Label(self.root, text = "Total Deaths")
        self.lbl3.grid(row = 2, column = 0)
        self.configWg(self.lbl3)

        self.lbl_totalDeaths = Label(self.root, text = data.formating_Number(data.total_deaths))
        self.lbl_totalDeaths.grid(row = 2, column = 1)
        self.configWg(self.lbl_totalDeaths)

        self.lbl4 = Label(self.root, text = "(Today) New Case")
        self.lbl4.grid(row = 0, column = 2)
        self.configWg(self.lbl4)

        self.lbl_NewCase = Label(self.root, text = data.formating_Number(data.total_new_cases_today))
        self.lbl_NewCase.grid(row = 0, column = 3)
        self.configWg(self.lbl_NewCase)

        self.lbl4 = Label(self.root, text = "(Today) New Deaths")
        self.lbl4.grid(row = 1, column = 2)
        self.configWg(self.lbl4)

        self.lbl_NewCase = Label(self.root, text = data.formating_Number(data.total_new_deaths_today))
        self.lbl_NewCase.grid(row = 1, column = 3)
        self.configWg(self.lbl_NewCase)

        self.btnRefresh = Button(self.root, text = "Refresh !", command = self.btnRefresh_command)
        self.btnRefresh.grid(row = 2, column = 2)
        self.btnRefresh.config(padx = 80, pady = 10)

        self.lbl5 = Label(self.root, text = "Last Update")
        self.lbl5.grid(row = 3, column = 0)
        self.configWg(self.lbl5)

        self.lbl_time = Label(self.root, text = data.updatedTime)
        self.lbl_time.grid(row = 3, column = 1, columnspan = 2)
        self.configWg(self.lbl_time)
        
        # while True:
        #     time.sleep(1)
        #     self.btnRefresh_command()
        t = threading.Timer(1.0, self.callBack)
        t.start()

        self.root.mainloop()
        
if __name__ == "__main__":
    app = Initial()
   