from datetime import date

from data.postgres import Base, Session, engine
from data.models.article import Article
from data.models.pattern import Pattern
from data.models.news_source import NewsSource

articles = [
    Article(id="1", title="Title 1", content="Content 1", link="link1", published="2020-01-01"),
    Article(id="2", title="Title 2", content="Content 2", link="link2", published="2020-01-02"),
    Article(id="3", title="Title 3", content="Content 3", link="link3", published="2020-01-03")
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

def load_mock_data():
    # Generate DB Schema
    Base.metadata.create_all(engine)

    # Create Session
    session = Session()

    ## Create News Source
    [session.add(source) for source in news_sources]

    ### Create Patterns
    [session.add(pattern) for pattern in patterns]

    ## Create Articles
    [session.add(article) for article in articles]

    ## Commit Changes to DB
    session.commit()
    session.close()