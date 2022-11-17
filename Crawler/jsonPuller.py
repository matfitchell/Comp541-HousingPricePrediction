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

    #filename = './new_JSON_read_files/chicago_json_file_pg_%s.json' %pageNumber    
    
    #filename = './new_JSON_read_files/detroit_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/topeka_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/richmondva_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/spokane_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/lasvegas_json_file_pg_%s.json' %pageNumber

    #filename = './new_JSON_read_files/greenbay_json_file_pg_%s.json' %pageNumber

    filename = './new_JSON_read_files/stlouis_json_file_pg_%s.json' %pageNumber

    #assign params for JSON pull request based on city
    #LA 
    #queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"Los Angeles, CA","mapBounds":{"west":-119.44444734375,"east":-113.01744539062501,"south":32.757531675134366,"north":35.104452906128245},"regionSelection":[{"regionId":12447,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":8}

    #Dallas
    #queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"Dallas, TX","mapBounds":{"west":-97.04728318457032,"east":-96.5075798154297,"south":32.70764142860342,"north":32.92807631002532},"regionSelection":[{"regionId":38128,"regionType":6}],"isMapVisible":True,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True,"mapZoom":11}

    #New York
    #queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"New York, NY","mapBounds":{"west":-75.05908773828125,"east":-72.90027426171875,"south":40.29893717780191,"north":41.0943914206361},"regionSelection":[{"regionId":6181,"regionType":6}],"isMapVisible":True,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True,"mapZoom":9}

    #Chicago
    #queryState = {"pagination":{"currentPage": pageNumber},"usersSearchTerm":"Chicago, IL","mapBounds":{"west":-88.27164536914063,"east":-87.19223863085938,"south":41.638280450652054,"north":42.029147261767314},"regionSelection":[{"regionId":17426,"regionType":6}],"isMapVisible":True,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True}


    #Detroit
    #queryState = {"pagination":{"currentPage": pageNumber},"usersSearchTerm":"Detroit, MI","mapBounds":{"west":-83.30004881103517,"east":-82.89836118896486,"south":42.28742000693798,"north":42.4180853903611},"regionSelection":[{"regionId":17762,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":12}

    #Topeka
    #queryState = {"pagination":{"currentPage": pageNumber},"usersSearchTerm":"Topeka, KS","mapBounds":{"west":-96.56166524414063,"east":-94.95491475585938,"south":38.80148868204754,"north":39.35052538887739},"regionSelection":[{"regionId":41256,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True}

    #Richmond VA
    #queryState = {"pagination":{"currentPage": pageNumber},"usersSearchTerm":"Richmond, VA","mapBounds":{"west":-77.89494912207032,"east":-77.09157387792969,"south":37.384382837793154,"north":37.66483727795263},"regionSelection":[{"regionId":6752,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":11}

    #Spokane
    #queryState = {"pagination":{"currentPage": pageNumber},"usersSearchTerm":"Spokane, WA","mapBounds":{"west":-118.23666074414062,"east":-116.62991025585937,"south":47.43389612708519,"north":47.91013155265828},"regionSelection":[{"regionId":20604,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True}

    #Las Vegas
    #queryState = {"pagination":{"currentPage": pageNumber},"usersSearchTerm":"Las Vegas, NV","mapBounds":{"west":-116.91755348828124,"east":-113.70405251171874,"south":35.64420017467124,"north":36.78538246207047},"regionSelection":[{"regionId":18959,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":9}

    #Green Bay
    #queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"Green Bay, WI","mapBounds":{"west":-88.3527676220703,"east":-87.54939237792968,"south":44.43227951010534,"north":44.68424809978317},"regionSelection":[{"regionId":45548,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":11}
    
    queryState = {"pagination":{"currentPage":pageNumber},"usersSearchTerm":"Saint Louis, MO","mapBounds":{"west":-90.65190012207032,"east":-89.84852487792969,"south":38.51499098681778,"north":38.79114908607131},"regionSelection":[{"regionId":6891,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":11}
    
    #wants for get request
    wants = {"cat1":["listResults","mapResults"],"cat2":["total"]}

    #insert params from individual city into boilerplate
    params = {'searchQueryState' : queryState, 'wants' : wants}
    #parse the params as acceptable URL 
    toBeAppended = urlparse.urlencode(params)
    #Cooldown so zillow doesn't kick us out

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
    
    time.sleep(20)