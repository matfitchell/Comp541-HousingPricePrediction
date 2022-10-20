
library(rvest)
library(RSelenium)

url <- "https://www.zillow.com/los-angeles-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-119.21510774414062%2C%22east%22%3A-117.60835725585937%2C%22south%22%3A33.870121297819686%2C%22north%22%3A34.17175136070247%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

sapply(2:40, function(x) {
  url <- "https://www.zillow.com/los-angeles-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-119.21510774414062%2C%22east%22%3A-117.60835725585937%2C%22south%22%3A33.870121297819686%2C%22north%22%3A34.17175136070247%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
  paste0(url, x) }) -> urls

driver <- rsDriver(browser=c("firefox"))
remDr <- driver[["client"]]

df_all <- data.frame()
for(i in 1:(length(urls))) {
  remDr$navigate(paste0(urls[[i]]))
  Sys.Sleep(1)
  links <- remDr$findElements(using = "xpath", value = "//*[@class = 'plink']")
  df <- data.frame(link = unlist(sapply(links, function(x){x$getElementAttribute('href')})))
  Sys.sleep(1)
  df_all <- rbind(df_all, df)
}

#get house price
  house_price <- page %>% 
    rvest::html_nodes("ul") %>% 
    rvest::html_nodes(xpath = '//*[@class="price_social"]') %>% 
    rvest::html_text() %>%
    .[[1]]

#get street address
 street_address <- page %>% 
   rvest::html_nodes("span") %>% 
   rvest::html_nodes(xpath = '//*[@class="span8"]') %>% 
   rvest::html_nodes("h1") %>%
   rvest::html_text()

# getting the key facts from the condo
# key facts are: building type, square feet, year built, bedrooms and bathrooms,
# taxes, and age
  key_facts <- page %>% 
    rvest::html_nodes("ul") %>% 
    rvest::html_nodes(xpath = '//*[@class="key_facts"]') %>% 
    rvest::html_nodes("li") %>%
    rvest::html_text()

# converting links stored in a data.frame() as factors to character type stored in a vector df
links <- sapply(df_all$link, as.character)
# initalize empty data frame where we will be storing our scraped data 
df_all_data <- data.frame()
# write our scraper function
scraper <- function(links) {
  
  # save link in url object
  url <- links
  # parse page url
  page <- xml2::read_html(url)
  Sys.sleep(0.25)
  
  #get house price
  house_price <- page %>% 
    rvest::html_nodes("ul") %>% 
    rvest::html_nodes(xpath = '//*[@class="price_social"]') %>% 
    rvest::html_text() %>%
    .[[1]]
  
  #get street address
  street_address <- page %>% 
    rvest::html_nodes("span") %>% 
    rvest::html_nodes(xpath = '//*[@class="span8"]') %>% 
    rvest::html_nodes("h1") %>%
    rvest::html_text()
  
  # getting the key facts from the condo
  # key facts are: building type, square feet, year built, bedrooms and bathrooms,
  # taxes, and age
  key_facts <- page %>% 
    rvest::html_nodes("ul") %>% 
    rvest::html_nodes(xpath = '//*[@class="key_facts"]') %>% 
    rvest::html_nodes("li") %>%
    rvest::html_text()
  
  # removing unnecessary content from the vector of strings and naming the vector elements
  key_facts %>%
    stringr::str_replace_all(., ".*: ", "") %>%
    purrr::set_names(., nm = stringr::str_replace_all(key_facts, ":.*", "") %>%
                       stringr::str_replace_all(., "[0-9]+", "") %>%
                       stringi::stri_trim_both(.)) -> key_facts
  
# the following code assigns the scraped data for each condo where applicable
# if the information is not available, we are filling the observation with a NA value
# for example, there are condos where taxes are not available
# moreover, some condos are going to get build in the future, so age was not available
  
# get the building type 
  building_type <- ifelse("Property Type" %in% names(key_facts),
                          key_facts[ grep("Property Type", names(key_facts), ignore.case = TRUE, value = TRUE) ],
                          NA) 
  
# get square feet
  square_feet <- ifelse("Living Space" %in% names(key_facts),
                        key_facts[ grep("Living Space", names(key_facts), ignore.case = TRUE, value = TRUE) ],
                        NA)
  
# get the number of bedrooms
  bedrooms <- ifelse("Bedrooms" %in% names(key_facts),
                     key_facts[ grep("Bedrooms", names(key_facts), ignore.case = TRUE, value = TRUE) ],
                     NA)
  
# get the number of bathrooms
  bathrooms <- ifelse("Bathrooms" %in% names(key_facts),
                      key_facts[ grep("Bathrooms", names(key_facts), ignore.case = TRUE, value = TRUE) ],
                      NA)
  
# get when the condo was built
  year_built <- ifelse("Year Built" %in% names(key_facts),
                       key_facts[ grep("Year Built", names(key_facts), ignore.case = TRUE, value = TRUE) ],
                       NA)
  
# get the age of the condo
  age <- ifelse("Approximate Age" %in% names(key_facts),
                key_facts[ grep("Age", names(key_facts), ignore.case = TRUE, value = TRUE) ],
                NA)
  
# get the taxes (property taxes)
  taxes <- ifelse("Other Taxes" %in% names(key_facts) | "Municipal Taxes" %in% names(key_facts),  
                  key_facts[ grep("taxes", names(key_facts), ignore.case = TRUE, value = TRUE) ], 
                  NA)
  
# storing individual links in df_individual_page object
  df_individual_page <- data.frame(price = house_price,
                                   address = street_address,
                                   squares = square_feet,
                                   type = building_type,
                                   year = year_built,
                                   age = age,
                                   bed = bedrooms,
                                   bath = bathrooms,
                                   tax = taxes)
  
  # rbinding df_all_data and df_individual_page
  # <<- makes df_all_data a global variable. Making it available in the global environment
  df_all_data <<- rbind(df_all_data, df_individual_page)
}
# looping over all links in the vector and applying scraper function to each link
sapply(links, scraper)