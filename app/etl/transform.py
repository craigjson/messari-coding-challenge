
# Transform RSS Feeds to Articles
from typing import List
from data.models import Article, Pattern
from requests import get
from etl.website import extract_articles_from_website

def transform_rss_entries_to_articles(rss_entries: list) -> List[Article]:
    return [transform_rss_entry_to_article(entry) for entry in rss_entries]

def transform_rss_entry_to_article(rss_entry) -> Article:
    if "content" in rss_entry.keys():
        print(f"""Title: {rss_entry.title}
              \nPublished:{rss_entry.published}
              \nContent:{rss_entry.content[0].value}\n""")
        
        return Article(
            title=rss_entry.title,
            content=rss_entry.content[0].value,
            published=rss_entry.published,
            link=rss_entry.link
        )
    else:
        # Content not found, parse summary or pull article html from the internet?
        print(get(rss_entry.link).content)
        return extract_articles_from_website()
    
# Determine if the article has a match for the pattern
def pattern_match_article_content(article_content: str, pattern: Pattern) -> bool:
    return pattern.pattern.search(article_content)