#Creator InnocentNyuu
#pip install KickApi
import time
from kickapi import KickAPI
from datetime import datetime, timedelta

# Create an instance of KickAPI
kick_api = KickAPI()

# Fetch video data
video = kick_api.video('video_id')

while True:
    # Convert to datetime object and format in the desired way
    original_date_obj = datetime.strptime(video.start_time, '%Y-%m-%d %H:%M:%S')
    formatted_date_str = original_date_obj.strftime('%Y-%m-%dT%H:%M:%S.000Z')

    # Fetch chat data for the video's channel and the specific date
    chat = kick_api.chat(video.channel.id, formatted_date_str)

    # Iterate over messages and print sender's username and text
    for message in chat.messages:
        print("{}: {}".format(message.sender.username, message.text))

    # Update start_time for the next iteration and pause for 5 seconds
    video.start_time = (original_date_obj + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(5)