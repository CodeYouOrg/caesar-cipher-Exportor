# variables for Caesar Cipher:


alph=['a','b','c','d','e','f','g','h','i','j','k','l'
      'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

giv_ch= str()
ci_val=5
nu_str=str()
ol_indi=int()
nu_indi=int()
off1=int()
off2=int()

def offset(ol_indi):
  off1=ol_indi-20
  off1=off1-1
  return off1

def regulr():
  for x in giv_str:
    if x == 0:
      nu_str+=' '
    elif x != 0:
      ol_indi==alph.index(x)
    elif ol_indi>20:
      offset()

    elif off1==0:
      nu_str+=alph[off1]

    elif off1!= 0:
      nu_str=nu_str+alph[off1]
    else:
      nu_indi+=5
      nu_str=nu_str+alph[nu_indi]
      return
    
def main():
  giv_str=input('please provide a message:')
  regulr()
  print(nu_str)


  if __name__=='__main__':
    main()

    

      


# add your code here
