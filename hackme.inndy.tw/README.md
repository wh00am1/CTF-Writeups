# hackme.inndy.tw

## web

### LFI

Use php-file-include vulnerability to download the login.php

## Pwn

### fast

First send the string "yes I know" , then use `eval()` to complete the math problems quickly

### catflag

Use pwntools instead of netcat

### homework

Calculate the return address based on the disassembly

### toooomuch

Just guess the number lol

### toooomuch2

First use `gets()` to write the shellcode to Bss segment, then redirect execution to Bss

### ROP

Simply use `ROPgadget` to find ROP chain

### ROP 2

This time `ROPgadget` won't work, so we have to craft our own ropchain.

The basic concept is that we have to read our shellcode to a memory segament, and somehow execute it.

I'm gonna use Bss again but using `syscall` to `execve`

The ROP chain looks like this:

First `syscall(3)` to read() the shellcode to buffer, then use `syscall(8)` to write() "/bin/sh" to Bss

For execution, use `syscall(11)` to execve() our input "/bin/sh" 

### echo

A simple format string challenge

The offset is 7, so use pwntool's `fmtstr_payload` to overwrite `printf()` to `system()`

This way, `printf("/bin/sh")` becomes system("/bin/sh") and we get a shell

### smashthestack

The program has canary, so the `__stack_chk_fail` won't let us redirect code execution 

but it'll print the content stored in `__libc_argv[0]`

So we can simply overwrite the `__libc_argv[0]` to the address to flag, 

then the `__stack_chk_fail` will print the flag for us.

### onepunch

The program allows us to change the content of any address, so we can write our shellcode to `.text`

Using IDA's `patch key` can help us to know what value to enter can make the main function a endless-loop

Then we patch it back, the program directly execute the shellcode we just write

