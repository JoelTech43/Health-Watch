from guizero import App, Text, Slider, PushButton, TextBox, Window
import pickle
import data_save as info

def resetDaily():
    info.manualDailyReset()
    set_Message()

def show_total_score():
    info.load_Data()
    TotMins = info.TotMins
    TotPoints = info.TotPoints
    if TotalMinutes.value == "":
        TotalMinutes.value = "Total Minutes: " + str(TotMins) + "!"
        TotalPoints.value = "Total Health Points: " + str(TotPoints) + "!"
    else:
        TotalMinutes.value = ""
        TotalPoints.value = ""

def set_Message():
    info.load_Data()
    DayMins = info.DayMins
    DayPoints = info.DayPoints
    MinsAim = info.MinsAim
    PointsAim = info.PointsAim
    if DayMins >= MinsAim and DayPoints >= PointsAim:
        Welcome.value = "You have achieved your daily exercise aims!"
        Minutes_exercised.value = "Minutes worked out: " + str(DayMins) + "! Completed!"
        Health_points_gained.value = "Health points: " + str(DayPoints) + "! Completed!"
    elif DayMins >= MinsAim and DayPoints< PointsAim:
        Welcome.value = "You have achieved your daily minutes goal!"
        Minutes_exercised.value = "Minutes worked out: " + str(DayMins) + "! Completed!"
        Health_points_gained.value = "Health Points: " + str(DayPoints) + "!"
    elif DayMins < MinsAim and DayPoints >= PointsAim:
        Welcome.value = "You have achieved your daily Health Points Goal!"
        Minutes_exercised.value = "Minutes worked out: " + str(DayMins) + "!"
        Health_points_gained.value = "Health Points: " + str(DayPoints) + "! Completed!"
    else:
        Welcome.value = "Welcome to my exercise tracker"
        Minutes_exercised.value = "Minutes worked out: " + str(DayMins) + "!"
        Health_points_gained.value = "Health Points: " + str(DayPoints) + "!"

def sub_daily():
    Sub_Mins = Minutes.value
    Sub_Points = Health_points.value
    info.save_data(Sub_Mins, Sub_Points)
    set_Message()

def updateAims():
    MinAim = SetMinutes.value
    PointAim = SetPoints.value
    info.update_aims(MinAim, PointAim)
    ValuesSetter.hide()

def setValuesShow():
    ValuesSetter.show()

app = App(title="Fitness App", bg=(00,80,00), height=750, width=1000)

Welcome = Text(app, text="Welcome to my exercise tracker", size=30, font="Times New Roman", color="lime")

ValuesSetter = Window(app, title="Set Values", width=750, height=300, bg=(00,80,00))
ValuesSetter.hide()

Minutes_exercised = Text(app, text="Minutes worked out: 0", size=30, font="Times New Roman", color="gold")

Health_points_gained = Text(app, text="Health points: 0", size=30, font="Times New Roman", color="gold")

set_Message()

Show = PushButton(app, command=show_total_score, text="Show Total Scores")

TotalMinutes = Text(app, size = 30, text="", color="gold")

TotalPoints = Text(app, size = 30, text="", color="gold")

reset = PushButton(app, command=resetDaily, text="Reset Daily Values")

reset_explanation = Text(app, text="This should happen automatically at the end of each day or the start of the following day but if it doesn't, press this button!", size=15, font="Times New Roman", color = "black")

Add= Text(app, text="Add more exercise:", size=20, font="Times New Roman", color="orange")

Minutes_text = Text(app, text="Minutes:", size=15, font="Times New Roman", color="black")

Minutes = Slider(app, width = "fill", start=1, end=120)

HealthPointsText = Text(app, text="Health Points:", size=15, font="Times New Roman", color="black")

HealthPointsText = Text(app, text="Health points are how tired you were after/while completing the activity. 0 is not tired, 50 is as tired as you can be.", size=12, font="Times New Roman", color="black")

Health_points = Slider(app, width = "fill", start=0, end=50)

Submit = PushButton(app, command=sub_daily, text="Submit")

Break = Text(app, text="")

SetValuesBtn = PushButton(app, command=setValuesShow, text="Set Goals")

SetValuesText = Text(ValuesSetter, text="Set your aim for amounts of minutes and heart points daily below:", size=20, font="Times New Roman", color="black")

SetMinutesAimText = Text(ValuesSetter, text="Minutes Aim:", size=15, font="Times New Roman", color="black")

SetMinutes = Slider(ValuesSetter, width = "fill", start=30, end=120)

SetPointsAimText = Text(ValuesSetter, text="Points Aim:", size=15, font="Times New Roman", color="black")

SetPoints = Slider(ValuesSetter, width = "fill", start=15, end=100)

SubmitValuesBtn = PushButton(ValuesSetter, text="Submit", command=updateAims)

Break2 = Text(ValuesSetter, text="")

Info = Text(ValuesSetter, text = "Made for my otter - create award in the CUB supercurriculum award at KEFW.\nThank you for viewing this and showing support!", size=15, color="black", font="Times New Roman")

Break3 = Text(app, text="")

copyWrite = Text(app, text="© Joel Hayward 2022. Thanks to my teachers and friends at KEFW who made this possible!", size=13, color="black", font="Times New Roman")

app.display()


