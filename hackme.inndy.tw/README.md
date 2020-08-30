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

 