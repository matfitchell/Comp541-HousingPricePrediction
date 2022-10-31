
#library(rvest)
library(dplyr)
#library(stringr)
library(rjson)

readIn =  fromJSON (file = "D:\\Coding\\541_dataHousingPredictions\\Comp541-HousingPricePrediction\\Crawler\\new_JSON_read_files\\json_dump.json")

names = c("zpid", "id","providerListingId","imgSrc","hasImage","detailUrl","statusType","statusText","countryCurrency","price","unformattedPrice","address","addressStreet","addressCity","addressState","addressZipcode","isUndisclosedAddress","beds","baths","area","latLong", "isZillowOwned", "variableData", "badgeInfo", "hdpData", "isSaved", "hasOpenHouse", "openHouseStartDate", "openHouseEndDate", "openHouseDescription", "isUserClaimingOwner", "isUserConfirmedClaim", "pgapt", "sgapt", "zestimate", "shouldShowZestimateAsPrice", "has3DModel", "hasVideo", "isHomeRec", "brokerName", "hasAdditionalAttributions", "isFeaturedListing", "availabilityDate", "list", "relaxed")

mylist = readIn

dataFrame = data.frame(matrix(ncol = 8 , nrow = 0))
colnames(dataFrame) = c("ZPID","address", "price", "bed", "bath", "Sq.Feet","city", "zip-code")
for(i in 1:length(mylist)){
  zpid = mylist[[i]]$zpid
  if (is.null(mylist[[i]]$unformattedPrice) == FALSE)
    price = mylist[[i]]$unformattedPrice
  else 
    price = 0
  if (is.null(mylist[[i]]$address) == FALSE)
    address = mylist[[i]]$address
  else
    address ='empty'
  if (is.null(mylist[[i]]$bed) == FALSE)
    bed = mylist[[i]]$bed
  else
    bath = 0
  if (is.null(mylist[[i]]$baths) == FALSE)
    bath = mylist[[i]]$baths
  else
    bath = 0
  if (is.null(mylist[[i]]$area) == FALSE)
    area = mylist[[i]]$area
  else
    area = 0
  if (is.null(mylist[[i]]$addressCity) ==FALSE)
    city = mylist[[i]]$addressCity
  else 
    city = 'empty'
  if (is.null(mylist[[i]]$addressZipcode) == FALSE)
    zipCode = mylist[[i]]$addressZipcode
  else 
    zipCode = 0
  #print(c(price, address, bed, bath, area))
 dataFrame[nrow(dataFrame) + 1,] = c(zpid, address, price, bed, bath, area, city, zipCode)
}

#dataFrame <- setNames(do.call(rbind.data.frame, mylist), names)
#dataFrame = mylist %>% as_tibble(rownames = pkgconfig::get_config("tibble::rownames", NULL), .name_repair = c("zpid", "id","providerListingId","imgSrc","hasImage","detailUrl","statusType","statusText","countryCurrency","price","unformattedPrice","address","addressStreet","addressCity","addressState","addressZipcode","isUndisclosedAddress","beds","baths","area","latLong", "isZillowOwned", "variableData", "badgeInfo", "hdpData", "isSaved", "hasOpenHouse", "openHouseStartDate", "openHouseEndDate", "openHouseDescription", "isUserClaimingOwner", "isUserConfirmedClaim", "pgapt", "sgapt", "zestimate", "shouldShowZestimateAsPrice", "has3DModel", "hasVideo", "isHomeRec", "brokerName", "hasAdditionalAttributions", "isFeaturedListing", "availabilityDate", "list", "relaxed"))

#str(dataFrame)

#dframe = as.data.frame(readIn)
#str(dframe)
