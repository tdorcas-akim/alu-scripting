#!/usr/bin/python3
"""This module fetches and prints the titles of the first 10 hot posts
from a given subreddit using the Reddit API.
"""


import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts of a subreddit.
    If the subreddit is invalid or cannot be reached, prints None.

    Args:
        subreddit (str): The subreddit to fetch data from.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditScript/1.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # If subreddit doesn't exist
        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")
