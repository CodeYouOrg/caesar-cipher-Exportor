message = str()
orig_index = int()
off_index = int()          #Variables
final_index = int()
orig_off = 5
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nu_mess = str()
blank = (' ')

message = input('please provide a message:')

for x in message:
   orig_index == 0
   orig_index=alph.index(x) 
   if  orig_index > 20:
          off_index = orig_index - 21
          nu_mess += alph[off_index]
   else:
       orig_index = orig_index + 5
       nu_mess += alph[orig_index]
print(nu_mess)

