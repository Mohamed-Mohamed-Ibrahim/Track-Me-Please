import cv2
from src.parser import get_parser
from constants.tracking_algorithm_enum import TrackingAlgorithm


tracker = None


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3)
    cv2.putText(
        img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
    )


def start_tracking():
    global tracker

    cap = cv2.VideoCapture(1)
    success, frame = cap.read()
    bbox = cv2.selectROI("Tracking", frame, False)
    tracker.init(frame, bbox)

    while True:
        timer = cv2.getTickCount()
        success, img = cap.read()
        success, bbox = tracker.update(img)

        if success:
            drawBox(img, bbox)
        else:
            cv2.putText(
                img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2
            )

        cv2.rectangle(img, (15, 15), (200, 90), (255, 0, 255), 2)
        cv2.putText(
            img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2
        )
        cv2.putText(
            img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2
        )
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        if fps > 60:
            myColor = (20, 230, 20)
        elif fps > 20:
            myColor = (230, 20, 20)
        else:
            myColor = (20, 20, 230)
        cv2.putText(
            img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2
        )
        cv2.imshow("Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    args = get_parser()

    if args.algorithm == TrackingAlgorithm.MOSSE.value:
        tracker = cv2.legacy.TrackerMOSSE_create()
    elif args.algorithm == TrackingAlgorithm.KCF.value:
        tracker = cv2.TrackerKCF_create()
    elif args.algorithm == TrackingAlgorithm.CSRT.value:
        tracker = cv2.TrackerCSRT_create()
    else:
        print("Unkown Tracking Algorithm")

    start_tracking()
