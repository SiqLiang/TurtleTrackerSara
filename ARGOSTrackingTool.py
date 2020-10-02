#-----------------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2020
#------------------------------------------------------------------------
file_object= open("./data/raw/Sara.txt", "r")
 
 #Read contents of file into a list
lineString = file_object.readline()

while lineString:
    if lineString[0] in ("#","u"): 
        # Move to the next line
        lineString = file_object.readline()
        continue
    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    
    # Move to the next line
    lineString = file_object.readline()
      
# Close the file
file_object.close()















