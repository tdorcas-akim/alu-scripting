#!/usr/bin/python3
"""This module prints the top 10 hot posts of a subreddit."""

import requests  # Permet d'envoyer une requête vers un site web


def top_ten(subreddit):
    """
    Affiche les 10 premiers titres des posts les plus populaires d'un subreddit.

    Args:
        subreddit (str): le nom du groupe Reddit (comme 'funny', 'science', etc.)
    """
    # On construit le lien vers Reddit (API spéciale)
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "SimpleScript/1.0"}  # Obligatoire, sinon Reddit dit "non"
    params = {"limit": 10}  # On veut juste les 10 premiers

    try:
        # On envoie la requête
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Si le subreddit est faux (ex: n'existe pas), on affiche None
        if response.status_code != 200:
            print("None")
            return

        # On transforme la réponse en dictionnaire Python
        data = response.json()

        # On prend les posts
        posts = data.get("data", {}).get("children", [])

        # S'il n'y a pas de posts, on affiche None
        if not posts:
            print("None")
            return

        # Sinon, on affiche chaque titre
        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None"))
