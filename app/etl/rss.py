# Get all RSS Entries for all news sources
from typing import Dict, List

from feedparser import parse
from util.url_cache import url_visited_set

from etl.html import get_raw_html_for_url


# Download RSS Feed from a URL, validate it and return the feed entries
def download_and_parse_rss_feed(rss_feed_url: str) -> List[Dict]:
    # Download RSS Feed from URL
    rss_feed = parse(rss_feed_url)
    # Determine if RSS Feed has well formed XML
    if rss_feed.bozo == 1:
        raise Exception(f"Failed to parse RSS Feed: {rss_feed_url} with\nError: {rss_feed.bozo_exception}")
    else:
        return rss_feed['entries']

# Check that the rss_entry has a link and that we have never visited it before
def should_parse_rss_entry(rss_entry: Dict) -> bool:
    if rss_entry['link'] in url_visited_set:
        print(f"Skipping URL: {rss_entry['link']}\n")
    return 'link' in rss_entry and rss_entry['link'] not in url_visited_set
    
def process_rss_entry(rss_entry: Dict) -> str:
    if 'content' not in rss_entry:
        # Content is not present in RSS Entry, attempt to download the raw HTML
        try:
            if should_parse_rss_entry(rss_entry):
                    entry_content_as_html = get_raw_html_for_url(rss_entry['link'])
                    url_visited_set.add(rss_entry['link'])
                    return entry_content_as_html
            else:
                # Nothing to do for this URL, skip this entry
                return None
        except Exception as e:
            print(f"Failed to download raw HTML for URL with\nError: {e}\n")
    else:
        return rss_entry['content'][0]['value']
