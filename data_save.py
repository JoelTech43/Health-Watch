import pickle
import datetime

global Day
global DayMins
global DayPoints
global TotMins
global TotPoints
global MinsAim
global PointsAim



def save_data(Mins, Points):
    data_file_open=open("data.pickle", "rb")
    data = pickle.load(data_file_open)
    data_file_open.close()
    totMins = data["totalMins"]
    totPoints = data["totalPoints"]
    DailyMins = data["Mins"]
    DailyPoints = data["Points"]
    totMins += Mins
    totPoints += Points
    DailyMins += Mins
    DailyPoints += Points
    data["totalMins"] = totMins
    data["totalPoints"] = totPoints
    data["Mins"] = DailyMins
    data["Points"] = DailyPoints
    data_file = open("data.pickle", "wb")
    pickle.dump(data,data_file)
    data_file.close()
    data_file = open("day.pickle", "rb")
    data = pickle.load(data_file)
    data_file.close()
    Day = data["day"]


def update_aims(MinsAim, PointsAim):
    data_file_open=open("data.pickle", "rb")
    data = pickle.load(data_file_open)
    data_file_open.close()
    data["MinsAim"] = MinsAim
    data["PointsAim"] = PointsAim
    data_file = open("data.pickle", "wb")
    pickle.dump(data,data_file)
    data_file.close()

def load_Data():
    global Day
    global DayMins
    global DayPoints
    global TotMins
    global TotPoints
    global MinsAim
    global PointsAim
    data_file = open("data.pickle", "rb")
    data = pickle.load(data_file)
    data_file.close()
    DayMins = data["Mins"]
    DayPoints = data["Points"]
    TotMins = data["totalMins"]
    TotPoints = data["totalPoints"]
    MinsAim = data["MinsAim"]
    PointsAim = data["PointsAim"]
    data_file = open("day.pickle", "rb")
    data = pickle.load(data_file)
    data_file.close()
    Day = data["day"]

def manualDailyReset():
    save_data(0,0)
    data_file_open=open("data.pickle", "rb")
    data = pickle.load(data_file_open)
    data_file_open.close()
    data["Mins"] = 0
    data["Points"] = 0
    data_file = open("data.pickle", "wb")
    pickle.dump(data,data_file)
    data_file.close()
