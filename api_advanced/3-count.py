#!/usr/bin/python3
"""Count keywords in titles of hot posts from a subreddit."""


import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Count given words in hot posts titles (case-insensitive).
    Prints sorted counts (desc by count, then alphabetically).
    """

    # Set a User-Agent so Reddit doesn't block us
    headers = {"User-Agent": "Mozilla/5.0"}

    # URL to request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code != 200:
            return  # Subreddit doesn't exist, do nothing

        data = response.json().get("data", {})
        posts = data.get("children", [])

        # Go through all posts
        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                word_lc = word.lower()
                count = title.count(word_lc)
                if count > 0:
                    if word_lc in word_count:
                        word_count[word_lc] += count
                    else:
                        word_count[word_lc] = count

        # Recursive call if there's a next page
        if data.get("after"):
            return count_words(subreddit, word_list,
                               data.get("after"), word_count)

        # All data is collected, now print
        if word_count:
            # Sort first by count (desc), then word (asc)
            sorted_words = sorted(word_count.items(),
                                  key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")

    except Exception:
        return  
