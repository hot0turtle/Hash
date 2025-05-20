#Trabalho Leonardo Siqueira Hanke
import itertools
import hashlib
import time
from final import User, users, load_users

load_users()



def brute(character,max_lenght):
    attempt = 0
    final = 0
    for user in users:
        print(user.username)
        start_time = time.perf_counter()
        for lenght in range(1,max_lenght + 1):
            for combination in itertools.product(character, repeat=lenght):
                attempt += 1
                guess = ''.join(combination)
                guess_hash = hashlib.md5(guess.encode()).hexdigest()
                if guess_hash == user.password:
                    print(f"A senha de {user.username} e {guess}")
                    final = attempt
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"It took {elapsed} seconds and {final} attempts")
                
                    






def main():
    characther = "abcdefghijklmnopqrstuvwxyzç1234567890!@#$%^&*()-_=+"
    max_lenght = 4
    brute(characther,max_lenght)

main()