
library(dplyr)

data_frame <- read.csv("D:\\Coding\\541_dataHousingPredictions\\Comp541-HousingPricePrediction\\Crawler\\housing_data.csv")

data_frame_2 <- read.csv("D:\\Coding\\541_dataHousingPredictions\\Comp541-HousingPricePrediction\\Crawler\\latlongdata.csv")

myList = data_frame_2

myList2 = data_frame

price <- data_frame(c(3), )

output_dataframe <- data.frame(matrix(ncol = 5 , nrow = 0))

colnames(output_dataframe) <= c("address", "long", "lat", "address", "price")

for (i in seq_along(myList)){
    address <- myList[[i]]$address

    long <- myList[[i]]$lon

    lat <- myList[[i]]$lat

    address <- myList[[i]]$address

    price <- myList2[[i]]$price
    }

#write output dframe to file
write.csv(output_dataframe, "D:\\Coding\\541_dataHousingPredictions\\Comp541-HousingPricePrediction\\Crawler")