for _ in range(30):
    
    conn.sendline('0')

response = conn.recvall().decode('utf-8')[-3]
print(response)