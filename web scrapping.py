import pandas as pd                                             #to create dataframe
import requests                                                 #to send the request to the URL
from bs4 import BeautifulSoup                                   #to get the content in the form of HTML
import numpy as np                                              # to count the values

#assigning the URL with variable name url
url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
#request allow you to send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#creating an empty list, so that we can append the values
movie_name = []
year = []
time = []
rating = []
metascore = []
votes = []
gross = []

#storing the meaningfull required data in the variable
movie_data = soup.findAll('div', attrs= {'class': 'lister-item mode-advanced'})

#calling one by one for using for loop
for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)

    yearrel = store.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
    year.append(yearrel)

    runtime = store.p.find('span', class_ = 'runtime').text.replace(' min', '')
    time.append(runtime)

    rate = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n', '')
    rating.append(rate)

    meta  = store.find('span', class_ = 'metascore').text.replace(' ', '') if store.find('span', class_ = 'metascore') else '-'
    metascore.append(meta)
    #since, gross and votes have same attributes, that's why we had created a common variable and then used indexing
    value = store.find_all('span', attrs = {'name': 'nv'})
    
    vote = value[0].text
    votes.append(vote)
    
    grosses = value[1].text if len(value) >1 else '*****'
    gross.append(grosses)
    
    
#creating a dataframe using pandas library
anime_DF = pd.DataFrame({'Name of movie': movie_name, 'Year of release': year, 'Watchtime': time, 'Movie Rating': rating, 'Metascore': metascore, 'Votes': votes, 'Gross collection': gross})

#Saving data in Excel file:

anime_DF.to_excel("Top_100_IMDB_Movies.xlsx")
anime_DF.head(7)
if True:
    print('Web Scrapping Done !!')

