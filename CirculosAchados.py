import cv2 
import numpy as np 
  
img = cv2.imread('bolas.jpg', cv2.IMREAD_COLOR) 
cv2.imshow('Imagem', img)
cv2.waitKey(0)
# imagem original, pronta para o processamento mostrada em janela

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Imagem_cinza', gray) 
cv2.waitKey(0)
# imagem cinza

gray_blurred = cv2.blur(gray, (9, 9)) 
cv2.imshow('Imagem_borrada', gray_blurred )
cv2.waitKey(0)
# imagem borrada

circulos = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 0, maxRadius =100) 
  
if circulos is not None: 
  
    
    circulos = np.uint16(np.around(circulos)) 
  
    
    for pt in circulos[0, : ]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
        
        print("Centro ({:}, {:}), radio = {:}".format(a, b, r))
  
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
		
        cv2.imshow("Circulos achados", img) 
        cv2.waitKey(0) 
        
# processamento de circulos achados

cv2.destroyAllWindows()