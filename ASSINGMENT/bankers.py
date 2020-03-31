avail_instance	= []	
alloc_matrix =	[]	
max_matrix = []	
need_matrix = []	
finished_processes = []	
m = int(input("Enter the number of resources: "))	
n = int(input("Enter the number	of	processes: "))	

print()	

for i in range(m):	
	x = int(input(f"Enter the availabe size for resource -	{str(chr(i+65))}:"))	
	avail_instance.append(x)	
print("\nAllocation matrix")	
for pi in range(n):	
	print(f"For Process - P{pi}")	
	row = []	
	for ri	in range(m):	
		x = int(input(f"Enter the allocation size for resource - {str(chr(ri+65))}: "))	
		row.append(x)	
		alloc_matrix.append(row)		
print("\nMax matrix")	
for pi in range(n):	
	print(f"For Process - P{pi}")	
	row = []	
	for ri in range(m):	
		x = int(input(f"Enter the max size for	resource - {str(chr(ri+65))}:"))	
		row.append(x)	
		max_matrix.append(row)	
for pi in range(n):	
	row = []	
	for ri	in range(m):	
		row.append(max_matrix[pi][ri]-allocation_matrix[pi][ri])	
		need_matrix.append(row)	
for pi in range(n):	
	for ri in range(m):	
		if need_matrix[pi][ri]	> avail_instance[ri]:	
			break		
		else:	
			finished_processes.append(pi)		
			avail_instance = [sum(i) for i in zip(avail_instance,	alloc_matrix[pi])]	
for pi in range(n):	
	if pi not in finished_processes:	
		for ri in range(m):	
			if need_matrix[pi][ri]	> avail_instance[ri]:	
				print("System is not in	safe state.")	
				exit(0)	
			else:	
				finished_processes.append(pi)	
				available_instance = [sum(i) for i in zip(avail_instance,alloc_matrix[pi])]	
				print("\nSystem	is in safe state. Safe sequence is:")	
for fp in finished_processes:	
	print(fp, end="	")	
print()	

OUTPUT:
Enter the number of resources: 4
Enter the number of processes: 5
Enter the availabe size for resource
- A: 3
Enter the availabe size for resource
- B: 2
Enter the availabe size for resource
- C: 1
Enter the availabe size for resource
- D: 1
Allocation matrix
For Process - P0
Enter the allocation size for resource
- A: 4
Enter the allocation size for resource
- B: 0
Enter the allocation size for resource
- C: 0
Enter the allocation size for resource
- D: 1
For Process - P1
Enter the allocation size for resource
- A: 1
Enter the allocation size for resource
- B: 1
Enter the allocation size for resource
- C: 0
Enter the allocation size for resource
- D: 0
For Process - P2
Enter the allocation size for resource
- A: 1
Enter the allocation size for resource
- B: 2
Enter the allocation size for resource
- C: 5
Enter the allocation size for resource
- D: 4
For Process - P3
Enter the allocation size for resource
- A: 0
Enter the allocation size for resource
- B: 6
Enter the allocation size for resource
- C: 3
Enter the allocation size for resource
- D: 3
For Process - P4
Enter the allocation size for resource
- A: 0
Enter the allocation size for resource
- B: 2
Enter the allocation size for resource
- C: 1
Enter the allocation size for resource
- D: 2
Max matrix
For Process - P0
Enter the max size for resource -
A: 6
Enter the max size for resource -
B: 0
Enter the max size for resource -
C: 1
Enter the max size for resource -
D: 2
For Process - P1 
Enter the max size for resource -
A: 2
Enter the max size for resource -
B: 7
Enter the max size for resource -
C: 5
Enter the max size for resource -
D: 0
For Process - P2
Enter the max size for resource -
A: 2
Enter the max size for resource -
B: 3
Enter the max size for resource -
C: 5
Enter the max size for resource -
D: 6
For Process - P3
Enter the max size for resource -
A: 1
Enter the max size for resource -
B: 6
Enter the max size for resource -
C: 5
Enter the max size for resource -
D: 3
For Process - P4
Enter the max size for resource -
A: 1
Enter the max size for resource -
B: 6
Enter the max size for resource -
C: 5
Enter the max size for resource -
D: 6
System is in safe state. Safe sequence
is:
0 2 3 4 1
