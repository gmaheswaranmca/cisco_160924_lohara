#win programmers
import subprocess
result = subprocess.run(['dir'],shell=True,capture_output=True,text=True)
print(result.stdout)

#result = subprocess.run(['dir'],capture_output=True,text=True) #mac programmers
#                                       mac programmers
#['dir']                                ['ls]
#['python','-c','print(2**8)']          #['python','-c',"'print(2**8)'"]


import os
