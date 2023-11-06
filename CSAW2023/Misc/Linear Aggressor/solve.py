from pwn import *

host = 'misc.csaw.io'
port = 3000

flag = ''

for iteration in range(30):
    conn = remote(host, port)

    for _ in range(30):
        if _ == iteration:
            conn.sendline(b'1')    
        else:
            conn.sendline(b'0')

    response = conn.recvall().decode('utf-8').strip()[-3:] # Get the flag-related output only
    flag_parts = chr(int(response) - 125)
    flag += flag_parts

    conn.close()

print(flag)
