import numpy as np
import cv2 as cv
# import GUI
from matplotlib import pyplot as plt
from test import *

# app=QApplication(sys.argv)
# s=App(Qwidget)

# print(s.openFileNameDialog())

# userip=s.openFileNameDialog()
database_array=[]
names =get_names()
for i in range(len(names)):
	if names[i].find(".jpeg")!=-1:
		pass
	elif names[i].find(".txt")!=-1:
		pass
	else:
		images=get_images(names[i])
		database_array.append([names[i],images])


# print(database_array)


def get_matches(input_image,database_image):
	MIN_MATCH_COUNT = 10
	img1 = cv.imread(input_image) # queryImage
	img2 = cv.imread(database_image) # trainImage
	# Initiate SIFT detector
	sift = cv.xfeatures2d.SIFT_create()
	# find the keypoints and descriptors with SIFT
	kp1, des1 = sift.detectAndCompute(img1,None)
	kp2, des2 = sift.detectAndCompute(img2,None)
	FLANN_INDEX_KDTREE = 1
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 50)
	flann = cv.FlannBasedMatcher(index_params, search_params)
	matches = flann.knnMatch(des1,des2,k=2)
	# store all the good matches as per Lowe's ratio test.
	good = []
	for m,n in matches:
		if m.distance < 0.7*n.distance:
			good.append(m)

	if len(good)>MIN_MATCH_COUNT:
		src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
		dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
		M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
		matchesMask = mask.ravel().tolist()
		h,w,d = img1.shape
		pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
		dst = cv.perspectiveTransform(pts,M)
		img2 = cv.polylines(img2,[np.int32(dst)],True,255,3, cv.LINE_AA)
		return (len(good))
	else:
		return ( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
		matchesMask = None


# print(get_matches("/home/arkasarkar/Desktop/project/6.jpeg","/home/arkasarkar/Desktop/project/7.jpeg"))
def get_name(userip):
	matched_array=[]
	number_matches = 0
	type_matched = ""
	name=""
	# temp=[]
	for i in range(0,len(database_array)):

		current_name=database_array[i][0]
		# temp.append(current_name)
		current_images=database_array[i][1]
		for j in range(len(database_array[i][1])):
			try:

				a=(get_matches(userip, "/home/arkasarkar/Desktop/project/%s/%s" %(current_name,str(database_array[i][1][j]))))
				if a>number_matches:
					number_matches=a
					type_matched=( "/home/arkasarkar/Desktop/project/%s/%s" %(current_name,str(database_array[i][1][j])))
					name=current_name
			except:
				pass
	return name
	# matched_array.append(temp)
# print(temp)

# print(name)

def content(flower_name):
	os.chdir("/home/arkasarkar/Desktop/project")
	# file.open("/home/arkasarkar/Desktop/project/%s.txt" %(name))
	with open("/home/arkasarkar/Desktop/project/%s.txt" %(flower_name)) as f:
		content = f.readlines()
	content  = [x.strip() for x in content]
	return content

	# print(content)
# for i in content:
# 	print(i)
# print(os.getcwd())



# sys.exit(s.exec_())

# s=get_name("/home/arkasarkar/Desktop/project/7.jpeg")
# print(s)