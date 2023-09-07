import os
import cv2

path = "Images/"
Images = []
for img in os.listdir(path):
    file, extension = os.path.splitext(img)
    if extension in ['.jpg', '.jpeg', '.jfif', '.png', '.jif', '.gif']:
        file_name = path+"/"+img
        print(file_name)
        Images.append(file_name)
print(len(Images))
count = len(Images)
frame = cv2.imread(Images[0])
height , width , channels  = frame.shape
size = (width,height)
print(size)
out = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    frame=cv2.imread(Images[i])
    out.write(frame)
out.release()
print("Done")