#To add to hash file run python cracker.py <filename> -h
#To run cracker run python cracker.py <filename> -c
from sys import argv, exit
from crypt import crypt

SALT = 'qd'#Randomly selected
HASH_FILE_NAME = 'hashes.txt'

def add_to_hash(word_list):
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

def crack(word_list):
    found = False
    hash_file = open(HASH_FILE_NAME)

    encrypted_passwords = hash_file.read().split('\n')

    for word in word_list:
        hashed_word = crypt(word , SALT)
        if(hashed_word in encrypted_passwords):
            print 'Match found: %r' % word
            found = True
    if not found:
        print 'No matches found'


if __name__ == '__main__':
    def print_argument_error_message():
        print 'Usage: python hash_creator.py <filename> -h|c'
        exit(0)

    try:
        ops = {'-h' : add_to_hash , '-c' : crack}
        if len(argv) < 3:
            print_argument_error_message()


        filename = argv[1]
        words = open(filename)

        word_list = words.read().split('\n')

        flag = argv[2]

        ops[flag](word_list)

    except KeyError:
        print_argument_error_message()
    except IOError:
        print 'No such file %r' % filename
        exit(0)

    
