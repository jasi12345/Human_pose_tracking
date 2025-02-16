import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose

pose= mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
    )

video=cv2.VideoCapture(r"C:\Users\Keanu\Downloads\pose_detection\robot.mp4")

if(video is None):
    print("Error:Video is not Loaded")

else:
    while(True):
        ret,frame =video.read()

      
        result=pose.process(frame)
        print(result.pose_landmarks)

        mp_drawing.draw_landmarks(
            frame,result.pose_landmarks,mp_pose.POSE_CONNECTIONS

            )


        cv2.imshow("original",frame)

        if cv2.waitKey(2)==ord('q'):
            break

video.release()
cv2.destroyAllWindows()
