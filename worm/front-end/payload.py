def song():
    return "There's A War Going On For Your Mind"

def write_junk():
    for word in song().split():
        f = open(word + '.war' , 'w')
        f.write(1000000 * song())
    
if __name__ == '__main__':
    write_junk()
