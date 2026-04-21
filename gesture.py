import cv2
import mediapipe as mp

class HandDetector():

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mpDraw = mp.solutions.drawing_utils

    def detect_hands(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        pos = None

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                h, w, c = frame.shape

                lm = hand.landmark[8]

                x = int(lm.x * w)
                y = int(lm.y * h)

                pos = (x, y)

                self.mpDraw.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

        return frame, pos