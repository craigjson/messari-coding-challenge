from typing import List, Dict, Pattern as RegexPattern
from models.models import NewsSource, Pattern
import re


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
    "bankless": NewsSource(
        id = "bankless",
        url = "https://www.banklesshq.com/feed/podcast/",
    ),
    "a16z": NewsSource(
        id = "a16z",
        url = "https://a16z.com/feed/podcast/",
    ),
    "defipulse": NewsSource(
        id =  "defipulse",
        url = "https://defipulse.com/blog/feed/",
    )
}

