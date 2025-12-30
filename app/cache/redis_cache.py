import os
import ssl
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

# redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)
redis_client = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True,
    ssl_cert_reqs=ssl.CERT_NONE
)


# def get_cached_prediction(key: str):
#     value = redis_client.get(key)
#     return eval(value) if value else None

def get_cached_prediction(key):
    try:
        return redis_client.get(key)
    except redis.RedisError as e:
        print("Redis error:", e)
        return None



def set_cached_prediction(key: str, value: dict):
    redis_client.set(key, str(value))