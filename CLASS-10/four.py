male_emp_names=[]
female_emp_names=[]
for emp in employees:
    if emp['gender']=='Male':
        male_emp_names.append(emp['ename']) 

    elif emp['gender'] =='Female':
        female_emp_names.append(emp['ename'])