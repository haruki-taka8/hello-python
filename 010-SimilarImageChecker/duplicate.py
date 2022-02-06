import os
import imagehash
from PIL import Image

hash = []
duplicate = []
basedir = 'ENTER DIRECTORY HERE'

for filename in os.listdir(basedir):
    if (filename.startswith('2')) and (filename.endswith('.png')):
        print(filename)
        hash.append(
            {
                'file': filename,
                'hash': imagehash.average_hash(Image.open(basedir + filename).convert('RGB'))
            }
        )

hash = sorted(hash, key=lambda k: str(k['hash']))

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


print('Original | Duplicate(s)')
i = 1
while i < len(hash)-1:
    j = 1
    while hash[i]['hash'] == hash[i+j]['hash']:
        j += 1

    if j > 1:
        print(hash[i]['file'], end='')
        for k in range(1, j):
            print('|' + hash[i+k]['file'], end='')
            duplicate.append(hash[i+k]['file'])
        print()

    i += j
    
print()
print()
print('All Duplicates')
print('|'.join(duplicate))