import requests                # Used to make requests to the internet to get webpage data
from bs4 import BeautifulSoup  # Used to help read and navigate through the HTML data
import pandas as pd            # Used to help manage and analyze data in a table format
from io import StringIO        # Allows treating strings as if they were files
import time                    # Used to get the current date and time

def train_location():
    # Get today's date in the format 'day/month/year'
    current_date = time.strftime("%d/%m/%Y")
    print("Today's Date:", current_date)

    # Ask the user for the train number
    train_no = input("Enter the train number: ")
    
    # Ask the user for the date they are traveling
    journey_date = input("Enter the date of journey (dd/mm/yyyy): ")

    # Determine if the journey is today or in the future
    if current_date == journey_date:
        st = '0'  # The journey is today
    else:
        st = '1'  # The journey is not today

    try:
        # Create the URL to check the train's status
        url = f"https://www.railyatri.in/live-train-status/{train_no}?start_date={st}"

        # Get the webpage's content
        response = requests.get(url).text

        # Use BeautifulSoup to help read the HTML content from the webpage
        soup = BeautifulSoup(response, 'html.parser')

        # This will hold the data we are interested in
        data = []

        # Look through the webpage's data and find specific pieces of information in 'script' tags
        for item in soup.find_all('script', type="application/ld+json"):
            data.append(item.get_text())

        # Convert the relevant data (the third piece) into a format that Pandas can read
        json_data = StringIO(data[2])

        # Load the data into a Pandas DataFrame, which is like a table
        df = pd.read_json(json_data)

        # Print out the information we want, which is the current status of the train
        print(df["mainEntity"][0]['acceptedAnswer']['text'])
    
    # If the data isn't found, let the user know that the train has finished its journey
    except KeyError:
        print(f"The train {train_no} has reached its destination.")

# Call the function to check the train's status
train_location()

