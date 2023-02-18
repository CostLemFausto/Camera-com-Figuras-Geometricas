# Este software abre uma webcam, e plota figuras no video
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while True:
   _, frame = cap.read()
   #************************************************************************
   frame = cv.line(frame,(250,240),(390,240),(0,255,255),2) # Cria linha
   # ***********************************************************************
   frame = cv.circle(frame,(320,240),(50),(200,0,0),2) # cria circulo com o
   # centro nas coordenadas (x=320,y=240),(raio=50),(B=200,G=0,R=0),largura=2
   frame = cv.rectangle(frame,(260,180),(380,300),(0,0,255),3) # cria retangulo
   # **************************************************************************
   cv.imshow("frame",frame)
   key = cv.waitKey(1)
   if key == 27:    
    break
   #print("Dimensao/Canais",frame.shape)
cap.release()
cv.destryAllWindows()
