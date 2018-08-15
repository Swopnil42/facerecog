def recog():
    import cv2
    import numpy as np
    import sqlite3
    conn = sqlite3.connect('facerecog.db')
    c = conn.cursor()

    name=""
    add=""
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

    cam=cv2.VideoCapture(0);

    recognizer=cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("recognizer/trainingData.yml")

    Id1=0
    font=cv2.FONT_HERSHEY_SIMPLEX

    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(222,0,0),2)
            Id1,conf=recognizer.predict(gray[y:y+h,x:x+w])
            name=c.execute("SELECT name FROM facerecognize WHERE Id=%d"%Id1)
            add=c.execute("SELECT address FROM facerecognize WHERE Id=%d"%Id1)
            
            cv2.putText(img,(str(Id1)+str(name)+str(add)),(x,y+h),font,4,(255,0,0))
        cv2.imshow("Face",img);
        name=c.execute("SELECT name FROM facerecognize WHERE Id=%d"%Id1)
        add=c.execute("SELECT address FROM facerecognize WHERE Id=%d"%Id1)
        
        
        
        if (cv2.waitKey(1)==ord('q')):
            break;
    cam.release()
    cv2.destroyAllWindows()
