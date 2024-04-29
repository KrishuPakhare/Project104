import cv2

#Read image
img= cv2.imread("C:/Users/Dell/OneDrive/Desktop/whitehatjr/Project 104/solar-system.jpg")

#To show text
cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)   
            )
cv2.putText(img,
            "Mercury",
            (120,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
cv2.putText(img,
            "Venus",
            (190,155),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
cv2.putText(img,
            "Earth",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
cv2.putText(img,
            "Mars",
            (390,155),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
cv2.putText(img,
            "Jupiter",
            (550,370),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
cv2.putText(img,
            "Saturn",
            (770,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
cv2.putText(img,
            "Uranus",
            (970,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
cv2.putText(img,
            "Neptune",
            (1110,135),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   
            )
#Show/Display image
cv2.imshow("Output",img)

#Save image
cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)


