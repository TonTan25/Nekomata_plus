w1 = 'hello im '
w2 = ' 猫又'
ws = w1+w2
print(ws)
wa = [w1,w2]
a = ' '.join(wa)#them vao giua cac phan tu nhung gia tri trong ''
print(a)
aa= 'that la thu zi {} , {}'.format(w1,w2) # them lan luot ca gia tri trong fomat vao chuoi 
print(aa)
b= 'watashi wa neko de su.'
c = '猫又です'
#ab = b.replace('watashi','Boku').replace('neko','nekomata')
ab = b.replace(b,c)# replace thay doi phan tu trong chuoi ma khong can xac dinh vi tri 
print(b +'\n'+ ab)