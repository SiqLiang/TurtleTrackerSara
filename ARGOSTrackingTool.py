#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2020
#-----------------------------------------------------------------------
#lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
#------------------------------------------------------------------------
user_date = input("Enter data to search for Sara[M/D/YYYY]: ")

file_object= open("./data/raw/Sara.txt", "r")

 #Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionary object
date_dict = {}
coord_dict = {}

#Iterate through all lines in the the lineList
for lineString in line_list:
    if lineString[0] in ("#","u"): continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    #if obs_lc not in ("1","2","3"):
    #    continue
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of sara if lc is 1, 2, or 3
    if obs_lc in ("1","2","3"):
        #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_lon)

#Create empty list to hold matching keys
matching_keys = []

#Loop through items in the the date_dict, and collect keys for matching ones
for date_item in date_dict.items():
    #Get the key and date of the dictionary item
    the_key, the_date = date_item
    #See if the date matches the user date
    if the_date == user_date: 
        #If so, add the key to the list
        matching_keys.append(the_key)
        
#If no records found, tell the user
if len(matching_keys) == 0:
    print(f"No observations on {user_date}; is your date format valid?")        

#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
