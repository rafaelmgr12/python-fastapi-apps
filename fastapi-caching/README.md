# Caching in FastAPI Applications

Caching is a powerful technique used to improve the performance and efficiency of web applications by storing the results of expensive computations or frequently accessed data. In this FastAPI project, we demonstrate how to implement both in-memory caching and disk caching.

## What is Caching?

Caching can be thought of as a method to store and quickly retrieve frequently accessed data or results of expensive computations. This prevents the need to repeatedly fetch or compute the same data, thus saving time and resources.

### Types of Caching

1. **Memory Caching**:
   - Stores data in the system’s RAM for super-fast access.
   - **Advantages**: Lightning-fast access times.
   - **Disadvantages**: Limited by system RAM and data is lost when the system restarts.

2. **Disk Caching**:
   - Stores data on disk for relatively fast access.
   - **Advantages**: More storage capacity, and persistent storage (data survives system restarts).
   - **Disadvantages**: Slower than memory caching.

## Why Use Caching?

- **Performance Improvement**: Caching reduces the need to perform expensive operations repeatedly, improving application performance.
- **Reduced Server Load**: By minimizing redundant computations, caching lowers the load on servers.
- **Cost Efficiency**: Lower server load can translate to cost savings, especially when using cloud services.
- **User Experience**: Faster response times enhance user experience, making applications more responsive.

## In-Memory Caching with `functools`

In-memory caching is implemented using the `lru_cache` decorator from the `functools` module. This decorator caches the results of function calls based on their inputs, reducing the need to recompute results for the same inputs.

### Example: In-Memory Caching

```python
from fastapi import FastAPI
from functools import lru_cache
import asyncio

app = FastAPI()

# In-memory caching using lru_cache
@lru_cache(maxsize=100)
async def get_factorial(n: int):
    await asyncio.sleep(2)  # Simulate delay
    if n == 1:
        return 1
    return n * await get_factorial(n - 1)

@app.get("/factorial/{num}")
async def compute_factorial(num: int):
    result = await get_factorial(num)
    return {"number": num, "factorial": result}
```

## Disk Caching with Diskcache

Disk caching stores data on disk for persistent storage. We use the `diskcache` library to implement disk caching in our FastAPI application.

### Example: Disk Caching

```python
from fastapi import FastAPI
from diskcache import Cache
from functools import wraps
from hashlib import sha256
import json

app = FastAPI()
cache = Cache("cache_dir")  # Initialize disk cache

def cache_decorator(expire=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = sha256(json.dumps((func.__name__, args, kwargs), sort_keys=True).encode()).hexdigest()
            data = cache.get(key)
            if not data:
                data = func(*args, **kwargs)
                cache.set(key, data, expire=expire)
            return data
        return wrapper
    return decorator

@app.post("/data")
@cache_decorator(expire=3600)
def get_data(body: dict):
    return body  # Return input for demonstration

@app.get("/clear-cache")
def clear_cache():
    cache.clear()
    return {"message": "Cache cleared"}

```

## How to Run

1. **Install Dependencies**:

   - Install FastAPI and Uvicorn: `pip install fastapi uvicorn`
   - Install Diskcache: `pip install diskcache`

2. **Run the Application**:

   - Start the server with Uvicorn: `uvicorn main:app --reload`

3. **Test the Endpoints**:

   - Use the `/factorial/{num}` endpoint to test in-memory caching.
   - Use the `/data` endpoint to test disk caching and the `/clear-cache` endpoint to clear the cache.

## Conclusion

Implementing caching in your FastAPI applications can significantly improve performance, reduce server load, and enhance user experience. By leveraging both in-memory and disk caching, you can optimize your application for different scenarios.

Feel free to explore this project and experiment with caching strategies to see the impact on performance!
