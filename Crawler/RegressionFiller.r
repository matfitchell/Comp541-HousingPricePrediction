# installing/loading the package:
if(!require(installr)) {
install.packages("installr"); require(installr)} #load / install+load installr

# using the package:
updateR() # this will start the updating process of your R installation.  It will check for newer versions, and if one is available, will guide you through the decisions you'd need to make.
dataset <- read.csv("C:/UserDump/Code/Comp541-HousingPricePrediction/Crawler/housing_data")

install.packages("caTools")
library(caTools)

split = sample.split(dataset$Sq.Feet, SplitRatio = 0.7)
trainingset = subset(dataset, split == TRUE)
testset = subset(dataset, split == FALSE)

lm.r = lm(formula = Sq.Feet ~ bed, data = trainingset)

coef(lm.r)

ypred = predict(lm.r, newdata = testset)

install.packages("ggplot2")
library(ggplot2)

ggplot() + geom_point(aes(x = trainingset$bed,
                        y = trainingset$Sq.Feet), colour = "red")+
                geom_line(aes(x = trainingset$bed,
                y=predict(lm.r, newdata = trainingset)), colour = "blue")+

                ggtitle("Square Feet Vs Number of Bedrooms(Training)")+
                xlab("Bedrooms") +
                ylab("Square Feet")

ggplot() +
geom_plot(aes(x=testset$bed, y = testset$Sq.Feet),
colour = "red")+
geom_line(aes(x = trainingset$bed, y = predict(lm.r,newdata = trainingset)),
colour = "blue") +

ggtitle ("Square Feet Vs Number of Bedrooms (Test Set)")+
xlab("Bedrooms") +
ylab("Square Footage")


write.csv(testset, "C:/UserDump/Code/Comp541-HousingPricePrediction/Crawler/testhousingdata.csv")

