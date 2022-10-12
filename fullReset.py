import pickle

opened = {"Mins":0,"Points":0,"totalMins":0,"totalPoints":0,"MinsAim":30,"PointsAim":25}

file = open("data.pickle", "wb")
pickle.dump(opened, file)
file.close()