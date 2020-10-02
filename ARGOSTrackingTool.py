#-----------------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2020
#-----------------------------------------------------------------------
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
lineData = lineString.split()

record_id = lineData[0]             # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[4]                 # Observation Location Class
obs_lat = lineData[6]               # Observation Latitude
obs_lon = lineData[7] 
print (f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon}W on {obs_date}")