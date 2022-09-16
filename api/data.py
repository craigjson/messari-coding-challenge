from typing import List, Dict
from models import Feed, Pattern


sources: Dict[str, Feed] = {
    "bankless": Feed(
        id = "bankless",
        url = "https://www.banklesshq.com/feed/podcast/",
        patterns = ["bankless", "bankless podcast"],
        
    ),
    "a16z": Feed(
        id = "a16z",
        url = "https://a16z.com/feed/podcast/",
        patterns = ["a16z", "a16z podcast"],
    ),
    "defipulse": Feed(
        id =  "defipulse",
        url = "https://defipulse.com/blog/feed/",
    )
}

patterns = Dict[str, Pattern] = {
    "listings" : Pattern(
        id = "listings",
        pattern = ".*((Coinbase)|(Binance)).*list.*"
    ),
    "hacks" : Pattern(
        id = "hacks",
        pattern = ".*((hack)|(exploit)|(vuln)).*"
    ),
    "eth_news": Pattern(
        id = "eth_news",
        pattern = ".*((Ethereum)|(ETH)).*((fork)|(upgrad)).*"
    )
}