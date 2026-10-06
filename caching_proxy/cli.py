import argparse

from .server import run_server


def main():
    parser = argparse.ArgumentParser(
        description="Caching HTTP Proxy"
    )

    parser.add_argument(
        "--port",
        type=int,
        required=True,
        help="Port to run the proxy on"
    )

    parser.add_argument(
        "--origin",
        required=True,
        help="Origin server URL"
    )

    args = parser.parse_args()

    run_server(args.port, args.origin)


if __name__ == "__main__":
    main()