import urllib.request as request
import numpy as np
import cv2
from PIL import Image
import time
url = 'http://192.168.2.101:8080/shot.jpg'


while True:
    img = request.urlopen(url)
    img_bytes = bytearray(img.read())
    img_np = np.array(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(img_np, -1)
    cv2.imshow('Smart Scanner', frame)
    if cv2.waitKey(1) == ord('s'):
        print('Save')
        img_pil = Image.fromarray(frame)
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
        print(time_str)
        img_pil.save(f'{time_str}.pdf')