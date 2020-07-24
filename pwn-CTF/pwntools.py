from pwn import *

p = remote('140.110.112.192', 2116)
p.sendlineafter(':)\n', p32(127174655))
p.recvuntil('\n', drop='True')

for i in range(1000):
	q = p.recvuntil('= ?', drop='True')
	print q
	p.sendline(str(eval(q)))

p.interactive()
p.close()
