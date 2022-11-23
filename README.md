# CS3500_Code
Our group assignment code for D3 in CS3500. 

The primary python file is called GUI.py. 
Run this to bring up the gui.
Enter the speed of your car in M/S and the program will begin running.
X out of the GUI to end the program.

To run test cases, simply click on each test case and run the file. if it returns back nothing the tests were successful.

 FILES INCLUDED  
 python files:
 
  road.py -- generates a random road for the program to simulate a real road
  
  sensor.py -- "scans" the road by taking in information from the road text file and writes to the sensor text file.
  
  identifier.py -- identifies impediments by reading lines from the sensor text file and writes instructions for the brakes and suspension to the identifer text file.
  
  gui.py -- creates the gui and displays each impediemnt and the cahnge in brakes and suspension.
  
  stop.py -- controls a global variable that stops each program in unison.
  
  
  roadtestcase.py -- Makes sure all paths of our CFG can be performed correctly in road.py
  
  sensortestcase.py -- Makes sure all paths of our CFG can be performed correctly in sensor.py
  
  identiifertestcase.py -- Makes sure all paths of our CFG can be performed correctly in identifier.py
  
  guitestcase.py -- Makes sure all paths of our CFG can be performed correctly in gui.py
  
 
 text files:
 
  road.txt -- contains the random road features. Written to by road.py and Main.py (speed of car), read by sensor.py.
  
  sensor.txt -- contains impediments on the road. Written to by sensor.py, read by identifer.py.
  
  identifer.txt -- contains impediment names and suspension and brake calculations. Written to by identifer.py, read by Main.py
 
