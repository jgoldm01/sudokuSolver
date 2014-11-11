'''li = [1,2,3];
i = 1;
if isinstance(i, list) and 2 in i:
	i.remove(2)'''

'''for j in [3,4,65,8]:
	print len(j);'''

it = iter(range(6))
for x, y, z in zip(it, it, it):
	print x, y, z, "|"

for f in range(6):
	print f,

print "\n_ _ _ _ _ _ "