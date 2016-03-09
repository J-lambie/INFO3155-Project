#To add to hash file run python cracker.py <filename> -h
#To run cracker run python cracker.py <filename> -c
from sys import argv, exit
import hashlib

HASH_FILE_NAME = 'hashes.txt'
RAINBOW_TABLE_DELIMETER = 'COOL_UWI_DELIMETER'

def add_to_hash(word_list):
    hash_file = open(HASH_FILE_NAME , 'a')

    count = 0
    total = len(word_list)

    for word in word_list:
        sha1_hash = hashlib.sha1(word.encode()).hexdigest()
        md5_hash = hashlib.md5(word.encode()).hexdigest()
        hash_file.write(sha1_hash + RAINBOW_TABLE_DELIMETER + md5_hash)
        hash_file.write('\n')
        if(count % 10000 == 0):
            print '%d of %d words hashed' % (count, total)
        count += 1 

    hash_file.close()
    print '%d of %d words hashed' % (count, total)

def crack(word_list):
    hash_file = open(HASH_FILE_NAME)
    matches = 0

    encrypted_passwords = hash_file.read().split('\n')

    for word in word_list:
        sha1_hash = hashlib.sha1(word.encode()).hexdigest()
        md5_hash  = hashlib.md5(word.encode()).hexdigest()
        for encrypted_password in encrypted_passwords:
            columns = encrypted_password.split(RAINBOW_TABLE_DELIMETER)
            if len(columns) > 1 and (sha1_hash == columns[0] or md5_hash == columns[1]):
                print 'Match found: %r' % word
                matches += 1
                break

    if matches == 0:
        print 'No matches found'
    else:
        print '%d matches' % (matches)


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

