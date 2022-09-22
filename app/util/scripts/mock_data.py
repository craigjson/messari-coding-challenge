from datetime import date

from data.models.news_source import NewsSource
from data.models.pattern import Pattern

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
        pattern = ".*((Ethereum)|(ETH)).*((fork)|(upgrade)).*"
    ),
    Pattern(
        id = "stablecoins",
        pattern = ".*((USDC)|(USD Coin)).*((USDT)|(Tether)).*((BUSD)|(Binance USD)).*((DAI)|(Dai Stablecoin)).*"
    )
]

news_sources = [
    NewsSource(
        id = "decrypt",
        url = "https://decrypt.co/feed",
        last_processed = date.today(),
        status = 0
    ),
    NewsSource(
        id= "blockworks",
        url= "https://blockworks.co/feed",
        last_processed = date.today(),
        status = 0
    ),
    NewsSource(
        id=  "cryptopotato",
        url= "https://cryptopotato.com/feed",
        last_processed = date.today(),
        status = 0
    ),
    NewsSource(
        id= "cryptobriefing",
        url= "https://cryptobriefing.com/feed",
        last_processed = date.today(),
        status = 0
    ),
    NewsSource(
        id= "dailyhodl",
        url= "https://dailyhodl.com/feed",
        last_processed = date.today(),
        status = 0
    ),
    NewsSource(
        id= "cointelegraph",
        url= "https://cointelegraph.com/rss",
        last_processed = date.today(),
        status = 0
    ),
    NewsSource(
        id = "coindesk",
        url= "https://www.coindesk.com/arc/outboundfeeds/rss/",
        last_processed = date.today(),
        status = 0
    ),
]
