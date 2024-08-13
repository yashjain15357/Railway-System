import requests

# Get user input for the source station code, destination station code, and date of journey
from_station = input("Enter the source station code (e.g., 'BHS' for Bhopal Station): ")
to_station = input("Enter the destination station code (e.g., 'BPL' for Bhopal Junction): ")
date_of_journey = input("Enter the date of journey (YYYY-MM-DD): ")

# Define the URL for the API endpoint that provides train details between stations
url = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"

# Set up the parameters for the API request, using the input values
querystring = {
    "fromStationCode": from_station,  # Source station code provided by the user
    "toStationCode": to_station,      # Destination station code provided by the user
    "dateOfJourney": date_of_journey  # Date of the journey provided by the user
}

# Set up the headers needed to authenticate the API request
headers = {
    # make your own API key in Rapid website
    "x-rapidapi-key": "ff3a943637msh0da6e83acca135se105fc8jsndec2ee9b661d",  # Your unique API key
    "x-rapidapi-host": "irctc1.p.rapidapi.com"  # The host for the API
}

# Make the GET request to the API using the defined URL, headers, and parameters
response = requests.get(url, headers=headers, params=querystring)

# Convert the response to JSON format for easier data extraction
d = response.json()

# Loop through the list of trains in the response data
for i in range(0, len(d["data"])):
    # Print the train number and train name
    print(d['data'][i]['train_number'], end=" ")
    print(d['data'][i]['train_name'], ">>")
    
    # Print the departure time, source station, journey duration, destination station, and arrival time
    print(f"{d['data'][i]['from_std']} {d['data'][i]['from']}----{d['data'][i]['duration']}----{d['data'][i]['to']} {d['data'][i]['to_std']}")
    
    # Print a separator line for readability
    print('_________________________________________________________')
