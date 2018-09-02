def print_yangtuo():
	print('       ')
	print('┆     　┏┓　　┏┓             ┆')
	print('┆      ┏┛┻━━━┛  ┻┓           ┆')
	print('┆     ┃　　　　   ┃          ┆')
	print('┆    ┃　 　 ━　    ┃         ┆')
	print('┆    ┃  ┳┛ 　┗┳　  ┃         ┆')
	print('┆    ┃　　　　　   ┃         ┆')
	print('┆     ┃　　┻　    ┃          ┆')
	print('┆     ┗━┓　马  ┏━┛           ┆')
	print('┆  　  　┃　勒 ┃             ┆')
	print('┆  　  　┃　 戈　┗━━━━━┓     ┆')
	print('┆   　  ┃　壁　　　　 　┣┓   ┆')
	print('┆   　　┃　 的 羊 驼 　┏┛    ┆')
	print('┆   　 　┗┓ ┓┏━┳┓ ━┳ ┏┛      ┆')
	print('┆   　 　　 ┃┫┫　  ┃┫┫       ┆')
	print('┆   　 　　 ┗┻┛　  ┗┻┛       ┆')
	print('┆    神兽镇楼   工程不挂     ┆')
	print('别看我只是一只羊，')
	print('       羊儿的聪明难以想象。 ')
	print('           ----尼古拉斯.老羊 ')	
	print('       ')
	print('小小编程写字间 ，马勒戈壁大草原')
	print('')
	print('老板督促写工程 ，客户又让改文件')
	print('')
	print('要问心中多少愁 ？万千羊驼在奔腾')
	print('')
	print('日月交替再明天 ，心无情系身无钱')
	print('')
	print('')

import random
import time

def exit():
	print('E x i t :  退  出'.center(30,' '))
	a = input('yes/no')
	if   a=='yes':
		print('已退出')
		return True
	elif a=='no':
		print('返回')
	
def login():
	name_1 = input('输入用户名')
	flag = 0
	for i in mp:
		if  name_1 == i['name']:
			flag = 1
			ps = input('输入密码')
			if ps == i['pswd']:
				print('登陆成功')
				print(i['ailic'])
				return  True
		elif flag == 0:
			print('未存在')
			continue
#名片账号密码管理系统框架(增)(删)(改)(查)

def ad():			#增
	inn= {}
	name = input('输入新的用户名(手机号)')
	ps_1 = input('输入您的密码')
	ps_2 = input('再次输入密码')
	pc   = random.randint(1000,9999)
	print('验证码为:%d'%pc)
	pc_1 = int(input('输入验证码:'))
	if len(name) == 11 and name.startswith('1') and ps_1 == ps_2 and len(ps_1) >=6 and len(ps_1)<=12 and pc_1 == pc:
		ailic = input('输入昵称')
		inn['name']=name
		inn['pswd']=ps_1
		inn['ailic']=ailic
		mp.append(inn)
		print('注册成功')
	else:
		print('输入错误，再来')
def fd():			#查
	name_1 = input('输入查看的用户名')
	flag = 0
	for i in mp:
		if  name_1 == i['name']:
			flag = 1
			print('已存在')
			print(i['ailic'])
		elif flag == 0:
			print('未存在')
def de():			#删
	name_1 = input('输入删除的用户名(手机号)')
	flag = 0
	for i in mp:
		if  name_1 == i['name']:
			flag ==1
			ps_1 = input('输入您的密码')
			pc   = random.randint(1000,9999)
			print('验证码为:%d'%pc)
			pc_1 = int(input('输入验证码:'))
			if  ps_1 == i['pswd'] and pc_1 == pc:
				i.clear()
				print('删除成功')
			else:
				print('删除失败')
	if flag ==0:
		print('查无此人')
def ch():			#改
	name_1 = input('输入更改的用户名(手机号)')
	flag =0
	for i in mp:
		if  name_1 == i['name']:
			flag =1
			ps_1 = input('输入您的密码')
			pc   = random.randint(1000,9999)
			print('验证码为:%d'%pc)
			pc_1 = int(input('输入验证码:'))
			if  ps_1 == i['pswd'] and pc_1 == pc:
				ch = int(input('1.更改密码2.更改昵称'))
				if ch == 1 :
					new_p1 = input('新密码')
					new_p2 = input('确认新密码')
					if new_p1 == new_p2 and len(new_n1)>=6 and len(new_n1)<=12:
						i['pswd']=new_p1
				elif ch == 2 :
					new_n1 = input('新昵称')
					i['ailic']=new_n1
				print('更改成功')
			else:
				print('更改失败')
	if flag ==0:
		print('查无此人')
def card():
	while True:
		a = input('1.添加账户\n2.查找账户\n3.删除账户\n4.更改账户\n5.退出')
		if int(a)==1:
			ad()
		elif int(a)==2:
			fd()
		elif int(a)==3:
			de()
		elif int(a)==4:
			ch()
		elif int(a)==5:
			exit()
			if True:
				break
			else:
				continue
#游戏系统框架
def cq():			#猜拳
	while True:
		jj = int(input('1.进入游戏2.退出游戏'))
		if jj==1:
			pc = random.randint(1,3)
			a =int(input('1.石头2.剪刀3.布'))
			if (pc==1 and a==2) or (pc==2 and a==3)or (pc==3 and a==1):
				print('输了')
			elif pc==a :
				print('平局')
			else:
				print('胜利')
		if jj==2:
			break
def cn(): 			#猜数
	while True:
		jj = int(input('1.进入游戏2.退出游戏'))
		if jj==1:
			pc =random.randint(0,100)
			min= 0
			max= 100
			flag = 0
			for i in range(0,10):
				guess = input('输入你猜的数字')
				if int(guess) > pc :
					max = guess
					print('大了')
					print(min,'~',max)
				elif int(guess) < pc:
					min = guess
					print('小了')
					print(min,'~',max)
				elif int(guess) == pc:
					flag=1
					print('大吉大利，深夜吃鸡')	
					if i<=3 and flag ==1:
						print('想与大神生猴子')
					elif i<=8 and i>3 and flag ==1:
						print('哼，╭(╯^╰)╮，凡人')
					elif i<=10 and i>8 and flag ==1:
						print('渣渣，小圈♂圈锤♂死♀你')
					break
				else:
					print('输入有误')
					print('本次计算在内')
				if i ==9:
					print('渣渣，这都猜不对，看到门了么？')
		if jj==2:
			break
def zx():			#真心话
	while True:
		a = input('输入需要的操作1.确定进入2.退出')
		if int(a)==1:
			tii = 0.1
			tio = 0.6
			for  i in range(1,7):
				pc = random.randint(1,6)
				print(pc)
				pc_1 = random.randint(1,6)
				time.sleep(tii)
				tii+=0.3
				print(pc_1)
				print('-'*10)
			ta = pc*pc_1
			print('她的总数:%d'%ta)
			time.sleep(tio)
			for  i in range(1,8):
				pc_2 = random.randint(1,6)
				print(pc_2)
				pc_3 = random.randint(1,6)
				time.sleep(tio)
				tio+=0.2
				print(pc_3)
				print('-'*10)
			me = pc_2*pc_3
			print('我的总数:%d'%me)
			if me <ta:
				print('输了')
				b = input('1.真心话2.大冒险')
				if int(b) ==1:
					do =random.randint(1,5)
					if do ==1:
						print('你喜欢什么颜色')
					elif do==2:
						print('你喜欢什么食物')
					elif do==3:
						print('你喜欢谁的歌')
					elif do==4:
						print('你喜欢我么')
					elif do==5:
						print('想和我一起去天池玩么？')
				elif int(b) ==2:
					do =random.randint(1,6)
					if do ==1:
						print('做一个俯卧撑')
					elif do==2:
						print('一口把一小袋薯片吃完')
					elif do==3:
						print('给我唱首歌或者写首诗')
					elif do==4:
						print('把我的头发吹起来5秒')
					elif do==5:
						print('亲我一口')
					elif do==6:
						print('说喜欢我')
					else:
						pass
			elif ta == me:
				print('平局是一种缘分')
			elif ta < me:
				print('赢了')
			else:
				print('输入有误')
				pass
		elif int(a)==2:
			break
		else:
			print('输入有误')
			continue
def ss():			#计算素数
	pass
def es():			#二十四点
	while True:
		a = input('输入需要的操作1.确定进入2.退出')
		if int(a)==1:
			l =[]
			for  i in range(4):
				ran =random.randint(1,13)
				l.append(ran)
			print(l)
			print('功能不会自己手算。。')
		elif int(a)==2:
			break	
def gam():
	while True:
		g = input('输入要进入的游戏\n1.猜拳\n2.猜数\n3.真心话大冒险\n4.计算素数\n5.二十四点\n6.退出系统')
		if   int(g)==1:
			cq()
		elif int(g)==2:
			cn()
		elif int(g)==3:
			zx()
		elif int(g)==4:
			ss()
		elif int(g)==5:
			es()
		elif int(g)==6:
			break
		else:
			pass
'''
#商品管理系统

def fz():			#买卖房子
def hc():			#车购买
def tb():			#杂货购买

def sp():			#商品管理
'''

#小工具

def jsq():			#计算器
	while True:
		js=input('1.开始计算2.退出')
		if int(js)==1:
			aaal =0
			while True:
				print('现在总值为%.02f'%float(aaal))
				sf=input('输入算法')
				if sf=='=':
					print('结果为%.02f'%float(aaal))
					break
				aal=float(input('输入值'))
				if sf=='+':
					aaal+=aal
				elif sf=='-':
					aaal-=aal
				elif sf=='*':
					aaal*=aal
				elif sf=='/':
					if aal ==0:
						print('错误')
						break
					else:
						aaal/=aal
				else:
					print('无效输入')
					pass
		elif int(js)==2:
			print('已退出')
			break
		else:
			pass
jsq()
vudio =[]
def lyj():			#录音机
	vv = input('1.开始录音2.退出系统')
	if  vv ==1:
		while True:
			vvv = input('1.终止录音2.暂停录音')
			flag=0
			if vvv==1:
				fi = input('输入需要添加的文件名')
				vudio.append(fi)


	elif vv ==2:
		print('退出录音')
		break
	else:
		print('输入错误')
		pass



def snf():			#算今年到今日共多少天

def litool():		#小工具
	li = input('1.计算器2.计算器')
	if int(li)==1:
		jsq()
	elif int(li)==2:
		lyj()
	else:
		pass
def main_l():
	while True:
		a = input('1.添加账户2.卡片管理3.游戏系统4.小工具5.退出')
		if int(a)==1 :
			ad()
		elif int(a)==2 :
			card()
		elif int(a)==3 :
			gam()
		elif int(a)==4 :
			litool()
		elif int(a)==5 :
			exit()
			if True:
				break
			else:
				pass
		else:
			print('输入有误')
			pass

def main_s():	#总系统
	cc = 0
	while True:
		print('您已进入'.center(30,'-'))
		print(' ')
		print(' ')
		print('..源池..'.center(30,' '))
		print(' ')
		print(' ')
		print('1.注册账号'.center(30,'-'))
		print('2.登录账号'.center(30,'-'))
		print('3.退出系统'.center(30,'-'))
		print(' ')
		hh =input('输入操作')
		print(' ')
		print('     '.center(30,'-'))
		if   int(hh) == 1:
			ad()
		elif int(hh) == 2:
			login()
			if  True:
				main_l()
				cc = 0
			else:
				print('登录失败')
				cc+=1
			if cc==3:
				print('已经输入3次，默认退出')
				break
			else:
				pass
		elif int(hh) == 3:
			exit()
			if True:
				break
			else:
				pass
		else:
			pass

mp = []

main_s()
'''