'''
C-create
R-retrieve
U-update
D-delete
'''
# 
nileFile = open('zdc.txt','w')

# print(nileFile.name)
# print(nileFile.close())
# print(nileFile.mode)
nileFile.write('Hey, this is the last lap in python dont give up')
nileFile.write("\nit's alright")
# nileFile.close()

nileFile = open('zdc.txt','a')
nileFile.write('\ni love php')

nileFile = open('zdc.txt','r+')
text = nileFile.read(35)
print(text)