import urllib.parse as urlparse
from urllib.parse import urlencode
import http.client
import time

for pageNumber in range(1,21):
    print('printing page number : %s' %pageNumber)
    filename = './new_JSON_read_files/json_file_pg_%s.json' %pageNumber
    #LA 
    queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"Los Angeles, CA","mapBounds":{"west":-119.44444734375,"east":-113.01744539062501,"south":32.757531675134366,"north":35.104452906128245},"regionSelection":[{"regionId":12447,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":8}

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
