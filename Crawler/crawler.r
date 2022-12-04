
#library(rvest)
library(dplyr)
#library(stringr)
library(rjson)

#Read in the compiled JSON file of all houses in data set // Should be downloaded to local memory 
readIn =  fromJSON (file = "D:\\Coding\\541_dataHousingPredictions\\Comp541-HousingPricePrediction\\Crawler\\new_JSON_read_files\\json_dump.json")

#set a variable list
mylist = readIn

#Initialize a dataframe with 7 columns for relavant data per house
dataFrame = data.frame(matrix(ncol = 8 , nrow = 0))
#set the column names
colnames(dataFrame) = c("ZPID","address", "price", "bed", "bath", "Sq.Feet","city", "zip-code")
#iterate over every house in the list 
for(i in 1:length(mylist)){
  #set house id
  zpid = mylist[[i]]$zpid
  #validate home price and assign 0 if empty
  if (is.null(mylist[[i]]$unformattedPrice) == FALSE)
    price = mylist[[i]]$unformattedPrice
  else 
    price = 0
  #assign entry with address present, assign 'empty' if empty
  if (is.null(mylist[[i]]$address) == FALSE)
    address = mylist[[i]]$address
  else
    address ='empty'
  #assign entry with number of bedrooms, assign 0 if empty
  if (is.null(mylist[[i]]$bed) == FALSE)
    bed = mylist[[i]]$bed
  else
    bath = 0
  #assign entry number of bathrooms, assign 0 if empty
  if (is.null(mylist[[i]]$baths) == FALSE)
    bath = mylist[[i]]$baths
  else
    bath = 0
  #assign entry square footage, assign 0 if empty
  if (is.null(mylist[[i]]$area) == FALSE)
    area = mylist[[i]]$area
  else
    area = 0
  #assign entry with relative city, assign 'empty' if empty 
  if (is.null(mylist[[i]]$addressCity) ==FALSE)
    city = mylist[[i]]$addressCity
  else 
    city = 'empty'
  #assign entry with zipcode, assign 0 if empty
  if (is.null(mylist[[i]]$addressZipcode) == FALSE)
    zipCode = mylist[[i]]$addressZipcode
  else 
    zipCode = 0
  #print entry to console to troubleshoot as error checking
  #print(c(price, address, bed, bath, area))
 dataFrame[nrow(dataFrame) + 1,] = c(zpid, address, price, bed, bath, area, city, zipCode)
}
#write dataFrame to CSV file for later reference
#write.csv(dataFrame, "D:\\Coding\\541_dataHousingPredictions\\Comp541-HousingPricePrediction\\Crawler\\housing_data")