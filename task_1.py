#Перебрать все возможные пароли от a до zzzzzzzzz, используя функцию h = f(p). p - пароль.
import itertools
import multiprocessing
import string
from itertools import product
import hashlib
from multiprocessing import Process, Event
password = 'abhyb'
hash_obj = hashlib.sha256(password.encode())
hashed_password = hash_obj.hexdigest()
chars = string.ascii_lowercase
chars_part_1 ='abcdef'
chars_part_2 = 'ghijkl'
chars_part_3 = 'mnopqrs'
chars_part_4 = 'tuvwxyz'


def generate_passwords(band):
    for length in range(1,10):
        for first_char in band:
            for comb in itertools.product(chars, repeat=length-1):
                trial_pass = first_char
                for sym in comb:
                    trial_pass+=sym
                yield trial_pass
def compare(chars_spare, stop_event):
    for value in generate_passwords(chars_spare):
        if stop_event.is_set():
            break
        hash_obj_example = hashlib.sha256(value.encode())
        hashed_example = hash_obj_example.hexdigest()
        if hashed_example == hashed_password:
            print(f'Пароль найден - {value}')
            stop_event.set()
            break
if __name__ == '__main__':
    stop_event = Event()
    p1 = multiprocessing.Process(target=compare, args=(chars_part_1, stop_event))
    p2 = multiprocessing.Process(target=compare, args=(chars_part_2, stop_event))
    p3 = multiprocessing.Process(target=compare, args=(chars_part_3, stop_event))
    p4 = multiprocessing.Process(target=compare, args=(chars_part_4, stop_event))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()







