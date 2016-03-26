import pyqrcode
import random
import string
rand1='entrance'
for x in range (1,100):
	rand2 = str(x)+''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(30))
	url = pyqrcode.create("web.lasactf.com:63017/" + rand2 + '.svg')
	url.svg(rand1+'.svg', scale = 10, background = "white")
	rand1 = rand2
url = pyqrcode.create("your flag is: 'lasactf{a_long_tw1sted_maz3}'")
url.svg(rand2+'.svg', scale = 10, background = "white")
