#!/usr/bin/python3
"""
This module fetches and prints the titles of the first 10 hot posts
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
    # Reddit API URL to get "hot" posts from a subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Custom User-Agent: Reddit wants you to identify your app
    headers = {"User-Agent": "linux:topten.bot:v1.0 (by u/realstudent123)"}

    # Query parameters: we ask for 10 posts
    params = {"limit": 10}

    try:
        # Make the request
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # If the subreddit is invalid, Reddit sends 302 or 404
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        # Loop through each post and print the title
        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)

    except requests.RequestException:
        # If something goes wrong with the network or request
        print("None")
