import os
x = os.chdir('C:/Users/vamsi/python/sample')
for i in os.listdir(x):
    f_name,f_ext = os.path.splitext(i)
    course,prog = f_name.split('-')
    prog_l,num = prog.split()
    new_name = '{}-{}{}'.format(num[1:],prog_l,f_ext)
    os.rename(i,new_name)
