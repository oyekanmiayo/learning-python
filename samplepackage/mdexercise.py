import urllib

func_list = dir(urllib)
print(func_list)
mylist = []

for func in func_list:
    if("pa" in func):
        mylist.append(func)

mylist.sort(reverse = True)
print(mylist)ls 