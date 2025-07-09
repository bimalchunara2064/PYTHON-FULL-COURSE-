import csv
fp=open("emp.csv",'r')
emp_scv_obj=csv.reader(fp)
for emp_list in (emp_csv_obj)[1:]:
    print(emp_list[1])