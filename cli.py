import argparse

from server import run_server


parser = argparse.ArgumentParser()

parser.add_argument("--port", type=int, required=True)
parser.add_argument("--origin", required=True)

args = parser.parse_args()

run_server(args.port, args.origin)