import socket,os

host=""
port=5678
flg=0
#dir = "/Data/"
def send(s,file):
    k=0
    size=len(file)
    k=k+1
    size=bin(size)[2:].zfill(16)
    s.send(size)
    s.send(file)
    lp=0
    fize=os.path.getsize(file)
    fize=bin(fize)[2:].zfill(32)
    s.send(fize)
    kl=0
    File=open(file,'rb')
    l=File.read()
    s.sendall(l)
    File.close()


s = socket.socket()
s.bind((host,port))
s.listen(5)

while True:
    conn,addr = s.accept()
    print 'Server Started'
    flg=1
    size= conn.recv(16)
    size=int(size,2)
    data=conn.recv(size)
    fnames=data.split()

    for f in fnames:
        flg=0
        if os.path.isfile(f):
            key=1
            key=bin(key)[2:].zfill(16)
            flg=1
            conn.send(key)
            file=f
            send(conn,file)
        else:
            key=0
            key=bin(key)[2:].zfill(16)
            conn.send(key)
            size=len(f)
            flg=0
            size = bin(size)[2:].zfill(16)
            conn.send(size)
            conn.send(f)
            print f + " does not exist"

    conn.close()
