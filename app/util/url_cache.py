import os

from redis import Redis

cache_name = 'url_visited_cache'

try:
    redis = Redis(host=os.getenv('REDIS_URL'), port=os.getenv('REDIS_PORT'))
except Exception as e:
    print(f"Failed to connect to Redis with error: {e}")
    
def is_containted_in_url_visited_cache(url: str) -> bool:
    try:
        return redis.sismember(cache_name, url)
    except Exception as e:
        print(f"Failed to check if URL is contained in cache with error: {e}")
        return False

def add_to_url_visited_cache(url: str):
    try:
        redis.sadd(cache_name, url)
    except Exception as e:
        print(f"Failed to add URL to cache with error: {e}")

def remove_from_url_visited_cache(url: str):
    try:
        redis.srem(cache_name, url)
    except Exception as e:
        print(f"Failed to remove URL from cache with error: {e}")
