# Problem Code :    RECNDSTR
# Sample Input:
# 4
# a
# ab
# abcd
# aaaaa

# Sample Output:
# YES
# YES
# NO
# YES


# Explanation:
# -->In this problem you have to perform two operation Left shift(in this first character will transfer to the last).
#   second is Right Shift(in this last character will shift to the first)
# --> and then we have to compare both character if  both content are equal then print "YES" else print "No"

# ===============================Code===========================================

t=int(input())
for val in range(t):
	val=input()
	L=val[1:]+val[0]
	S=val[-1]+val[:-1]
	if(L==S) and len(L)==len(S):
		print("YES")
	else:
		print("NO")
