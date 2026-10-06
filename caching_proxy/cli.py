import argparse

from .server import run_server
from .cache import Cache


def main():
    parser = argparse.ArgumentParser(
        description="Caching HTTP Proxy"
    )

    parser.add_argument(
        "--port",
        type=int,
        help="Port to run the proxy on"
    )

    parser.add_argument(
        "--origin",
        help="Origin server URL"
    )

    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear the cache"
    )

    args = parser.parse_args()

    if args.clear_cache:
        cache = Cache()
        cache.clear()
        print("Cache cleared.")
        return

    if args.port is None or args.origin is None:
        parser.error("--port and --origin are required")

    run_server(args.port, args.origin)


if __name__ == "__main__":
    main()