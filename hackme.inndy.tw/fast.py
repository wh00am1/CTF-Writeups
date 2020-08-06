#!/usr/bin/env python2

from pwn import *

p = remote('hackme.inndy.tw', 7707)
context.log_level = 'debug'

p.sendlineafter("Send 'Yes I know' to start the game.", 'Yes I know')

res = ''
for i in range(10000):
    res += (str(eval(p.recvuntil('= ?\n', drop='True'))) + ' ')

p.sendline(res)
print p.recv()
p.close()

# not done, WTF
