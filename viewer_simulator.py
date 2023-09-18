import random
import time

def increase_viewers(stream_url):
    while True:
        fake_viewers = random.randint(1, 10)  # Simulate viewers joining your stream.
        print(f"New viewers joined: {fake_viewers}")
        # Add code to interact with the streaming platform's API to update viewer count.
        time.sleep(random.randint(10, 60))  # Simulate random viewer activity.

if __name__ == "__main__":
    stream_url = "your_stream_url_here"
    increase_viewers(stream_url)
