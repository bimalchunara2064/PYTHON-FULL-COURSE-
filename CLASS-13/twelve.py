a=None 
fp=None
try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    
    print("Your Numbers are",a,":",b)
    print(a/b)
    
    fp=open("emp.txt")

except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(a/1)

except FileNotFoundError as err:
    print("File Nout Found Please check")
except:
    pass