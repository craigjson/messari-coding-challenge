from datetime import date

from data.postgres import Base, Session, engine
from data.models.article import Article
from data.models.pattern import Pattern
from data.models.news_source import NewsSource
from data.models.article_pattern_match import ArticlePatternMatch


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

def create_db():
    session = Session()
    Base.metadata.create_all(engine)
    session.commit()
    session.close()
    print("created DB")
    
def create_sources():
    session = Session()
    try:
        [session.add(source) for source in news_sources]
        session.commit()
    except:
        print("News Source already exists")
    finally:
        session.close()
    
def create_patterns():
    session = Session()
    try:
        [session.add(pattern) for pattern in patterns]
        session.commit()
    except:
        print("Patterns already exists")
    finally:
        session.close()

def load_mock_data():
    create_db()
    create_sources()
    create_patterns()
    print()