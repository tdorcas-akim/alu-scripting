#!/usr/bin/python3
"""
This module contains a function that gets the number of subscribers
for a given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of a given subreddit.
    If the subreddit is invalid or request fails, returns 0.

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: Number of subscribers
    """
    # URL to get info about a subreddit, in JSON format
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Set a custom User-Agent (Reddit recommends this)
    headers = {"User-Agent": "MyRedditChecker/1.0 (by u/fakeusername)"}

    try:
        # We make the request without allowing redirects (to avoid fake subs)
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if we got a valid response (status code 200)
        if response.status_code == 200:
            # Parse the JSON and get the number of subscribers
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers", 0)
            return subscribers
        # If we got a 404 or other error, return 0
        return 0

    except requests.RequestException:
        # If the request totally fails (e.g., no internet), return 0
        return 0
