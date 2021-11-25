import os
import pickle
import hmac
import hashlib
def fun(name,password):
    s = {"username":name,"password":password}
    safecode = pickle.dumps(s)
    digest =  hmac.new('shared-key', safecode, hashlib.sha1).hexdigest()
    header = '%c' % (digest)
    conn.send(header + ' ' + safecode)
    with open("users.json","wb") as f:
        f.write(safecode)
    return safecode

def __setstate__(self, state):
        os.system('echo Executing malicious command')

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    yo_fun = fun(u,p)