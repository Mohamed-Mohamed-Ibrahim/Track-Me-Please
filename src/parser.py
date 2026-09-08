import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        "--algorithm",
        choices=["mosse", "kcf", "csrt"],
        default="mosse",
        help="Tracking Algorithm",
    )
    return parser.parse_args()
