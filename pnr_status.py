import requests
import time

# Get today's date
today_date = time.strftime("%d-%m-%Y")

# Take PNR number as input from the user
pnr_number = input("Enter the PNR number: ")

# API request details
url = "https://irctc1.p.rapidapi.com/api/v3/getPNRStatus"
querystring = {"pnrNumber": pnr_number}

headers = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY_HERE",
    "x-rapidapi-host": "irctc1.p.rapidapi.com"
}

try:
    # Make the API request
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Raises an error for bad HTTP status codes
    info = response.json()

    # Check if the 'data' key exists in the JSON response
    if 'data' not in info:
        raise ValueError("Invalid response: 'data' field not found.")

    # Print today's date
    print("Today's Date:", today_date)

    # Print train details
    print(info["data"]["Doj"], "                     ", info["data"]["DestinationDoj"])
    print(" ", info["data"]["DepartureTime"], "----------", info["data"]["Duration"], "----------", info["data"]["ArrivalTime"])
    print(" ", info["data"]["From"], "                           ", info["data"]["To"])
    print(info["data"]["FromDetails"]["stationName"], "                     ", info["data"]["ToDetails"]["stationName"])
    print("PNR  : ", info["data"]["Pnr"])
    print("Class: ", info["data"]["Class"])
    print("Chart Prepared: ", info["data"]["ChartPrepared"])

    # Print passenger details
    for i in range(len(info["data"]["PassengerStatus"])):
        print("Passenger :", info["data"]["PassengerStatus"][i]["Number"])
        print(info["data"]["PassengerStatus"][i]["BookingCoachId"], "-", info["data"]["PassengerStatus"][i]["BookingBerthCode"], "-",
              info["data"]["PassengerStatus"][i]["BookingBerthNo"], "::", info["data"]["PassengerStatus"][i]["CurrentStatusNew"])

except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:", e)
except ValueError as ve:
    print("An error occurred while processing the data:", ve)
except KeyError as ke:
    print("Missing key in the data:", ke)
except Exception as ex:
    print("An unexpected error occurred:", ex)
