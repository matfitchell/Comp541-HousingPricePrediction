import urllib.parse as urlparse
from urllib.parse import urlencode
import http.client
import time

#iterate through 20 pages per city
for pageNumber in range(1,21):
    #print status message to console
    print('printing page number : %s' %pageNumber)

    #assign a unique file name including city and page number
    #filename = './new_JSON_read_files/los_angeles_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/dallas_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/new_york_json_file_pg_%s.json' %pageNumber

    filename = './new_JSON_read_files/chicago_json_file_pg_%s.json' %pageNumber    
    
    #assign params for JSON pull request based on city
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
    queryState = {"pagination":{"currentPage":2},"usersSearchTerm":"Chicago, IL","mapBounds":{"west":-88.27164536914063,"east":-87.19223863085938,"south":41.638280450652054,"north":42.029147261767314},"regionSelection":[{"regionId":17426,"regionType":6}],"isMapVisible":True,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True}

    wants ={"cat1":["listResults","mapResults"],"cat2":["total"]}

    #insert params from individual city into boilerplate
    params = {'searchQueryState' : queryState, 'wants' : wants}
    #parse the params as acceptable URL 
    toBeAppended = urlparse.urlencode(params)
    #Cooldown so zillow doesn't kick us out
    time.sleep(20)

    #utilize thunderclient to submit the pull request
    conn = http.client.HTTPSConnection("www.zillow.com")
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }
    #we return no data
    payload = ""
    #submit connection request with our desired and parsed parameters
    conn.request("GET", "/search/GetSearchPageState.htm?%s" % toBeAppended)
    response = conn.getresponse()
    result = response.read()
    #print decoded utf-8 code to new JSON file
    with open(filename, 'w') as f:
        print(result.decode("utf-8"),file=f)
