import numpy as np
import matplotlib.pyplot as matplotlib

#backLegSensorValues = np.load("data/backLegSensorValues.npy")

#frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

#targetAngles = np.load("data/targetAngles.npy")

backLegTargetAngles = np.load("data/backTargetAngleValues.npy")
frontLegTargetAngles = np.load("data/frontTargetAngleValues.npy")

matplotlib.plot(backLegTargetAngles, label = "Back Leg", linewidth = 3)
matplotlib.plot(frontLegTargetAngles, label = "Front Leg")

#print(backLegSensorValues)
#print(frontLegSensorValues)

#matplotlib.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
#matplotlib.plot(frontLegSensorValues, label = "Front Leg")


#add legend to plot
matplotlib.legend()

#show plot
matplotlib.show()