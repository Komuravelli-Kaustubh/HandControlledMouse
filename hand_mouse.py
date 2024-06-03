import cv2
import mediapipe
import pyautogui
capture_hands = mediapipe.solutions.hands.Hands()
drawing_options = mediapipe.solutions.drawing_utils
cam = cv2.VideoCapture(0)
screen_w,screen_h= pyautogui.size()
x1=y1=x2=y2=0
while True:
    _,img = cam.read()
    img = cv2.flip(img,1)
    img_h,img_w,_ = img.shape
    rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_img)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_options.draw_landmarks(img,hand)
            one_hand_landmarks = hand.landmark
            for id,lm in enumerate(one_hand_landmarks):
                x=int(lm.x*img_w)
                y=int(lm.y*img_h)
                # print(x,y)
                if(id==8):
                    mouse_x = int(screen_w/img_w * x)
                    mouse_y = int(screen_h/img_h * y)
                    cv2.circle(img,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1=x
                    y1=y
                if(id==4):
                    x2=x
                    y2=y
                    cv2.circle(img,(x,y),10,(0,255,255))
            dist=(y2-y1)
            print(dist)
            if(dist<=43):
                print('clicked')
                pyautogui.click()
    cv2.imshow("Hand movement Vid Cap:",img)
    key=cv2.waitKey(10)
    if key==27:
        break

cam.release()
cv2.destroyAllWindows()
