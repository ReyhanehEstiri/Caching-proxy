# Caching Proxy

A simple HTTP caching proxy server built with Python.

This project was built as part of the [roadmap.sh Caching Proxy project](https://roadmap.sh/projects/caching-server).

The proxy receives HTTP GET requests, forwards them to an origin server, caches the responses locally, and serves cached responses for subsequent requests.

## Features

- Forward GET requests to an origin server
- Persistent local response caching
- `X-Cache: HIT` and `X-Cache: MISS` response headers
- Configurable port and origin server
- Clear cache from the command line
- Installable CLI command
- Unit tests with pytest

## Project Structure

```text
caching-proxy/
├── caching_proxy/
│   ├── __init__.py
│   ├── cache.py
│   ├── server.py
│   └── cli.py
├── tests/
│   └── test_cache.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Requirements

- Python 3.10+
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/ReyhanehEstiri/Caching-proxy.git
cd Caching-proxy
```

Install the project:

```bash
pip install -e .
```

## Usage

Start the proxy:

```bash
caching-proxy --port 3000 --origin https://dummyjson.com
```

The proxy will be available at:

```text
http://localhost:3000
```

For example:

```text
http://localhost:3000/products/1
```

## Cache Behavior

The first request for a URL is a cache miss:

```text
Cache MISS: /products/1
Forwarding request to: https://dummyjson.com/products/1
```

The response contains:

```text
X-Cache: MISS
```

When the same URL is requested again, the response is served from the cache:

```text
Cache HIT: /products/1
```

The response contains:

```text
X-Cache: HIT
```

This prevents the proxy from making another request to the origin server for the same cached resource.

## Clear Cache

To clear the stored cache:

```bash
caching-proxy --clear-cache
```

Output:

```text
Cache cleared.
```

## Running Tests

Run the unit tests with:

```bash
pytest
```

Example output:

```text
4 passed
```

## Technologies

- Python
- http.server
- urllib
- pickle
- pytest

## Project Challenge

This project is based on the [roadmap.sh Caching Proxy challenge](https://roadmap.sh/projects/caching-server).

