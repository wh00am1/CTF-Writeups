#!/usr/bin/env python2

from pwn import *
from base64 import b64decode

context.log_level = 'debug'
p = remote('isc.taiwan-te.ch', 10801)
for i in range(100):
    p.recvuntil('100\n', drop='True')
    ans = base64.b64decode(p.recvline())
    ans = ans.replace('=', '')
    ans = ans.replace('?', '')
    p.sendlineafter('>', str(eval(ans)))

print p.recv()
p.interactive()
p.close()

# flag is お疲れ様 ???
#failed(flag incorrect), why?
