from enum import Enum


class TrackingAlgorithm(Enum):
    MOSSE = "mosse"
    KCF = "kcf"
    CSRT = "csrt"
