#!/usr/bin/python3
"""
This script defines a function that uses recursion
to get all hot post titles from a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively gets all hot post titles of a subreddit.

    Args:
        subreddit (str): The subreddit name to query.
        hot_list (list): The list that accumulates titles (used by recursion).
        after (str): The "after" token for pagination.

    Returns:
        A list of titles (strings), or None if subreddit is invalid.
    """
    # We build the URL to ask Reddit for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Reddit wants us to give a custom User-Agent to avoid blocking
    headers = {"User-Agent": "MySimpleScript/1.0"}

    # We ask for 100 posts per page (max allowed) and use 'after' to paginate
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None
        # subreddit is probably invalid

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title")
            hot_list.append(title)

        # If there is another page, recurse with new 'after' token
        next_page = data.get("after")
        if next_page:
            return recurse(subreddit, hot_list, next_page)

        return hot_list
    # No more pages, return the full list

    except Exception:
        return None
