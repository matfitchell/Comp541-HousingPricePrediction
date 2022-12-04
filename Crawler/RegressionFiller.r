# installing/loading the package:
if (!require(installr)) {
install.packages("installr"); require(installr)} #load / install+load installr


#install.packages("scales")
# using the package:
#updateR() # this will start the updating process of your R installation.  It will check for newer versions, and if one is available, will guide you through the decisions you'd need to make.

dataset <- read.csv("D:/Coding/541_dataHousingPredictions/Comp541-HousingPricePrediction/Crawler/housing_data.csv")


#install.packages("caTools")
library(caTools)

split <- sample.split(dataset$Sq.Feet, SplitRatio = 0.7)
trainingset <- subset(dataset, split == TRUE)
testset <- subset(dataset, split == FALSE)

lm_r <- lm(formula = Sq.Feet ~ bed, data = trainingset)

coef(lm_r)

ypred <- predict(lm_r, newdata = testset)

#install.packages("ggplot2")
library(ggplot2)

ggplot() + geom_point(aes(x = testset$bed,
                        y = testset$Sq.Feet), colour = "red")+
                geom_line(aes(x = testset$bed,
                y = predict(lm_r, newdata = testset)), colour = "blue")+

                ggtitle("Square Feet Vs Number of Bedrooms(Testing)")+
                xlab("Bedrooms") +
                ylab("Square Feet")

ggplot() +
geom_plot(aes(x = testset$bed, y = testset$Sq.Feet),
colour = "red") +
geom_line(aes(x = trainingset$bed, y = predict(lm_r, newdata = trainingset)),
colour = "blue") +

ggtitle("Square Feet Vs Number of Bedrooms (Test Set)")+
xlab("Bedrooms") +
ylab("Square Footage")


write.csv(testset, "C:/UserDump/Code/Comp541-HousingPricePrediction/Crawler/testhousingdata.csv")
