from datetime import date

from data.postgres import Base, Session, engine
from data.models.article import Article
from data.models.pattern import Pattern
from data.models.news_source import NewsSource

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

articles = [
    Article(id="1", 
            source_id="decrypt",
            title="Title 1", 
            content="Content 1", 
            link="link1", 
            published="2020-01-01"
    ),
    Article(id="2",
            source_id="blockworks",
            title="Title 2", 
            content="Content 2", 
            link="link2", 
            published="2020-01-02"
    ),
    Article(id="3", 
            source_id="dailyhodl", 
            title="Title 3", 
            content="Content 3", 
            link="link3", 
            published="2020-01-03"
    )
    ]

def create_db():
    Base.metadata.create_all(engine)
    session = Session()
    session.commit()
    session.close()
    
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
    
def create_articles():
    session = Session()
    try:
        [session.add(article) for article in articles]
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

def load_mock_data():
    #create_db()
    #create_sources()
    #create_patterns()
    create_articles()