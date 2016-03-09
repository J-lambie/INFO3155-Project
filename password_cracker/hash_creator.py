#To Hash a file run python hash_creator.py <filename>
from sys import argv, exit
from crypt import crypt

SALT = 'qd'#Randomly selected
HASH_FILE_NAME = 'hashes.txt'
if len(argv) < 2:
    print 'Usage: python hash_creator.py <filename>'
    exit(0)

filename = argv[1]
words = open(filename)

word_list = words.read().split('\n')
hash_file = open(HASH_FILE_NAME , 'a')

count = 0
total = len(word_list)

for word in word_list:
    hashed_word = crypt(word , SALT)
    hash_file.write(hashed_word)
    hash_file.write('\n')
    if(count % 10000 == 0):
        print '%d of %d words hashed' % (count, total)
    count += 1 
     
hash_file.close()
print '%d of %d words hashed' % (count, total)


