from pwn import *
p=process("./chall_09")
payload = xor(b'=\x01',0x69)+b'\x00'
print(payload)
p.sendline(payload)
p.interactive()
