# import the necessary packages
from imutils.video import VideoStream
import imutils
import time
import cv2
import land_mark
 
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor", required=True,
#	help="path to facial landmark predictor")
#ap.add_argument("-r", "--picamera", type=int, default=-1,
#	help="whether or not the Raspberry Pi camera should be used")
#args = vars(ap.parse_args())
 
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
#print("[INFO] loading facial landmark predictor...")
#detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor("./face_predictor/shape_predictor_68_face_landmarks.dat")

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] camera sensor warming up...")
vs = VideoStream(1).start()
time.sleep(2.0)
lm = land_mark.LandMark();

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream, resize it to
    # have a maximum width of 400 pixels, and convert it to
    # grayscale
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lm.setVideo(gray);
    
    mapa = lm.getLandMark();
    
    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
    for face in mapa:  
        for mark in face:            
            x = mark[0]
            y = mark[1]
            cv2.circle(frame, (int(x),int(y)), 2, (0, 0, 255), -1)
	  
    # show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()