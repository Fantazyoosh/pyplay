import hashlib
import os
import glob

path = '/home/pi/Desktop/mes/'
#plik = 'God of War II (USA).iso'
plik = '1.NES'

print(glob.glob(path+'*.*'))

blocksize = 65536
hasher = hashlib.sha1()
with open(path+plik, 'rb') as afile:
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
print(hasher.hexdigest())


if hasher.hexdigest() == 'a20a0ba427a13b2268e82701a9aea09a31b12855':
    print('zgadza sie')
    # os.rename(path+plik,path+plik+'xxx')
