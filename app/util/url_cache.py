from redis import Redis

redis = Redis(host='0.0.0.0', port=6379)
cache_name = 'url_visited_cache'

def is_containted_in_url_visited_cache(url: str) -> bool:
    return redis.sismember(cache_name, url)

def add_to_url_visited_cache(url: str):
    redis.sadd(cache_name, url)