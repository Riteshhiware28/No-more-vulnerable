import os
import pickle
import hmac
import hashlib
def reverse_fun()
    conn,addr = self.receiver_socket.accept()
    data = conn.recv(1024)
    recvd_digest, safecode = data.split(' ')
    new_digest = hmac.new('shared-key', safecode, hashlib.sha1).hexdigest()
    if recvd_digest != new_digest:
      print 'Integrity check failed'
    else:
        with open("users.json","rb") as f:
        data = f.read()
        d = pickle.loads(data)
        return d

if __name__ == '__main__':
      print(reverse_fun())