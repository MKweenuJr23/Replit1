import requests
import json
from typing import Dict, Any

# Define the API endpoint for Ditto
API_URL = "https://pokeapi.co/api/v2/pokemon/ditto"

def fetch_pokemon_data(url: str) -> Dict[str, Any] | None:
    """
    Fetches JSON data from a given API URL.

    Args:
        url: The URL to make the GET request to.

    Returns:
        A dictionary containing the parsed JSON data, or None if the request failed.
    """
    print(f"Attempting to fetch data from: {url}")
    try:
        # Make the GET request to the API
        response = requests.get(url)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON content
        data = response.json()
        print("Data successfully fetched.")
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def format_name(name: str) -> str:
    """Cleans a hyphenated name string for display."""
    return ' '.join(word.capitalize() for word in name.split('-'))

def display_pokemon_details(data: Dict[str, Any]):
    """
    Prints the extracted details of the Pokémon in a formatted way.

    Args:
        data: The Pokémon JSON object.
    """
    name = format_name(data.get('name', 'N/A'))
    pokemon_id = data.get('id', 'N/A')
    
    print("\n" + "="*40)
    print(f"| Pokémon: {name.upper()} ({pokemon_id})".ljust(39) + "|")
    print("="*40)

    # General Information
    height = data.get('height') # Height is in decimetres (dm)
    weight = data.get('weight') # Weight is in hectograms (hg)

    print(f"  > Height: {height / 10 if height is not None else 'N/A'} m")
    print(f"  > Weight: {weight / 10 if weight is not None else 'N/A'} kg")
    print("-" * 40)

    # Abilities
    abilities = data.get('abilities', [])
    print("  > Abilities:")
    for slot in abilities:
        ability_name = format_name(slot['ability']['name'])
        is_hidden = " (Hidden)" if slot['is_hidden'] else ""
        print(f"    - {ability_name}{is_hidden}")
    print("-" * 40)

    # Base Stats
    stats = data.get('stats', [])
    print("  > Base Stats:")
    for stat_slot in stats:
        stat_name = format_name(stat_slot['stat']['name'])
        base_stat = stat_slot['base_stat']
        print(f"    - {stat_name.ljust(15)}: {base_stat}")
    print("="*40 + "\n")


if __name__ == "__main__":
    # Ensure the 'requests' library is installed: pip install requests
    
    ditto_data = fetch_pokemon_data(API_URL)
    
    if ditto_data:
        display_pokemon_details(ditto_data)
    else:
        print("Could not display details. Please check the API URL or your network")