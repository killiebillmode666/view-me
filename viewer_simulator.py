import random
import time
import requests  # Import the requests library for HTTP requests.

# Function to update viewer count via the streaming platform's API.
def update_viewer_count(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            viewer_data = response.json()
            return viewer_data['viewer_count']
        else:
            print(f"Failed to fetch viewer count. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error updating viewer count: {str(e)}")

def increase_viewers(stream_url, api_url):
    while True:
        fake_viewers = random.randint(1, 10)  # Simulate viewers joining your stream.
        print(f"New viewers joined: {fake_viewers}")
        
        # Update viewer count via the streaming platform's API.
        viewer_count = update_viewer_count(api_url)
        if viewer_count is not None:
            print(f"Current viewer count: {viewer_count}")
        
        time.sleep(random.randint(10, 60))  # Simulate random viewer activity.

if __name__ == "__main__":
    stream_url = "https://chaturbate.com/badbiboy666/"
    api_url = "https://viewerbot.webcam/api"  # Replace with the actual API endpoint.
    increase_viewers(stream_url, api_url)
