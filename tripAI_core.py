import json
import datetime
import requests
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def analyze_user_input(budget, days, trip_type):
    """Basic AI logic for trip suggestions."""
    if trip_type == "international" and budget > 1500:
        return "Paris, France"
    elif trip_type == "international" and 800 <= budget <= 1500:
        return "Bangkok, Thailand"
    elif trip_type == "domestic" and budget >= 500:
        return "New York, USA"
    else:
        return "Bali, Indonesia"

def get_flights_api_stub(destination):
    """Mock flight API."""
    return [
        f"Flight 1 → {destination} — $850",
        f"Flight 2 → {destination} — $920"
    ]

def get_hotels_api_stub(destination):
    """Mock hotel API."""
    return [
        f"Hotel Example A in {destination} — $100/night",
        f"Hotel Example B in {destination} — $150/night"
    ]

def generate_itinerary(destination, days):
    """Generate a basic itinerary."""
    sample_activities = {
        "Paris, France": ["Eiffel Tower", "Louvre Museum", "Seine River Cruise"],
        "Bangkok, Thailand": ["Grand Palace", "Wat Arun", "Floating Market"],
        "New York, USA": ["Statue of Liberty", "Central Park", "Times Square"],
        "Bali, Indonesia": ["Ubud Rice Terrace", "Tanah Lot Temple", "Seminyak Beach"]
    }
    spots = sample_activities.get(destination, ["Explore local sites"])
    itinerary = [{"day": i + 1, "activity": spots[i % len(spots)]} for i in range(days)]
    return itinerary

def generate_trip_plan(user_data):
    """Generate full trip plan."""
    destination = analyze_user_input(user_data["budget"], user_data["days"], user_data["type"])
    flights = get_flights_api_stub(destination)
    hotels = get_hotels_api_stub(destination)
    itinerary = generate_itinerary(destination, user_data["days"])
    map_link = f"https://www.google.com/maps/place/{destination.replace(' ', '+')}"

    trip_plan = {
        "destination": destination,
        "flights": flights,
        "hotels": hotels,
        "itinerary": itinerary,
        "map_link": map_link,
        "timestamp": str(datetime.datetime.now())
    }
    return trip_plan

def secure_store_data(data, filename="user_data/trip_encrypted.dat"):
    """Encrypt and store trip plan."""
    encrypted = cipher.encrypt(json.dumps(data).encode())
    with open(filename, "wb") as f:
        f.write(encrypted)
    return "Data securely stored."
