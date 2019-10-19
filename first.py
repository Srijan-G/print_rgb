import cv2
def click_event(event, x,y, flags, param):
    if event== cv2.EVENT_LBUTTONDOWN:
      print (img[x,y]) 
img=cv2.imread("dog.jpg")
cv2.imshow("dog",img)


cv2.setMouseCallback("dog",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()