import cv2
import time
from gesture import HandDetector
from calculator_ui import Calculator

def main():

    cap = cv2.VideoCapture(0)

    detector = HandDetector()
    calc = Calculator()

    last_click = 0
    delay = 0.8

    while True:

        success, frame = cap.read()

        if not success:
            continue

        frame = cv2.flip(frame,1)

        frame, pos = detector.detect_hands(frame)

        if pos:

            x, y = pos

            for bx, by, val in calc.buttons:

             if bx < x < bx + calc.size and by < y < by + calc.size:
                    if time.time() - last_click > delay:

                        last_click = time.time()

                        if val == "C":
                            calc.expression = ""

                        elif val == "=":
                            try:
                                calc.expression = str(eval(calc.expression))
                            except:
                                calc.expression = "Error"

                        else:
                            calc.expression += val

        frame = calc.draw(frame)

        cv2.imshow("Hand Gesture Calculator", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

main()