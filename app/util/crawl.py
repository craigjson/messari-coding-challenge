from enum import Enum

class CrawlStatus(Enum):
    """Crawl status enum"""
    NOT_STARTED = 0
    PENDING = 1
    RUNNING = 2
    SUCCESS = 3
    FAILED = 4