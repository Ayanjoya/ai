import time
def start():
	print("(1.add/2.sub/3.mul/4.exit)")
	a=input("(1./2./3./4.) ")

	def suma():
		sum1 = input("1NUMBER: ")
		sum2 = input("2NUMBER: ")
		a1 = int(sum1)+int(sum2)
		print (sum1,"+",sum2,"=",a1)

	def sub():
		sub1 = input("1NUMBER: ")
		sub2 = input("2NUMBER: ")
		a2 = int(sub1)-int(sub2)
		print (sub1,"-",sub2,"=",a2)

	def mul():
		mul1 = input("1NUMBER: ")
		mul2 = input("2NUMBER: ")
		a3 = int(mul1)*int(mul2)
		print (mul1,"X",mul2,"=",a3)


	if a == "1":
		suma()
	elif a == "2":
		sub()
	elif a == "3":
		mul()
	elif a == "4":
		print("GOOD BYE...")
		quit()
	else:
		print("ERROR COMMAND")
		time.sleep(2)
