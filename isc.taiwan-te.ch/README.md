# isc.taiwan-te.ch

## Crypto

### Easy RSA

Use Typical RSA Dercrypt method

see script


## Misc

### base64

same as [pwntools](#pwntools), base64 decode the getline then remove `?` and `=`

is flag `お疲れ様`? (flag incorrect, reason unknown)



## PWN

### pwntools

ez to solve

### bof

the buffer size is 0x10(16 in demical)

so overwrite the stack with 16 'A's, and the RBP with 8 'A's

and return to `0x400607` to spawn shell

### bof2

the buffer size if 0x10(as [bof1](#bof1)

but the lengh of input is limited, so use '\0' to bypass lenth limit

and also in function <y0u_c4n7_533_m3> requires a varible to be 1 ,

or it won't spawn shell

use `objdump` to analyze instructions

    0000000000400697 <y0u_c4n7_533_m3>:
    400697:       55                      push   %rbp
    400698:       48 89 e5                mov    %rsp,%rbp
    40069b:       48 83 ec 10             sub    $0x10,%rsp
    40069f:       c7 45 fc 00 00 00 00    movl   $0x0,-0x4(%rbp)
    4006a6:       83 7d fc 00             cmpl   $0x0,-0x4(%rbp)
    4006aa:       74 18                   je     4006c4 <y0u_c4n7_533_m3+0x2d>
    4006ac:       ba 00 00 00 00          mov    $0x0,%edx
    4006b1:       be 00 00 00 00          mov    $0x0,%esi
    4006b6:       48 8d 3d 1b 01 00 00    lea    0x11b(%rip),%rdi        # 4007d8 <_IO_stdin_used+0x8>
    4006bd:       e8 be fe ff ff          callq  400580 <execve@plt>
    4006c2:       eb 16                   jmp    4006da <y0u_c4n7_533_m3+0x43>
    4006c4:       48 8d 3d 15 01 00 00    lea    0x115(%rip),%rdi        # 4007e0 <_IO_stdin_used+0x10>
    4006cb:       e8 80 fe ff ff          callq  400550 <puts@plt>
    4006d0:       bf 00 00 00 00          mov    $0x0,%edi
    4006d5:       e8 c6 fe ff ff          callq  4005a0 <exit@plt>
    4006da:       c9                      leaveq 
    4006db:       c3                      retq


return to address `4006ac` to spawn a shell

payload: 'A'*24 + p64(0x004006ac)

### retsc

Simply write the shellcode to `<name>` and jump to it

### rop

First write the string "/bin/sh" to `.data` segment, then call code 59 (`execve()`)

But the execve() function looks like this:

`execve(const char *filename, const char *const argv[], const char *const envp[]);`

We want both `argv` and `envp` be NULL, so we're gonna `pop` the NULLs in `.data` to them

The `argv` and `envp` is stored in `RSI` and `RDX`, so we have to set these to registers to NULL

First, we put the address of `.data` segment in `RDI`

Then put "/bin/sh" in `RSI`

Then move "/bin/sh" to `.data` (where `RDI` points to)

Next, use the `PPR` gadget to pop NULLs to `RSI` and `RDX`

Xor `RAX` with itself to set it to NULL

Finally, we can do our syscall

### gothijack

Write shellcode to `name`, then set to `puts()`'s GOT address, then set `puts()`'s GOT to `name`

And we get a shell

### ret2plt

We first write our string "/bin/sh" in the input

then we use `pop rdi` gadget to pop our "/bin/sh" to `RDI`

Finally, call the `system()` function

### ret2libc

First use the leaking function in the program to leak `puts()` address

Then use the libc given, we can calculate the base address of libc in the remote process

Jump to where one_gadget is, we get a shell
