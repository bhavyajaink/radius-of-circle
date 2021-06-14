ext=input('enter the fileneme:')
a=ext.split('.')
b=a[1]
if b=='py':
    print("The extesion of file is:'python'")
elif b=='java':
    print("The extesion of file is:'Java'")
elif b=='cpp':
    print("The extesion of file is:'C++'")
else:
    print("Don't know this type of extennsion")
    
