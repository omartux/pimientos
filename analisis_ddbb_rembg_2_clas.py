# -*- coding: utf-8 -*-
"""
MCC 2023
Omar Castillo Alarcon
Erwin Cruz Mamani
Edwin Fredy Chambi Mamani
Gludher Quispe Cotacallapa
Etapa de Clasificacion
"""
import cv2 as cv
import numpy as np
from datetime import date, datetime
import os
import time
from rembg import remove
#from PIL import Image

print ("Iniciando ")
time.sleep(1)

hoy = date.today()
ahora = datetime.now()
tiempo_actual = ahora.strftime("%H:%M:%S")
# Objetivos : 
# Leer imagen y obtener parametros, definir que tipo de pimiento es
# - Guardar los datos en un archivo csv.

print (hoy)
print (ahora)
print (tiempo_actual)

archivo = open('clasificacion.csv', "w+")
cadena = ('dia'+";"+'tiempo_actual'+";"+'archivo'+";"
          +'medH'+";"+'medS'+";"+'medV'+";"
          +'medB'+";"+'medG'+";"+'medR'+";"
          +'medL'+";"+'medA'+";"+'medBB'+";"
          +'medY'+";"+'medCB'+";"+'medCR'+";"
          +'meH'+";"+'meS'+";"+'meV'+";"
          +'meB'+";"+'meG'+";"+'meR'+";"
          +'meL'+";"+'meA'+";"+'meBB'+";"
          +'meY'+";"+'meCB'+";"+'meCR'+";"+'tipo'+"\n") 

archivo.write(cadena)
archivo.close()
tipo = 'No cumple'
carpeta = os.getcwd()
fotos = str(carpeta+"\\Morrones_ddbb")
print ("entrando en ... ",fotos)

for filename in os.listdir(fotos):
    if filename.endswith(".jpg") or filename.endswith(".JPG"):
        print (filename)
        entrada = './Morrones_ddbb/'+filename
        #print (entrada)
        frame = cv.imread(entrada,cv.IMREAD_UNCHANGED)
        #print (frame)
        bgr = remove(frame)
        normal = bgr.copy()
        b,g,r,alpha = cv.split(normal)
        # Combinar los canales de color en una sola imagen
        color_img = cv.merge((b,g,r))
        #cv.imwrite('alfa.png',alpha)
        #break
        # Crear una nueva imagen JPEG con un fondo negro
        background = alpha
        
        (thresh, mask) = cv.threshold(background, 10, 255, cv.THRESH_BINARY)
                                                     
        # Copiar la imagen PNG con transparencia en la imagen JPEG con fondo negro
        #background_copy = background.copy()
        #background_copy[:, :, :] = 0
        #background_copy = cv.copyTo(color_img, alpha, background_copy) 
        result = color_img

            
        hsv = cv.cvtColor(result, cv.COLOR_BGR2HSV)
        bgr = result
        lab = cv.cvtColor(result, cv.COLOR_BGR2LAB)
        ycbcr = cv.cvtColor(result, cv.COLOR_BGR2YCR_CB)
        
        h, s, v = cv.split(hsv)
        b, g, r = cv.split(bgr)
        l, a, bb = cv.split(lab)
        y, cb, cr = cv.split(ycbcr)
        
        #chancada de salidas para eliminar info
        h = cv.bitwise_and(h, h, mask=mask)
        s = cv.bitwise_and(s, s, mask=mask)
        v = cv.bitwise_and(v, v, mask=mask)
        
        b = cv.bitwise_and(b, b, mask=mask)
        g = cv.bitwise_and(g, g, mask=mask)
        r = cv.bitwise_and(r, r, mask=mask)
        
        l = cv.bitwise_and(l, l, mask=mask)
        a = cv.bitwise_and(a, a, mask=mask)
        bb = cv.bitwise_and(bb, bb, mask=mask)

        y = cv.bitwise_and(y, y, mask=mask)
        cb = cv.bitwise_and(cb, cb, mask=mask)
        cr = cv.bitwise_and(cr, cr, mask=mask)

        #flatten y ordenar h
        vector_h = h.flatten()
        newVector_h=[]
        for i in vector_h:    
            if i>0:
                newVector_h.append(i)

        #flatten y ordenar s
        vector_s = s.flatten()
        newVector_s=[]
        for i in vector_s:    
            if i>0:
                newVector_s.append(i)

        #flatten y ordenar v
        vector_v = v.flatten()
        newVector_v=[]
        for i in vector_v:    
            if i>0:
                newVector_v.append(i)
                
        #flatten y ordenar b
        vector_b = b.flatten()
        newVector_b=[]
        for i in vector_b:    
            if i>0:
                newVector_b.append(i)

        #flatten y ordenar g
        vector_g = g.flatten()
        newVector_g=[]
        for i in vector_g:    
            if i>0:
                newVector_g.append(i)
                
        
        #flatten y ordenar r
        vector_r = r.flatten()
        newVector_r=[]
        for i in vector_r:    
            if i>0:
                newVector_r.append(i)


        #flatten y ordenar l
        vector_l = l.flatten()
        newVector_l=[]
        for i in vector_l:    
            if i>0:
                newVector_l.append(i)


        #flatten y ordenar a
        vector_a = a.flatten()
        newVector_a=[]
        for i in vector_a:    
            if i>0:
                newVector_a.append(i)


        #flatten y ordenar bb
        vector_bb = bb.flatten()
        newVector_bb=[]
        for i in vector_bb:    
            if i>0:
                newVector_bb.append(i)

        #flatten y ordenar y
        vector_y = y.flatten()
        newVector_y=[]
        for i in vector_y:    
            if i>0:
                newVector_y.append(i)

        #flatten y ordenar cb
        vector_cb = cb.flatten()
        newVector_cb=[]
        for i in vector_cb:    
            if i>0:
                newVector_cb.append(i)

        #flatten y ordenar cr
        vector_cr = cr.flatten()
        newVector_cr=[]
        for i in vector_cr:    
            if i>0:
                newVector_cr.append(i)
                
        medH = np.median(newVector_h)
        medS = np.median(newVector_s)
        medV = np.median(newVector_v)
        
        medB = np.median(newVector_b)
        medG = np.median(newVector_g)
        medR = np.median(newVector_r)
        
        medL = np.median(newVector_l)
        medA = np.median(newVector_a)
        medBB = np.median(newVector_bb)
    
        medY = np.median(newVector_y)
        medCB = np.median(newVector_cb)
        medCR = np.median(newVector_cr)
        #********************
        meH = np.mean(newVector_h)
        meS = np.mean(newVector_s)
        meV = np.mean(newVector_v)
        
        meB = np.mean(newVector_b)
        meG = np.mean(newVector_g)
        meR = np.mean(newVector_r)
        
        meL = np.mean(newVector_l)
        meA = np.mean(newVector_a)
        meBB = np.mean(newVector_bb)
         
        meY = np.mean(newVector_y)
        meCB = np.mean(newVector_cb)
        meCR = np.mean(newVector_cr)
        
        meH = np.round(meH,2)
        meS = np.round(meS,2)
        meV = np.round(meV,2)
    
        meB = np.round(meB,2)
        meG = np.round(meG,2)
        meR = np.round(meR,2)
   
        meL = np.round(meL,2)
        meA = np.round(meA,2)
        meBB = np.round(meBB,2)
        
        meY = np.round(meY,2)
        meCB = np.round(meCB,2)
        meCR = np.round(meCR,2)  
        
        #evaluacion del tipo
        
        #parametros de calidad Color Lab Amarillo son
        Media_L_A = 214
        sigma_L_A = 5*2
        
        Media_A_A = 116 
        sigma_A_A = 2*2
        
        Media_B_A = 210 
        sigma_B_A = 2*2
        #
        #parametros de calidad Color Lab Naranja son
        Media_L_N = 185 
        sigma_L_N = 6*2
        
        Media_A_N = 138 
        sigma_A_N = 5*2
        
        Media_B_N = 201 
        sigma_B_N = 2*2
        #
        #parametros de calidad Color Lab Rojo son
        Media_L_R = 123 
        sigma_L_R = 8*2
        
        Media_A_R = 178 
        sigma_A_R = 3*2
        
        Media_B_R = 167
        sigma_B_R = 4*2
        #
        
        if meL<(Media_L_A + sigma_L_A) and meL >(Media_L_A - sigma_L_A) and \
            meA<(Media_A_A + sigma_A_A) and meA>(Media_A_A - sigma_A_A) and \
                meBB<(Media_B_A + sigma_B_A) and meBB>(Media_B_A - sigma_B_A):
                    tipo = 'amarillo'
        
        if meL<(Media_L_N + sigma_L_N) and meL >(Media_L_N - sigma_L_N) and \
            meA<(Media_A_N + sigma_A_N) and meA>(Media_A_N - sigma_A_N) and \
                meBB<(Media_B_N + sigma_B_N) and meBB>(Media_B_N - sigma_B_N):
                    tipo = 'naranja'

        if meL<(Media_L_R + sigma_L_R) and meL >(Media_L_R - sigma_L_R) and \
            meA<(Media_A_R + sigma_A_R) and meA>(Media_A_R - sigma_A_R) and \
                meBB<(Media_B_R + sigma_B_R) and meBB>(Media_B_R - sigma_B_R):
                    tipo = 'rojo'
        
        
            #guardado de los resultados
        hoy = date.today()
        ahora = datetime.now()
        tiempo_actual = ahora.strftime("%H:%M:%S")
        
        print(medH, medS, medV, medB, medG, medR, medL, medA, medBB, medY, medCB, medCR)
        print(meH, meS, meV, meB, meG, meR, meL, meA, meBB, meY, meCB, meCR, tipo)
        
        #titulos
        archivo = open('clasificacion.csv', "a")
        cadena = (str(hoy)+";"+str(tiempo_actual)+";"+str(filename)+";"
                  +str(medH)+";"+str(medS)+";"+str(medV)+";"
                  +str(medB)+";"+str(medG)+";"+str(medR)+";"
                  +str(medL)+";"+str(medA)+";"+str(medBB)+";"
                  +str(medY)+";"+str(medCB)+";"+str(medCR)+";"
                  +str(meH)+";"+str(meS)+";"+str(meV)+";"
                  +str(meB)+";"+str(meG)+";"+str(meR)+";"
                  +str(meL)+";"+str(meA)+";"+str(meBB)+";"
                  +str(meY)+";"+str(meCB)+";"+str(meCR)+";"+str(tipo)+"\n") 
        archivo.write(cadena)
        archivo.close()
 
cv.destroyAllWindows()
