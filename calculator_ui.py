import cv2

class Calculator:

    def __init__(self):

        self.size = 80
        self.expression = ""

        self.buttons = [

        (300,100,"7"), (380,100,"8"), (460,100,"9"), (540,100,"/"),

        (300,180,"4"), (380,180,"5"), (460,180,"6"), (540,180,"*"),

        (300,260,"1"), (380,260,"2"), (460,260,"3"), (540,260,"-"),

        (300,340,"C"), (380,340,"0"), (460,340,"="), (540,340,"+")


        ]

    def draw(self, frame):

        cv2.rectangle(frame,(300,30),(620,90),(0,0,0),-1)

        cv2.putText(frame,self.expression,(410,75),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

        for bx,by,val in self.buttons:

            cv2.rectangle(frame,(bx,by),(bx+self.size,by+self.size),(255,255,255),2)

            cv2.putText(frame,val,(bx+25,by+50),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

        return frame