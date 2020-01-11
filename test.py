import os 

def get_names():
	list1=os.listdir()
	# print(list1)
	list2=[]
	for i in range(len(list1)):
		if list1[i].find("py")==-1:
			list2.append(list1[i])
	return list2
# print(list2)
def get_images(name):

	os.chdir('/home/arkasarkar/Desktop/project/%s' %(name))
	# print(os.getcwd())
	return(os.listdir())

