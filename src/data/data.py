from typing import List, Dict, Pattern as RegexPattern
from models.models import Article, NewsSource, Pattern
import re

articles: Dict[str, Article] = {
    "1": Article("1", "Title 1", "Content 1", "2020-01-01"),
    "2": Article("2", "Title 2", "Content 2", "2020-01-02"),
    "3": Article("3", "Title 3", "Content 3", "2020-01-03"),
}

patterns: Dict[str, Pattern] = {
    "listings" : Pattern(
        id = "listings",
        pattern = re.compile(".*((Coinbase)|(Binance)).*list.*")
    ),
    "hacks" : Pattern(
        id = "hacks",
        pattern = re.compile(".*((hack)|(exploit)|(vuln)).*")
    ),
    "eth_news" : Pattern(
        id = "eth_news",
        pattern = re.compile(".*((Ethereum)|(ETH)).*((fork)|(upgrad)).*")
    )
}

news_sources: Dict[str, NewsSource] = {
    "decrypt": NewsSource(
        id = "decrypt",
        url = "https://decrypt.co/feed",
    ),
    "blockworks": NewsSource(
        id= "blockworks",
        url= "https://blockworks.co/feed",
    ),
    "cryptopotato": NewsSource(
        id=  "cryptopotato",
        url= "https://cryptopotato.com/feed",
    ),
    "cryptobriefing": NewsSource(
        id= "cryptobriefing",
        url= "https://cryptobriefing.com/feed",
    ),
    "dailyhodl": NewsSource(
        id= "dailyhodl",
        url= "https://dailyhodl.com/feed",
    ),
    "cointelegraph": NewsSource(
        id= "cointelegraph",
        url= "https://cointelegraph.com/rss",
    ),
    "coindesk": NewsSource(
        id = "coindesk",
        url= "https://www.coindesk.com/arc/outboundfeeds/rss/",
    ),
}

