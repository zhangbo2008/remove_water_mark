# coding=utf-8

from nowatermark import WatermarkRemover

# path = 'data/'

# watermark_template_filename = path + 'anjuke-watermark-template.jpg'
# remover = WatermarkRemover()
# remover.load_watermark_template(watermark_template_filename)

# remover.remove_watermark(path + 'anjuke2.jpg', '1.png')
# remover.remove_watermark(path + 'anjuke3.jpg', path + 'anjuke3-result.jpg')
# remover.remove_watermark(path + 'anjuke4.jpg', path + 'anjuke4-result.jpg')

import cv2
a=~cv2.imread('9.png',0)
img=cv2.imread('微信图片_20241231111137.jpg')
dst = cv2.inpaint(img, a, 5, cv2.INPAINT_TELEA)
cv2.imwrite('oooooooooo.png',dst)
