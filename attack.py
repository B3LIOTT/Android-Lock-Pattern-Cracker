from utils import *
import itertools
from hashlib import sha1, sha256
from plotter import *
from math import factorial, comb
from tqdm import tqdm
from time import perf_counter
import sys


__author__ = "b3liott"



def attack(hash_type: HashType, hash: str):
    """
    Brute force attack to find the pattern
    :param hash_type: Hash type, SHA1 or SHA256
    :param hash: Hash value, in hex
    """

    print("Hash type: ", hash_type)
    print("Hash: ", hash)

    if hash_type == HashType.SHA1:
        hash_func = sha1
    elif hash_type == HashType.SHA256:
        hash_func = sha256
    
    vals = NODES.keys()
    length = len(vals)
    start = perf_counter()

    for i in range(2, length+1):
        if VERBOSE:
            print("\n\nTrying with ", i, " nodes")

        perms = itertools.permutations(vals, i)
        
        size = factorial(i)*comb(length, i)
        iterator = tqdm(perms, total=size) if VERBOSE else perms

        for perm in iterator:
            perm = ''.join(perm).encode('utf-8')
            computed_hash = hash_func(perm).hexdigest()

            if computed_hash == hash:
                return perm, perf_counter()-start
                
    raise ValueError("Pattern not found")


def init_attack(attack_type: AttackType, data: str):
    """
    Initialize the attack
    :param attack_type: Attack type, HASH or FILE
    :param data: Hash value or file path
    """

    if attack_type == AttackType.HASH:
        if len(bytearray.fromhex(data)) == 20:
            return attack(hash_type=HashType.SHA1, hash=data)

        elif len(bytearray.fromhex(data)) == 32:
            return attack(hash_type=HashType.SHA256, hash=data)

    elif attack_type == AttackType.FILE:
        hash = open_key_file(data)
        return init_attack(attack_type=AttackType.HASH, data=hash)

    else:
        raise ValueError("Invalid attack type")



#--------------------------------------------------------------#

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc not in [3, 4]:
        print("Usage: ")
        print("attack.py [-v] [-p hash ] or [-f file.key ] ]")
        print("-v : verbose mode")
        print("-p : hash value in hex")
        print("-f : file path, like gesture.key")
        print()
        sys.exit(1)

    else:
        global VERBOSE
        VERBOSE = False

        res = None
        start = 1
        try:
            if sys.argv[1] == '-v':
                if argc == 4:
                    VERBOSE = True
                    start = 2
                else:
                    raise ValueError("Invalid arguments")

            data_type = sys.argv[start]
            data = sys.argv[start+1]

            if sys.argv[start] == '-f':
                res = init_attack(attack_type=AttackType.FILE, data=data)
            
            elif sys.argv[start] == '-p':
                res = init_attack(attack_type=AttackType.HASH, data=data)

        except Exception as e:
            print("An error occured: ", e)
            sys.exit(1)


        print()
        print("--------Attack finished--------")
        try:
            pattern = res[0]
            time = res[1]
            decoded_res = pattern.hex().replace('0', '')
            print("Pattern found: ", decoded_res)
            print("Time taken: ", time, " seconds")
            
        except Exception as e:
            print("Failed to decode the result: ", e)
            print("Ressult: ", res)
            sys.exit(1)
        
        try:
            print()
            plot_graph(pattern=decoded_res)

        except Exception as e:
            print("Failed to plot the pattern: ", e)
            sys.exit(1)
