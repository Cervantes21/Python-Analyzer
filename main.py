import cv2
# Importando Librerías.

face_cascade = cv2.CascadeClassifier('./raw/haarcascade_frontalface_default.xml')
# Guardamos en una variable nuestra Haarcascade

cap = cv2.VideoCapture(0)
# Hacemos referencia de nuestra web-cam. Canal de referencia 0.

while True:
# Comenzamos llamando un ciclo While para analizar los fotogramas.
    _, img = cap.read()
# Con la función cap.read() para leer cada uno de los fotogramas del vídeo.

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convertimos los fotogramas a escala de grises.

    faces = face_cascade.detectMultiScale(gray, 1.1,4)
# En la variable faces guardaremos todas las caras que detecte el programa con el metodo detectMultiScale()
# '''
# Los dos últimos parametros después de gray, son para ir manejando la escala de grises y como los irá detectando el programa. ['Más información:'](https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81)
# '''
    for (x, y, w, h) in faces:
# (x,y,w,h) son los vertices del cuadrado.
        cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0),2)
# Luego con la función cv2.rectangle() pintaremos ese cuadro encima de las caras. (255,0,0) se refiere al color del cuadro y el 2 al grosor de la línea.
    cv2.imshow('img', img)
    # Utilizamos esta función para mostrar el fotograma ya modificado y con la cara detectada.

    k = cv2.waitKey(30)
# Está función nos permite revisar cada 30 milisegundos si se esta presionando alguna tecla. 
    if k == 27: # 27 es el ascii para Esc
        break
cap.release()
# Para salir del programa y cerrar la cámara web.

