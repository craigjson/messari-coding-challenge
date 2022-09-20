import re
from typing import List
from .models import Article, NewsSource, Pattern

articles = [
    Article(id="1", title="Title 1", content="Content 1", published="2020-01-01"),
    Article(id="2", title="Title 2", content="Content 2", published="2020-01-02"),
    Article(id="3", title="Title 3", content="Content 3", published="2020-01-03")
    ]

patterns = [
    Pattern(
        id = "listings",
        pattern = ".*((Coinbase)|(Binance)).*list.*"
    ),
    Pattern(
        id = "hacks",
        pattern = ".*((hack)|(exploit)|(vuln)).*"
    ),
    Pattern(
        id = "eth_news",
        pattern = ".*((Ethereum)|(ETH)).*((fork)|(upgrad)).*"
    )
]

news_sources = [
    NewsSource(
        id = "decrypt",
        url = "https://decrypt.co/feed",
    ),
    NewsSource(
        id= "blockworks",
        url= "https://blockworks.co/feed",
    ),
    NewsSource(
        id=  "cryptopotato",
        url= "https://cryptopotato.com/feed",
    ),
    NewsSource(
        id= "cryptobriefing",
        url= "https://cryptobriefing.com/feed",
    ),
    NewsSource(
        id= "dailyhodl",
        url= "https://dailyhodl.com/feed",
    ),
    NewsSource(
        id= "cointelegraph",
        url= "https://cointelegraph.com/rss",
    ),
    NewsSource(
        id = "coindesk",
        url= "https://www.coindesk.com/arc/outboundfeeds/rss/",
    ),
]

