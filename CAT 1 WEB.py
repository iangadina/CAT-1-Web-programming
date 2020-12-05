"""QUESTION 1"""
def csc_217_attendance():#this is the funtion for merging the two files and removing the dublicate
	file=open("CSC_217_attendance_ week1_30.txt","r")
	member_list1=file.read()
	file.close()
	file=open("CSC_217_attendance_ week1_end.txt","r")
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
def replace_b_with_B():#this is the funtion for replacing b with B before sorting so as not to elimininate some members
        file=open("CSC_217_attendance_week1.txt","r")
        f=open("t.txt","w")
        replace=[i for i in file]
        for i in replace:
                if "2019" in i:
                        s=i.split()
                        for j in s:
                                if "2019" in j:
                                        replaced=j.replace("b","B")
                                        f.write(replaced)
        file.close()
replace_b_with_B()
"""QUESTION 2"""
def csc_217_Seperated():#ths the function for sepparating the two files
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
csc_217_Seperated()#This function spaces 2019 with the name so as it can be indexed and formated
def spacingcomp():
	file=open("CSC_217_Computer.txt","r")
	spaces=[file.read()]
	for i in spaces:
		space=i.replace("-"," ")
	file=open("CSC_217_Computer.txt","w")
	for i in space:
		file.write(i)
spacingcomp()
def spacingit():
	file=open("CSC_217_IT.txt","r")
	spaces=[file.read()]
	for i in spaces:
		space=i.replace("_","")
		space=i.replace("2019","2019 ")
	file=open("CSC_217_IT.txt","w")
	for i in space:
		file.write(i)
spacingit()
"""QUESTION 3 i"""
def csc_217_Computer():#This function orders Computer in terms of admission number being the first 
	file=open("CSC_217_Computer.txt","r")
	f=open("copy.txt","w")
	formated=[i for i in file]
	for i in formated:
		if "B135" in i:
			order=i.split()
			for j in order:
				if "B135" in j:
					index=order.index(j)
					order=[order[index]]+order[:index]+order[index+1:]
		student=(" ".join(order))
		f.write(student+"\n")
	f.close()
	file.close()
	f=open("copy.txt","r")
	c=f.read()
	f.close()
	file=open("CSC_217_Computer.txt","w")
	file.write(c+"\n")
	file.close()
csc_217_Computer()
"""QUESTION 3 ii"""
def csc_217_IT():#This function orders IT in terms of admission number being the first
	file=open("CSC_217_IT.txt","r")
	f=open("copy.txt","w")
	formated=[i for i in file]
	for i in formated:
		if "B141" in i:
			order=i.split()
			for j in order:
				if "B141" in j:
					index=order.index(j)
					order=[order[index]]+order[:index]+order[index+1:]
		student=(" ".join(order))
		f.write(student+"\n")
	f.close()
	file.close()
	file=open("CSC_217_IT.txt","w")
	f=open("copy.txt","r")
	c=f.read()
	file.write(c+"\n")
csc_217_IT()
def underscoreit():
     file=open("CSC_217_IT.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace(" ","_")
     file=open("CSC_217_IT.txt","w")
     for i in under:
          file.write(i)
     file=open("CSC_217_IT.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace("__","_")
     file=open("CSC_217_IT.txt","w")
     for i in under:
          file.write(i)
     file=open("CSC_217_IT.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace("-","")
     file=open("CSC_217_IT.txt","w")
     for i in under:
          file.write(i)
     file=open("CSC_217_IT.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace("__","_")
     file=open("CSC_217_IT.txt","w")
     for i in under:
          file.write(i)
underscoreit()
def underscorecomp():
     file=open("CSC_217_Computer.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace("2019","2019 ")
     file=open("CSC_217_Computer.txt","w")
     for i in under:
          file.write(i)
     file=open("CSC_217_Computer.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace(" ","_")
     file=open("CSC_217_Computer.txt","w")
     for i in under:
          file.write(i)
     file=open("CSC_217_Computer.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace(".","")
     file=open("CSC_217_Computer.txt","w")
     for i in under:
          file.write(i)
     file=open("CSC_217_Computer.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace("-","")
     file=open("CSC_217_Computer.txt","w")
     for i in under:
          file.write(i)
     file=open("CSC_217_Computer.txt","r")
     underscore=[file.read()]
     for i in underscore:
          under=i.replace("__","_")
     file=open("CSC_217_Computer.txt","w")
     for i in under:
          file.write(i)
underscorecomp()
"""QUESTION 4"""
def CSC_217_formated():
        file=open("CSC_217_Computer.txt","r")
        underscore=[file.read()]
        for i in underscore:
                under=i.replace("2019_","2019, ")
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","w")
        for i in under:
                file.write(i)
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","r")
        underscore=[file.read()]
        for i in underscore:
                under=i.replace("2018_","2018, ")
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","w")
        for i in under:
                file.write(i)
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","r")
        underscore=[file.read()]
        for i in underscore:
                under=i.replace("2016_","2016, ")
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","w")
        for i in under:
                file.write(i)
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","r")
        underscore=[file.read()]
        for i in underscore:
                under=i.replace("_"," ")
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","w")
        for i in under:
                file.write(i)
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","r")
        underscore=[file.read()]
        for i in underscore:
                under=i.replace("17838/2019, ","17838/2019, Computer 2019")
        file.close()
        file=open("CSC_217_Computer_Week1_final.txt","w")
        for i in under:
                file.write(i)
        file.close()
        file=open("CSC_217_IT.txt","r")
        underscore=[file.read()]
        for i in underscore:
                under=i.replace("2019_","2019, ")
        file.close()
        file=open("CSC_217_IT_Week1_final.txt","w")
        for i in under:
                file.write(i)
        file.close()
        file=open("CSC_217_IT_Week1_final.txt","r")
        underscore=[file.read()]
        for i in underscore:
                under=i.replace("_"," ")
        file.close()
        file=open("CSC_217_IT_Week1_final.txt","w")
        for i in under:
                file.write(i)
        file.close()
        print(i)
CSC_217_formated()

          
          
     



