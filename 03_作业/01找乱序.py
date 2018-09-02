import time
import random
listt=[]
def numberx():
	global listt
	while True:
		num=random.randint(1,100)
		if len(listt)==10:
			print('添加完成')
			print('----------')
			break
		if num in listt:
			continue
		listt.append(num)

	print(listt)
	makeup=listt[7]
	print('标记7是%d\n重新排序'%makeup)
	listt.sort()
	print(listt)
	for inx,val in enumerate(listt):
		if makeup==val:
			print('索引是%d'%inx)
			print('数字是%d'%val)
			break

numberx()