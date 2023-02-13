import numpy as np
import matplotlib.pyplot as matplotlib

#backLegSensorValues = np.load("data/backLegSensorValues.npy")

#frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

targetAngles = np.load("data/targetAngles.npy")

#print(backLegSensorValues)
#print(frontLegSensorValues)
print(targetAngles)

#matplotlib.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
#matplotlib.plot(frontLegSensorValues, label = "Front Leg")

matplotlib.plot(targetAngles, label = "targetAngles")

#add legend to plot
matplotlib.legend()

#show plot
matplotlib.show()