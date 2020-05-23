#!/usr/bin/env python2

from pwn import *

context.log_level = 'debug'

p = remote('isc.taiwan-te.ch', 9999)
p.sendlineafter(':)\n', p32(3735928559)) #magic number
print p.recvline()

for i in range(1000):
    p.sendline(str(eval(p.recvuntil('= ?', drop='True'))))

# print p.recv()
p.interactive()
p.close()


