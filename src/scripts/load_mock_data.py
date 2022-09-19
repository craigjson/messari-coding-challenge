from datetime import date

from ..data.postgres import Base, Session, engine
from ..data.mock_data import articles, news_sources, patterns


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