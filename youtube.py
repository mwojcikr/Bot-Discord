import requests
import json
import os
from dotenv import load_dotenv

def get_videos_in_url(limit, channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={os.getenv('YOUTUBE_APKI_KEY')}&channelId={channel_id}&part=id&order=date"
    if limit is not None:
        url += "&maxResults=" + str(limit)
    return url


def get_videoID_from_page(url):
    header = {'Accept': 'application/json'}
    data = requests.get(url, headers=header).json()
    video_ids = []
    for video in data['items']:
        video_ids.append(video['id']['videoId'])
    return video_ids


def yt_create_config():
    with open("youtubeconfig.txt","w") as f:
        f.write("7veg1m26UkU,7veg1m26UkU")


def get_new_videos(received):
    with open("youtubeconfig.txt","r") as f:
        old = f.read()
        old = old.split(',')
    new = []
    for video_id in received:
        if video_id not in old:
            new.append(video_id)
    return new


def update_vide_file(new):
    with open("youtubeconfig.txt","a") as f:
        for video_id in new:
            f.write(f"{video_id},")


def generate_link(video_id : str):
    return f"https://www.youtube.com/watch?v={video_id}"


def get_channel_ids():
    with open("channels.json") as f:
        channels = json.load(f)
    return channels


def get_new_urls():
    load_dotenv()
    url = []
    channel_ids = get_channel_ids()
    print(channel_ids)
    for channel_name in channel_ids:
        query_result = get_videoID_from_page(get_videos_in_url(4,channel_ids[channel_name]))
        new = get_new_videos(query_result)
        update_vide_file(new)
        for video_id in new:
            url.append(generate_link(video_id))
    return url

