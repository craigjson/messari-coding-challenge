from datetime import datetime
from typing import List

from data.models.article import Article
from data.models.news_source import NewsSource
from util.constants import rss_feed_pull_cadence_in_seconds
from util.crawl import CrawlStatus
from util.time import is_time_between_greater_than

from etl.html import parse_html_for_article_content, html_content_matches_pattern
from etl.rss import download_and_parse_rss_feed, process_rss_entry


# Given a NewsSource, determine if it should be parsed for articles
# NewsSource should be parsed if the last run was a failure 
# or if it has not been parsed in the last N seconds where N is 
# configured in util/constants.py
def should_parse_news_source(news_source: NewsSource) -> bool:
    last_run_status = CrawlStatus(news_source.status)
    return last_run_status == CrawlStatus.FAILED \
        or last_run_status == CrawlStatus.NOT_STARTED \
        or is_time_between_greater_than(
            datetime.now(),
            news_source.last_processed, 
            rss_feed_pull_cadence_in_seconds)
    
# Parse News Source and return valid articles
def parse_news_source(news_source: NewsSource) -> List[Article]:
    if (should_parse_news_source(news_source)):
        try:
            valid_articles = []
            feed_entries = download_and_parse_rss_feed(news_source.url)
            for rss_entry in feed_entries:
                entry_content_as_html = process_rss_entry(rss_entry)
                
                if entry_content_as_html:
                    article_content = parse_html_for_article_content(entry_content_as_html)
                    article =  Article(
                                    id = rss_entry['link'],
                                    source_id = news_source.id,
                                    title = rss_entry['title'],
                                    content = article_content,
                                    published = rss_entry['published'],
                                    last_updated = datetime.now()
                                )
                    if html_content_matches_pattern(article_content):
                            article.has_match = True
                    valid_articles.append(article)
            return valid_articles
        except Exception as e:
            print(f"Failed to parse news source: {news_source.url} with\nError: {e}\n")
            raise e
    else:
        return []