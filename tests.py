'''li = [1,2,3];
i = 1;
if isinstance(i, list) and 2 in i:
	i.remove(2)'''

'''for j in [3,4,65,8]:
	print len(j);'''


def test():
	global num 
	num = 3
	ln = list([num])
	print ln

global num
test()
print num