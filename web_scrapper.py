import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm



print("Starting the scraping process...")  # Debugging statement

# URL of the e-commerce website (Books to Scrape)
url = 'http://books.toscrape.com/'

try:
    # Send a request to the website
    response = requests.get(url)
    response.raise_for_status()  # Ensure we successfully get the webpage
    
    # Check if the response is successful
    print(f"Status Code: {response.status_code}")
    print(response.text[:500])  # Print the first 500 characters of the HTML content for debugging

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book containers (div with class 'product_pod')
    product_containers = soup.find_all('article', class_='product_pod')

    # Initialize empty lists to store book details
    book_titles = []
    book_prices = []
    book_ratings = []

    # Use tqdm to show a progress bar while scraping
    for product in tqdm(product_containers, desc="Scraping books", unit="book"):
        try:
            # Get the book title
            title = product.find('h3').find('a')['title']
            
            # Get the book price
            price = product.find('p', class_='price_color').text.strip()
            
            # Get the book rating (this is stored as a class name with a star rating)
            rating = product.find('p', class_='star-rating')['class'][1]  # Extract the rating from the class
            
            # Append the extracted data to the lists
            book_titles.append(title)
            book_prices.append(price)
            book_ratings.append(rating)

        except AttributeError:
            # Handle any missing data gracefully
            continue

    # Create a DataFrame to store the data
    data = {
        'Book Title': book_titles,
        'Price': book_prices,
        'Rating': book_ratings
    }

    df = pd.DataFrame(data)

    # Save the data to a CSV file
    df.to_csv('books.csv', index=False)

    print("Book information has been saved to 'books.csv'")

except Exception as e:
    print(f"Error occurred: {e}")