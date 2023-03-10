from simulation import SIMULATION
import sys

try:
    directOrGUI = sys.argv[1]
except:
    directOrGUI = "GUI"


simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()
print("FINISHED SIMULATION")