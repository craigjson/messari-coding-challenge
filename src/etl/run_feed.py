from load import load_article_into_postgres
from transform import transform_rss_entries_to_articles
from rss import extract_rss_entries_from_feed

# Run ETL Feed
def extract_transform_load_feed():
    try:
        rss_entries = extract_rss_entries_from_feed()
        articles = transform_rss_entries_to_articles(rss_entries)
        for article in articles:
            load_article_into_postgres(article)
    except Exception as e:
        print(f"Error running ETL Feed: {e.message}")