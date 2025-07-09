enames=['rahul','basant','bikash']
def changecase(ename):
    return ename.upper()
new_names=list(map(changecase,enames))
print(enames)
print(new_names)