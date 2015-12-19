
#!/usr/bin/env python
import hashlib

def find_prefix(input, prefix):
    for i in range(0, 10000000):
        hash = hashlib.md5(input + str(i).encode()).hexdigest()
        if (hash.startswith(prefix)):
            print("number: %d, hash: %s" % (i, hash))
            return



def main():
    puzzle = b'ckczppom'
    find_prefix(puzzle, '00000')
    find_prefix(puzzle, '000000')

    # puzzle = b'abcdef' # test, result should be 609043
    # puzzle = b'pqrstuv' # test, result should be 1048970



if __name__ == '__main__':
    main()
