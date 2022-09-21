from typing import List

from bs4 import BeautifulSoup
from requests import get

from etl.pattern_match import article_content_matches_pattern


# Download raw HTML from the URL
def get_raw_html_for_url(url: str) -> str:
    # Use some default headers to avoid 403 errors
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    response_data = get(url=url, headers=headers)
    if response_data.ok:
        return response_data.text
    else:
        raise Exception(f"Get Request to {url} returned status code: {response_data.status_code}")

# Parse the HTML from the RSS Entry and return the article content
def parse_html_for_article_content(html: str) -> str:
    soup = BeautifulSoup(html, 'lxml')
    article_content = ""
    for paragraph in soup.find_all('p'):
        article_content += paragraph.text
    return article_content

# Determine if the html content matches any of the configured patterns
def html_content_matches_pattern(html: str) -> bool:
    article_content = parse_html_for_article_content(html)
    return article_content_matches_pattern(article_content)

# Parse and match the entry html content with configured patterns
def parse_and_match_entry_html_content(html: str) -> str:
    try:
        article_content = parse_html_for_article_content(html)
        if article_content_matches_pattern(article_content):
            return article_content
    except Exception as e:
        print(f"Failed to parse article content with\nError: {e}\n")
