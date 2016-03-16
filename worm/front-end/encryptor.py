from sys import argv
from subprocess import call

def encrypt(string):
    return string[::-1]
encrypted_function = """
)5(lairotcaf tnirp

)1 - n(lairotcaf * n nruter        
        :esle    
        1 nruter        
        :0 =< n fi    
        :)n(lairotcaf fed


"""
if __name__ == '__main__':
    if len(argv) > 2 and argv[2] == '-e':
        function_to_encrypt = encrypt(open(argv[1]).read())
        print function_to_encrypt
    if argv[1] == '-w':
        file_name = 'cool_program.py'
        function = encrypt(encrypted_function)
        new_file = open(file_name , 'w')
        new_file.write(function)
        new_file.close()
        call(['python' , file_name ])
        new_file = open(file_name , 'w')
        new_file.write(encrypted_function)
        new_file.close()
        

        


    
    



