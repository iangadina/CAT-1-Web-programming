def csc_217_attendance():
	file=open("CSC_217_attendance_week1_30.txt","r")
	member_list1=file.read()
	file.close()
	file=open("CSC_217_attendance_week1_end.txt","r")
	member_list2=file.read()
	file.close()
	file=open("CSC_217_attendance_week1trial.txt","w")
	member_list={member_list1}.union({member_list2})
	for i in member_list:
		file.write(i)
	file.close()
	dublicate=set()
	file=open("CSC_217_attendance_week1.txt","w")
	for i in open("CSC_217_attendance_week1trial.txt","r"):
		if i not in dublicate:
			file.write(i)
			dublicate.add(i)
	file.close()
csc_217_attendance()
def csc_217_Seperated():
	file=open("CSC_217_attendance_week1.txt","r")
	Comp_members=[i for i in file if "B135" in i]
	file.close()
	file=open("CSC_217_attendance_week1.txt","r")
	IT_members=[j for j in file if "B141" in j]
	file.close()
	file=open("CSC_217_Computer.txt","w")
	for i in Comp_members:
		file.write(i)
	file.close()
	file=open("CSC_217_IT.txt","w")
	for i in IT_members:
		file.write(i)
	file.close()
csc_217_Seperated()

