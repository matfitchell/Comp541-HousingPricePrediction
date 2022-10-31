import json

cities = ['baltimore','chicago', 'dallas','new_york','portland','tampa']

houses = []

for cities in cities :

    for pageNumber in range(1,21):
        print('printing city : %s _ page number : %s' %(cities,pageNumber))
        filename = './new_JSON_read_files/%s_json_file_pg_%s.json' %(cities,pageNumber)

        with open(filename, 'r') as f:
            ppfile = json.load(f)
            pageList = ppfile['cat1']['searchResults']['listResults']
            for house in pageList :
                houses.append(house)

with open('./new_JSON_read_files/json_dump.json', 'w') as f:
    print(json.dumps(houses), file=f)