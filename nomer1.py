import numpy as np
 
x=1
q=1/np.e * (np.sin(x)+1)
w=(5/4+1/x**15)
y=np.log(q / w)/np.log(1+ x**2)
print(y,  'если х=1')

x=10 
q=1/np.e * (np.sin(x)+1)
w=(5/4+1/x**15)
y=np.log(q / w)/np.log(1+ x**2)
print(y,  'если х=10')

x=1000
q=1/np.e * (np.sin(x)+1)
w=(5/4+1/x**15)
y=np.log(q / w)/np.log(1+ x**2)
print(y,  'если х=1000')


