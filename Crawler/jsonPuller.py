import urllib.parse as urlparse
from urllib.parse import urlencode
import http.client
import time

for pageNumber in range(1,21):
    print('printing page number : %s' %pageNumber)

    #filename = './new_JSON_read_files/los_angeles_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/dallas_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/new_york_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/chicago_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/portland_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/tampa_json_file_pg_%s.json' %pageNumber

    filename = './new_JSON_read_files/baltimore_json_file_pg_%s.json' %pageNumber

    
    
    #LA 
    #queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"Los Angeles, CA","mapBounds":{"west":-119.44444734375,"east":-113.01744539062501,"south":32.757531675134366,"north":35.104452906128245},"regionSelection":[{"regionId":12447,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":8}

   #wants = {"cat1":["listResults","mapResults"],"cat2":["total"]}

   #Dallas
    #queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"Dallas, TX","mapBounds":{"west":-97.04728318457032,"east":-96.5075798154297,"south":32.70764142860342,"north":32.92807631002532},"regionSelection":[{"regionId":38128,"regionType":6}],"isMapVisible":True,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True,"mapZoom":11}

    #wants = {"cat1":["listResults","mapResults"],"cat2":["total"]}
    #New York
    #queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"New York, NY","mapBounds":{"west":-75.05908773828125,"east":-72.90027426171875,"south":40.29893717780191,"north":41.0943914206361},"regionSelection":[{"regionId":6181,"regionType":6}],"isMapVisible":True,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True,"mapZoom":9}

   # wants = {"cat1":["listResults","mapResults"],"cat2":["total"]}
   #Chicago
    #queryState = {"pagination":{"currentPage":2},"usersSearchTerm":"Chicago, IL","mapBounds":{"west":-88.27164536914063,"east":-87.19223863085938,"south":41.638280450652054,"north":42.029147261767314},"regionSelection":[{"regionId":17426,"regionType":6}],"isMapVisible":True,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True}

    #wants ={"cat1":["listResults","mapResults"],"cat2":["total"]}

    #Portland
    #queryState ={"pagination":{"currentPage":2},"usersSearchTerm":"Portland, OR","mapBounds":{"west":-122.919539,"east":-122.471849,"south":45.395871,"north":45.714497},"regionSelection":[{"regionId":13373,"regionType":6}],"isMapVisible":False,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True}
    #wants = {"cat1":["listResults"],"cat2":["total"]}

    #Tampa
    #queryState = {"pagination":{"currentPage":2},"usersSearchTerm":"Tampa, FL","mapBounds":{"west":-83.25765574414064,"east":-81.65090525585939,"south":27.681931008465693,"north":28.306420078252618},"regionSelection":[{"regionId":41176,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True}
    #wants = {"cat1":["listResults","mapResults"],"cat2":["total"]}

    #Baltimore
    queryState = {"pagination":{"currentPage":2},"usersSearchTerm":"Baltimore, MD","mapBounds":{"west":-77.02217362207031,"east":-76.21879837792969,"south":39.16008602472207,"north":39.43374473444153},"regionSelection":[{"regionId":3523,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":11}
    wants = {"cat1":["listResults","mapResults"],"cat2":["total"]}

    params = {'searchQueryState' : queryState, 'wants' : wants}

    toBeAppended = urlparse.urlencode(params)
    time.sleep(20)

    conn = http.client.HTTPSConnection("www.zillow.com")
    headersList = {


    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    payload = ""

    conn.request("GET", "/search/GetSearchPageState.htm?%s" % toBeAppended)
    response = conn.getresponse()
    result = response.read()

    with open(filename, 'w') as f:
        print(result.decode("utf-8"),file=f)
