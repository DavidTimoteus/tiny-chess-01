import os,json as J,urllib.request as W
V=(0,100,320,330,500,900,0);MT=30000
N=(33,31,18,14,-14,-18,-31,-33);D=(17,15,-15,-17);S=(16,-16,1,-1);T=D+S
P='KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEGIIIIKKKIKLMILLMIKMMIMMMILKKGIIIKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLGIIJIKKKIKLLJKLLKKLLILLLIKKKGIIJECCAECCAECCAECCAGEECIGGGOOKKOQMK'
R={4:12,7:14,0:13,116:3,119:11,112:7}
A=[0]*128;TN=1;CR=0;EP=-1;e=0;K_=[0,0];j=[];k=0;l=0
def w(p,s):
 a=abs(p);r=s>>4;f=min(s&7,7-(s&7));i=(a-1)*32+((7-r if p>0 else r)*4+f);v=V[a]+5*(ord(P[i])-75)
 return v*p//a
def x(q,z):
 for O,V in (((-15*z,-17*z),1),(N,2),(T,6)):
  if any(not (q+d)&136 and A[q+d]==V*z for d in O):return 1
 for O,U,V in ((D,3,5),(S,4,5)):
  for d in O:
   t=q+d
   while not t&136:
    p=A[t]
    if p==U*z or p==V*z:return 1
    if p:break
    t+=d
 return 0
def y():
 for q in range(128):
  if q&136:continue
  p=A[q]
  if not p or (p>0)!=(TN>0):continue
  a=abs(p)
  if a==1:
   o=q+16*TN
   T_=[o] if not o&136 and A[o]==0 else []
   if T_ and (q>>4)==(7-5*TN)//2 and A[q+32*TN]==0:T_+=[q+32*TN]
   T_+=[t for t in (q+15*TN,q+17*TN) if not t&136 and (A[t] and (A[t]>0)!=(TN>0) or t==EP)]
   for t in T_:yield from (q|t<<7|r<<14 for r in ((5,4,3,2) if t>>4 in (0,7) else (0,)))
  else:
   for u in (N,D,S,T,T)[a-2]:
    t=q+u
    while 1:
     if t&136:break
     if not A[t] or (A[t]>0)!=(TN>0):yield q|t<<7
     if A[t] or a in (2,6):break
     t+=u
 K0=60-56*TN
 for D_ in (2,-2):
  E_=K0+D_
  if CR>>((TN<0)*2+(D_<0))&1 and all(not A[K0+i]for i in((1,2)if D_>0 else(-1,-2,-3))) and not any(x(s,-TN)for s in(K0,K0+D_//2,E_)):yield K0|E_<<7
def M(m):
 global TN,CR,EP,e,K_
 a=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=A[a];s=TN
 cs=t-16*s*(abs(p)==1 and t==EP and A[t]==0);cap=A[cs]
 j.append((m,cap,cs,CR,EP,e,list(K_)));A[a]=0
 if cap:e-=w(cap,cs);A[cs]=0
 np=pr*s if pr else p;e+=w(np,t)-w(p,a);A[t]=np
 if abs(p)==6:
  K_[s>0]=t
  if abs(t-a)==2:
   rf,rt=(t+1,t-1) if t>a else (t-2,t+1);r=A[rf];A[rf]=0;A[rt]=r
 CR&=R.get(a,15)&R.get(t,15);EP=(a+t)//2 if abs(p)==1 and abs(t-a)==32 else -1;TN=-s
 if x(K_[s>0],TN):U();return 0
 return 1
def U():
 global TN,CR,EP,e,K_
 m,cap,cs,CR,EP,e,K_=j.pop();a=m&127;t=(m>>7)&127;pr=(m>>14)&7;v=A[t]
 if pr:v=v//abs(v)
 A[a]=v;A[t]=0
 if cap:A[cs]=cap
 if abs(v)==6 and abs(t-a)==2:
  rf,rt=(t+1,t-1) if t>a else (t-2,t+1);A[rf]=A[rt];A[rt]=0
 TN=-TN
def O(L):
 return sorted(L,key=lambda m:-(10*V[abs(A[t])or 1]-V[abs(A[m&127])]//10+900*((m>>14)&7==5)) if A[t:=(m>>7)&127] or (m>>14)&7 or t==EP else 0)
def s(d,a,b,c):
 global k,l
 if c>=63:return e*TN
 k+=1
 if k>=60000:l=1;return 0
 C=x(K_[TN>0],-TN);d+=C
 if d<=0:
  v=e*TN
  if v>=b:return b
  if v>a:a=v
  L=[m for m in y() if A[t:=(m>>7)&127] or ((m>>14)&7) or t==EP]
 else:L=y()
 v1=-MT;h=0
 for m in O(L):
  if not M(m):continue
  h+=1;s2=-s(d-1 if d>0 else 0,-b,-a,c+1);U()
  if l:return 0
  if s2>v1:v1=s2
  if s2>a:a=s2
  if a>=b:break
 if h==0 and d>0:return(-MT+c)*C
 return a if d<=0 else v1
def t(L=None):
 global k,l
 G1=[m for m in y() if M(m) and (U() or 1)] if L is None else [v(H) for H in L]
 if not G1:return ''
 k=0;l=0;B1=G1[0];B2=-MT
 for m in O(G1):
  if not M(m):continue
  S2=-s(2,-MT,-B2,1);U()
  if l:break
  if S2>B2:B2,B1=S2,m
 return u(B1)
def u(m):
 a=m&127;t=(m>>7)&127;r=(m>>14)&7
 return '%c%d%c%d'%(97+(a&7),(a>>4)+1,97+(t&7),(t>>4)+1)+'  nbrq'[r].strip()
def v(s):
 a,t=[(int(s[i+1])-1)*16+ord(s[i])-97 for i in (0,2)]
 r='nbrq'.index(s[4])+2 if len(s)>4 else 0
 return a|t<<7|r<<14
def Y():
 global e,K_,j
 e=0;K_=[0,0];j=[]
 for q,p in enumerate(A):
  if p:
   e+=w(p,q)
   if abs(p)==6:K_[p>0]=q
if __name__=='__main__':
 url=os.environ['MAKEFUN_ENV_URL'].rstrip('/')
 while 1:
  X=J.load(W.urlopen(url+'/game',b'{}'))
  if X['status']=='over':continue
  if X['status']!='your_move':break
  L=X['legal_moves']
  A=[0]*128
  for i,c in enumerate('42356324'):A[i]=int(c);A[112+i]=-int(c);A[16+i]=1;A[96+i]=-1
  TN=1;CR=15;EP=-1;Y()
  for H in X['moves']:M(v(H))
  B=t(L)
  if not B:break
  J.load(W.urlopen(W.Request(url+'/move',J.dumps({'game':X['game'],'move':B}).encode())))
