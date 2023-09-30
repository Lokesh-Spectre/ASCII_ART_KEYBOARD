data={
'height':5,
'width':7,
"A":
r'''
 //A\\ 
||   ||
||===||
||   ||
||   ||
''',
"B":
'''
|----< 
|     >
B----< 
|     >
|----< 
''',
"C":
r'''
  #####
 #     
#      
 #     
  #####
''',
"D":
r'''
||:::\\
||   ||
|| D ||
||   ||
||::://
''',
"E":
r'''
//=====
||     
|E===  
||     
\\=====
''',
"F":
'''
//*====
||     
|F*====
||     
||     
''',
"G":
r'''
 //==\\
||     
|| G###
||   ||
 \\==//
''',
"H":
'''
__   __
||   ||
||=H=||
||   ||
^^   ^^
''',
"I"
:r'''
=======
  \|/  
   I   
  /|\  
=======
''',
"J":
'''
@@@J@@@
   @   
   @   
   @   
@@@@   
''',
"K":
r'''
#    % 
#  %   
#K     
# \\   
#   \\ 
''',
"L":
'''
#      
#      
#      
#      
L######
''',
"M":
'''
##   ##
# # # #
#  M  #
#     #
#     #
''',
"N":
'''
##    #
# #   #
#  N  #
#   # #
#    ##
''',
"O":
'''
 ##O## 
#     #
#     #
#     #
 ##### 
''',
"P":
'''
P##### 
#     #
###### 
#      
#      
''',
"Q":
r'''
 ##Q## 
#     #
#  \  #
 ###\# 
     \ 
''',
"R":
'''
/##### 
#     #
##R### 
#  #   
#    # 
''',
"S":
r'''
//===\ 
\\    |
  \S\  
|    \\
 \===//
''',
"T":
'''
###T###
   #   
   #   
   #   
   #   
''',
"U":
'''
#     #
#     #
#     #
#     #
 ##U## 
''',
"V":
'''
_     _
#     #
 #   # 
  # #  
   #   
''',
'W':
'''
#     #
#     #
#  #  #
#  #  #
 ##### 
''',
'X':
'''
#     #
 #   # 
  |#|  
 #   # 
#     #
''',
'Y':
'''
#     #
 #   # 
  # #  
   #   
   #   
''',
'Z':
'''
#######
     # 
   #   
 #     
#######
''',
" ":'\n'.join(['     ' for x in range(5)])
}

def checker(data=data):
    h=data['height']
    w=data['width']
    del data['height'],data['width']
    f=False
    for i in data:
        if i==' ':
            continue
        a=data[i].strip('\n')
        linecheck=[len(x)==w for x in a.split('\n')]
        if not (all(linecheck) and len(linecheck)==h):
            print(a)
            print('h:',len(linecheck))
            print('w',linecheck)
            f=True
    
    if not f:
        print(f"\n{'*'*5}completed...dimensions r perfect!{'*'*5}")
    else:
        exit()
def add(a,b):
    a=a.split('\n')
    b=b.split('\n')
    obj=map(lambda x,y:x+y,a,b)
    return '\n'.join(list(obj))
def addspace(n=1):
    for i in data:
        data[i]=add(data[i],(' '*n+'\n')*5)
def listize():
    for i in data:
        data[i]=data[i].split('\n')

def justDoIt(string):
    string=string.upper()
    out=['' for x in range(5)]
    for i in string:
        for k in range(5): 
            out[k]+=data[i][k]
            
    return '\n'.join(out)

def shell():
    while True:
        print(exec(input('>>>')))

def getdata():
    global data
    data=dict([ (x,data[x])if x in ['height','width'] else (x,[j+' ' for j in data[x].strip('\n').split('\n')]) for x in data])
    return data

# getdata()
# print(justDoIt('up and runiing'))
# use keyboard module and 'up' & 'down' to navigate
