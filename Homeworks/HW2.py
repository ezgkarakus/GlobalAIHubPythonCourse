cv1= {"Name":"Özge", "Surname":"Dincer", "Age":"19", "Job":"Information Systems  Engineer",
"Mail":"ozgedincer@hotmail.com", "Education":"Mugla Sitki Kocman Univertiy"}
cv2= {"Name":"Sude", "Surname":"Ensici", "Age":"20", "Job":"Teacher",
"Mail":"sudensici@hotmail.com", "Education":"Istanbul University"}
cv3= {"Name":"Hicran", "Surname":"Kirazli", "Age":"21", "Job":"Textile Engineer",
"Mail":"hicrankirazli@hotmail.com", "Education":"Istanbul Technical University"}
cv4= {"Name":"İremnur", "Surname":"Çiv", "Age":"22", "Job":"Midwife",
"Mail":"iremnurciv@hotmail.com", "Education":"Kocaeli Univertiy"}
cv5= {"Name":"Sema", "Surname":"Arslan", "Age":"23", "Job":"Dentist",
"Mail":"semaarslan@hotmail.com", "Education":"Hacettepe University"}
cvlist=[cv1,cv2,cv3,cv4,cv5]
i = 1
for cv in cvlist:
    print("********** CV-", i, "**********")
    i = i + 1
    for j, k in cv.items():
        print(j, ":", k)
