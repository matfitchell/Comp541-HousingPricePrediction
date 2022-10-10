# Inspired by https://github.com/notesofdabbler

library(rvest)

url <- "https://www.zillow.com/homes/"
url <- paste0(url, "portland")

page <- read_html(url)

houses <- page %>%
  html_elements(".photo-cards li article")

##z_id <- houses %>% html_attr("id")
print(houses)

##address <- houses %>%
##  html_element(".zsg-photo-card-address") %>%
##  html_text()
prices <- c()
i <- 0
for(house in houses) {
  price <- house %>%
    html_element(xpath="//div/div[1]/div[2]/span") %>%
    html_text() %>%
    readr::parse_number()
  print(house)
  print(price)
  append(prices, price)
  i <- i + 1
}
##params <- houses %>%
##  html_element(".zsg-photo-card-info") %>%
##  html_text() %>%
##  strsplit("\u00b7")
# print(prices)
#