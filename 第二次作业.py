file=open('xx.gv','w')
file.write('digraph G{ \n')
D=[
        [1,1,2],
	    [2,2,3],
		[3,3,4],
		[4,4,5],
		[5,1,8],
		[6,8,7],
        [7,7,6],
		[8,6,5],
		[9,2,8],
		[10,3,7],
		[11,4,6]
]
for d in D :
      file.write('%d->%d;\n' % (d[1] , d[2]))
file.write("}")