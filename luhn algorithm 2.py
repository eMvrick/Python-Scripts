"""
Python script to check the validity of credit card numbers

"""

def luhn(n):
        # reverse the credit card number
	r = [int(ch) for ch in str(n)][::-1]
        # double every second digit	
	return (sum(r[0::2]) + sum(sum(divmod(d*2,10))
       # return True or False
       for d in r[1::2])) % 10 == 0
 
for n in (4137894711755904,6499802450273568 , 8504172191273888 , 0043668783485480 ):
print(n, luhn(n))
