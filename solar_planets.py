import cv2
img=cv2.imread("116/solar-system.jpg") 
print(img.shape)

cv2.putText(img,
            "Sun",
             (20,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))  

cv2.putText(img,
            "mercrey",
             (80,180),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))

cv2.putText(img,
            "veneus",
             (160,200),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))

cv2.putText(img,
            "Earth",
             (300,250),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))

cv2.putText(img,
            "mars",
             (400,250),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))

cv2.putText(img,
            "jupeter",
             (500,250),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))

cv2.putText(img,
            "sauturn",
             (800,250),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))

cv2.putText(img,
            "uranus",
             (1000,250),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))

cv2.putText(img,
            "neptune",
             (1200,250),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255,
               ))
cv2.imshow("output",img)
cv2.waitKey(0)

# cv2.imwrite("Solar_systemwithname.jpg",img)