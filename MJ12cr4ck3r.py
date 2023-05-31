#!/usr/bin/env python3
import random
import string
import sys
import time

def generate_fake_password(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_banner():
    print('               _           _   _      _ ____')
    print('  /\/\   __ _ (_) ___  ___| |_(_) ___/ |___ \\')
    print(' /    \ / _` || |/ _ \/ __| __| |/ __| | __) |')
    print('/ /\/\ \ (_| || |  __/\__ \ |_| | (__| |/ __/')
    print('\/    \/\__,_|/ |\___||___/\__|_|\___|_|_____|')
    print('            |__/')
    print('')

def main():
    show_banner()
    print("   Majestic12 Fake Password Cracker v1.0 by 6un7h3r h3rm4nn\n\n")
    target = input("Enter the target's username: ")
    print(f"Attempting to crack password for: {target}  ", end="")
    spinner = spinning_cursor()
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    fake_password = generate_fake_password(12)
    print(f"\nCracked password: {fake_password}")

if __name__ == "__main__":
    main()
