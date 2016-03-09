#To add to hash file run python cracker.py <filename> -h
#To run cracker run python cracker.py <filename> -c
from sys import argv, exit
import hashlib

HASH_FILE_NAME = 'hashes.txt'
RAINBOW_TABLE_DELIMITER = 'COOL_UWI_DELIMITER'

def add_to_hash(word_list):
    hash_file = open(HASH_FILE_NAME , 'a')

    count = 0
    total = len(word_list)

    for word in word_list:
        if len(word) > 0:
            sha1_hash = hashlib.sha1(word.encode()).hexdigest()
            md5_hash = hashlib.md5(word.encode()).hexdigest()
            hash_file.write(sha1_hash + RAINBOW_TABLE_DELIMITER + md5_hash)
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

    table = map(lambda x: [x.split(RAINBOW_TABLE_DELIMITER)[0] , x.split(RAINBOW_TABLE_DELIMITER)[1]] if len(x) > 1 else [] , encrypted_passwords)
    for word in word_list:
        sha1_hash = hashlib.sha1(word.encode()).hexdigest()
        md5_hash  = hashlib.md5(word.encode()).hexdigest()
        hash_row = [sha1_hash , md5_hash]
        if hash_row in table:
            print 'Match found: %r' % word
            matches += 1

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

