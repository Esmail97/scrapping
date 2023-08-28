from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.booking.com/searchresults.en-gb.html?label=gog235jc-1DCAEoggI46AdICVgDaFCIAQGYAQm4ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArDuuaEGwAIB0gIkZmJhYjE4YzAtNDdhMy00MmY1LTk2NWItN2UzOTgyNTk1OWEx2AIE4AIB&aid=397594&ss=Cairo%2C+Egypt&ssne=London&ssne_untouched=London&efdco=1&lang=en-gb&src=searchresults&dest_id=-290692&dest_type=city&ltfd=6%3A1%3A%3A&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

response  = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# Find all the hotel elements in the HTML document
hotels = soup.findAll('div', {'data-testid': 'property-card'})

hotels_data = []
# Loop over the hotel elements and extract the desired data
for hotel in hotels:
    # Extract the hotel name
    name_element = hotel.find('div', {'data-testid': 'title'})
    name = name_element.text.strip()

    # Extract the hotel location
    location_element = hotel.find('span', {'data-testid': 'address'})
    location = location_element.text.strip()

    # Extract the hotel price
    price_element = hotel.find('span', 
                               {'data-testid': 'price-and-discounted-price'}) 
    #price = price_element.text.strip()
    
    # Extract the hotel rating
    rating_element = hotel.find('div', {'class': 'b5cd09854e d10a6220b4'})
    #rating = rating_element.text.strip()
    
    # Append hotels_data with info about hotel
    hotels_data.append({
        'name': name,
        'location': location,
        'price': price_element,
        'rating': rating_element
    })

hotels = pd.DataFrame(hotels_data)
hotels.head()
hotels.to_csv('hotels.csv', header=True, index=False)
