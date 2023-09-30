from ascii_art_chars import getdata
from pynput import keyboard as kb
import pyperclip
import os

###T### __   __ ======= //===\        P#####  /#####   ##O##   //==\\ /#####   //A\\  ##   ##       ###T### #     # P#####  //===== //===\         //A\\  //===\    ##### ======= =======        //A\\  /#####  ###T### 
   #    ||   ||   \|/   \\    |       #     # #     # #     # ||      #     # ||   || # # # #          #     #   #  #     # ||      \\    |       ||   || \\    |  #        \|/     \|/         ||   || #     #    #    
   #    ||=H=||    I      \S\         ######  ##R###  #     # || G### ##R###  ||===|| #  M  #          #      # #   ######  |E===     \S\         ||===||   \S\   #          I       I          ||===|| ##R###     #    
   #    ||   ||   /|\   |    \\       #       #  #    #     # ||   || #  #    ||   || #     #          #       #    #       ||      |    \\       ||   || |    \\  #        /|\     /|\         ||   || #  #       #    
   #    ^^   ^^ =======  \===//       #       #    #   #####   \\==// #    #  ||   || #     #          #       #    #       \\=====  \===//       ||   ||  \===//   ##### ======= =======       ||   || #    #     #    
# You  need type slow for it to work properly
# use '`' character to get into and out of ascii art mode

os.system('cls')
data=getdata()
def renderChar(key):
	out=list()
	for i in data[key.upper()]:
		out+=[i]
	return '\n'.join(out)
ctrl=kb.Controller()
count=0
c=0
ignore=0
last=0
ignore_stack=[]
def artify(key):
	global c,lock,ignore
	lock=True
	try:
		if key.char=='`':
			ctrl.tap(kb.Key.backspace)
			lock=True
			print('Normal Mode')
			return
		if 'z' >= key.char >= 'a':
			
			ctrl.tap(kb.Key.backspace)
			ignore+=1
			if not c:
				out=renderChar(key.char)
				ctrl.type(out)
				ignore+=len(out)

				c=1
			else:
				out=renderChar(key.char)
				print(out)
				[ctrl.tap(kb.Key.up) for x in range(4)]
				ignore+=len(out)+4
				out=out.split('\n')
				ctrl.type(out[0])
				for i in out[1:]:
					ctrl.tap(kb.Key.down)
					ctrl.type(i)
					
					
				
	except AttributeError:
		if key==kb.Key.space:
			out=renderChar(' ')
			ctrl.tap(kb.Key.backspace)
			ignore+=1
			[ctrl.tap(kb.Key.up) for x in range(4)]
			ignore+=len(out)+4
			out=out.split('\n')
			ctrl.type(out[0])
			for i in out[1:]:
				ctrl.tap(kb.Key.down)
				ctrl.type(i)
				
		elif key== kb.Key.esc:
			listner.stop()
		elif key == kb.Key.backspace:
			[ctrl.tap(kb.Key.backspace) for i in range(7)]
			ignore+=7
			for i in range(4):
				if last == kb.Key.backspace:
					ctrl.tap(kb.Key.down)
				else:
					ctrl.tap(kb.Key.up)
				[ctrl.tap(kb.Key.delete) for i in range(8)]
				ignore+=9
			[ctrl.tap(kb.Key.down) for x in range(4)]
			ignore+=4
	lock=False
lock=False
def onpress(key):
	global lock,ignore,count
	if lock:
		try:
			if key.char=='`':
				ctrl.tap(kb.Key.backspace)
				ignore+=1
				lock = False
				print('ASCII ART Mode')
		except:
			pass
		return
	else:
		if count >100:
			exit()
		# try: # degugging code
		# 	print(ignore,key.char)
		# except AttributeError:
		# 	print(ignore,key)
		if ignore!=0:
			ignore-=1
			return
		last=key
		artify(key)
listner=kb.Listener(on_press=onpress)
listner.start()
#while True:
#	pass
listner.join()

# write a one time fucntion to check the data set and enter number of keystrokes it takes