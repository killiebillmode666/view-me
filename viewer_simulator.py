import random
import time
import requests

# Function to read a list of proxies from a text file.
def read_proxies(file_path):
    try:
        with open(file_path, 'r') as file:
            proxies = file.read().splitlines()
        return proxies
    except Exception as e:
        print(f"Error reading proxies from file: {str(e)}")
        return []

# Function to select a random proxy from the list.
def get_random_proxy(proxies):
    return random.choice(proxies)

def increase_viewers(stream_url, proxies_file_path):
    proxies = read_proxies(proxies_file_path)
    if not proxies:
        print("No proxies found in the file. Exiting.")
        return

    while True:
        fake_viewers = random.randint(1, 10)  # Simulate viewers joining your stream.
        print(f"New viewers joined: {fake_viewers}")

        # Select a random proxy from the list.
        proxy = get_random_proxy(proxies)
        print(f"Using proxy: {proxy}")

        # Use the selected proxy for the request.
        try:
            response = requests.get(stream_url, proxies={'http': proxy, 'https': proxy})
            if response.status_code == 200:
                print("Request succeeded.")
            else:
                print(f"Request failed. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error making request with proxy: {str(e)}")

        time.sleep(random.randint(10, 60))  # Simulate random viewer activity.

if __name__ == "__main__":
    stream_url = "https://chaturbate.com/badbiboy666/"
    proxies_file_path = "proxies.txt"
    increase_viewers(stream_url, proxies_file_path)
