from random import SystemRandom
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ޛ=ord
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱=chr
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𡘁=range
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ=list
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈纾=open
import re
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𓀐=re.compile
def 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𩝊(l,n):
 return l[n:]+l[:n]
def 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞠖(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐠲,묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶗ,묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓,묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜,묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫,묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞡳):
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ڜ=0
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐳍=0
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𣾯=""
 for 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐲮 in 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐠲:
  묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ڜ+=1
  묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐳍+=1
  묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𩝊(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓,1)
  if 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ڜ>26:
   묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ڜ=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ڜ%26
   묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𩝊(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜,1)
  if 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐳍>676:
   묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐳍=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐳍%676
   묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𩝊(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫,1)
  묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﲤ=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶗ[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ޛ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐲮)-65]
  묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٹ=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ޛ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ޛ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ޛ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﲤ)-65])-65])-65]
  묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𫩦=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓.index(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜.index(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫.index(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞡳[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ޛ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٹ)-65])+65))+65))+65)
  묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𣾯+=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶗ.index(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𫩦)+65)
 return 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𣾯
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐪚=SystemRandom()
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ=[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱(x)for x in 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𡘁(65,91)]
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶗ=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐪚.shuffle(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶗ)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐪚.shuffle(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐪚.shuffle(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐪚.shuffle(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞡳=[""]*26
for 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢦂 in 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𡘁(0,26):
 if not 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞡳[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢦂]=="":
  continue
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ.remove(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢦂+65))
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𧀁=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐪚.choice(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ)
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞡳[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢦂]=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𧀁
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞡳[묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ޛ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𧀁)-65]=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢾱(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢦂+65)
 묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﻢ.remove(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𧀁)
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ち=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈纾('plaintext.txt','r')
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐠲=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ち.read()
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﺣ=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𓀐('[^a-zA-Z]')
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐠲=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﺣ.sub('',묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐠲.upper())
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𣾯=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞠖(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𐠲,묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶗ),묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𢐓),묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𦲜),묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈蠫),묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ٲ(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𞡳))
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶥ=묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈纾('hard.txt','w')
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶥ.truncate()
묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈ﶥ.write(묏𦦋𐠕쁼ﾒﴧ液𐤢𐢈𣾯)
