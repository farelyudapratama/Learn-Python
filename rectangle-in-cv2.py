import cv2
import numpy as np
canvas = np.zeros((640, 480, 3),np.uint8)
canvas += 255
rectangle = cv2.rectangle(canvas,(150, 200),(350, 400),(255, 0, 0), 4)
cv2.imshow('Canvas with Rectangle',rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()


from tkinter  import *
from textwrap import fill
canvas = Canvas(width=300, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_rectangle(20,20, 300, 300, width=10, fill='red')
mainloop()
