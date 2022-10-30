import json

houses = []
for pageNumber in range(1,20):
    print('printing page number : %s' %pageNumber)
    filename = './new_JSON_read_files/json_file_pg_%s.json' %pageNumber

    with open(filename, 'r') as f:
        ppfile = json.load(f)
        pageList = ppfile['cat1']['searchResults']['listResults']
        for house in pageList :
            if house['area'] != None : 
                houses.append(house)


with open('./new_JSON_read_files/json_dump.json', 'w') as f:
    print(json.dumps(houses), file=f)