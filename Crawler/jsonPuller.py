import http.client
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

pageNumber = 1

boilerPlate = '/search/GetSearchPageState.htm?searchQueryState='

queryState = '{"pagination":{"currentPage":2},"usersSearchTerm":"Los Angeles, CA","mapBounds":{"west":-119.44444734375,"east":-113.01744539062501,"south":32.757531675134366,"north":35.104452906128245},"regionSelection":[{"regionId":12447,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":8}'

wants = '{"pagination":{"currentPage":2},"usersSearchTerm":"Los Angeles, CA","mapBounds":{"west":-119.44444734375,"east":-113.01744539062501,"south":32.757531675134366,"north":35.104452906128245},"regionSelection":[{"regionId":12447,"regionType":6}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True},"isManufactured":{"value":False},"isLotLand":{"value":False},"isTownhouse":{"value":False}},"isListVisible":True,"mapZoom":8}'

requestId = '&requestId=19'

conn = http.client.HTTPSConnection("www.zillow.com")

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

payload = ""

conn.request("GET", boilerPlate+queryState+wants+requestId, payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))