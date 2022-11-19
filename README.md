# CS3500_Code
Our group assignment code for D3 in CS3500. 

The main python file is called Main.py. 
Run this to bring up the gui.
Enter the speed of your car in M/S and the program will begin running.
X out of the GUI to end the program.

 FILES INCLUDED  
 python files:
 
  road.py -- generates a random road for the program to simulate a real road
  
  sensor.py -- "scans" the road by taking in information from the road text file and writes to the sensor text file.
  
  identifier.py -- identifies impediments by reading lines from the sensor text file and writes instructions for the brakes and suspension to the identifer text file.
  
  main.py -- creates the gui and displays each impediemnt and the cahnge in brakes and suspension.
  
  stop.py -- controls a global variable that stops each program in unison.
 
 text files:
 
  road.txt -- contains the random road features. Written to by road.py and Main.py (speed of car), read by sensor.py.
  
  sensor.txt -- contains impediments on the road. Written to by sensor.py, read by identifer.py.
  
  identifer.txt -- contains impediment names and suspension and brake calculations. Written to by identifer.py, read by Main.py
 
