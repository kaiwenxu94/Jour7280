r = 0.05 / 12
n = 20 * 12
P = 10000000
A = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
print(A)
outstanding = P
m = 0

print('Month\tInstalment\tInterest\tPrincipal\tOutstanding')
while m>=0:
	m=m+1
	interest_in_instalment = r * outstanding
	principal_in_instalment = A - interest_in_instalment
	outstanding = outstanding - principal_in_instalment
	print('{0:03d}\t{1}\t{2}\t{3}\t{4}'.format(m,A,interest_in_instalment,principal_in_instalment,outstanding))
	if outstanding <=0:
		break

