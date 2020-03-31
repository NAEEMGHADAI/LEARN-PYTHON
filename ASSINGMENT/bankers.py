avail_instance	= []	
alloc_matrix =	[]	
max_matrix	= []	
need_matrix	= []	
finished_processes = []	
m =	int(input("Enter the number of resources: "))	
n =	int(input("Enter the number	of	processes: "))	

print()	
for	i in range(m):	
	x =	int(input(f"Enter the availabe	size for resource -	{str(chr(i+65))}:"))	
	avail_instance.append(x)	
print("\nAllocation	matrix")	
for	pi	in	range(n):	
	print(f"For	Process	- P{pi}")	
	row	= []	
	for	ri	in	range(m):	
		x =	int(input(f"Enter the allocation size for resource - {str(chr(ri+65))}:	"))	
		row.append(x)	
		alloc_matrix.append(row)		
print("\nMax matrix")	
for	pi in range(n):	
	print(f"For	Process	- P{pi}")	
	row	= []	
	for	ri in range(m):	
		x =	int(input(f"Enter the max size for	resource - {str(chr(ri+65))}:"))	
		row.append(x)	
		max_matrix.append(row)	
for	pi	in	range(n):	
	row	= []	
	for	ri	in	range(m):	
		row.append(max_matrix[pi][ri]-allocation_matrix[pi][ri])	
		need_matrix.append(row)	
for	pi in range(n):	
	for	ri in range(m):	
		if	need_matrix[pi][ri]	> avail_instance[ri]:	
			break		
		else:	
			finished_processes.append(pi)		
			avail_instance = [sum(i) for i in zip(avail_instance,	alloc_matrix[pi])]	
for	pi in range(n):	
	if pi not in finished_processes:	
		for	ri in range(m):	
			if	need_matrix[pi][ri]	>	avail_instance[ri]:	
				print("System	is	not	in	safe	state.")	
				exit(0)	
			else:	
				finished_processes.append(pi)	
				available_instance	=	[sum(i)	for	i in zip(avail_instance,	alloc_matrix[pi])]	
				print("\nSystem	is in safe state. Safe sequence is:")	
for	fp	in	finished_processes:	
	print(fp,	end="	")	
print()	