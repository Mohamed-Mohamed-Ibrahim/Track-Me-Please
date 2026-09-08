import argparse
from constants.tracking_algorithm_enum import TrackingAlgorithm


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        "--algorithm",
        choices=[algorithm.value for algorithm in TrackingAlgorithm],
        default="mosse",
        help="Tracking Algorithm",
    )
    return parser.parse_args()
