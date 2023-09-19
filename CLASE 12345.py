# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:59:14 2023

@author: USUARIO
"""


  
  
nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
   print("The native VLAN and the data VLAN are the same.")
else:
   print("This native VLAN and the data VLAN are different.")
  
  
  
  
aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
     print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
     print("This is a extended IPv4 ACL.")
else:
     print("This is not a standard or extended IPv4 ACL.")



devices=["R1","R2","R3","S1","S2"]
for item in devices:
    print(item)
  
  

lista=[1,2,3,4,5,6,7]
print(len(lista))

for elemento in lista:
    print(elemento, end=" ")
    
for item in range(10,1,-1):
    print(item)
    







