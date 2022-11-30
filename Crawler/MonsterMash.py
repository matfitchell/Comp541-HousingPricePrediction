#Program to compile a master list of houses from multiple JSON files into one compiled JSON file
import json

#create array of cities for file naming // file access 
cities = ['atlanta','baltimore','chicago', 'detroit','greenbay', 'dallas','lasvegas', 'new_york','portland','raleigh','richmondva','sacramento','spokane','stlouis','tampa','topeka']

#create empty array to hold houses to append to final JSON
houses = []
#iterate through every city in array
for cities in cities :
    #iterate through every page in city
    for pageNumber in range(1,21):
        #print status message
        print('printing city : %s _page number : %s' %(cities,pageNumber))
        #assign file name to current city and page number
        filename = './new_JSON_read_files/%s_json_file_pg_%s.json' %(cities,pageNumber)
        #open file
        with open(filename, 'r') as f:
            ppfile = json.load(f)
            #select to 40 house entries in JSON
            pageList = ppfile['cat1']['searchResults']['listResults']
            #append each house in list to master list
            for house in pageList :
                houses.append(house)

#write master list of houses to final JSON file
with open('./new_JSON_read_files/json_dump.json', 'w') as f:
    print(json.dumps(houses), file=f)