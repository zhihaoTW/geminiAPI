import cv2
import random as rng
 
rng.seed(12345)
Image = cv2.imread("./piranha.jpg")

print(Image.shape)
#NewImage = Image[603:494, 696:628] Ymin Xmin Ymax Xmax

# X,Y,W,H (Xmin, Ymin), (Xmax, Ymax)

#Resize

Re_Image = cv2.resize(Image, (1000, 1000), interpolation=cv2.INTER_AREA)

color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))

cv2.rectangle(Re_Image, (494,603), (628, 696), color, 2)

cv2.imshow("Windows", Re_Image)

cv2.waitKey(0)
cv2.destroyAllWindows()