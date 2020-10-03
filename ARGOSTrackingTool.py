#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2020
#-----------------------------------------------------------------------
#lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
#------------------------------------------------------------------------
user_date = input("Enter data to search for Sara: ")


file_object= open("./data/raw/Sara.txt", "r")

 #Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionary object
date_dict = {}
coord_dict = {}



#Print the location of sara

for lineString in line_list:
    if lineString[0] in ("#","u"): continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    if obs_lc in ("1","2","3"):
        #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_lon)

matching_keys= []
#loop through items in the dat_dict, and collect keys for matching ones
for date_item in date_dict.items():
    the_key, the_date = date_item
    if the_date == user_date:
        matching_keys.append(the_key)
        
for matching_key in matching_keys:
    obs_lat,obs_lon = coord_dict[matching_key]
    the_date = date_dict[matching_key]
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
#Iterate through all lines in the the lineList
    
    








