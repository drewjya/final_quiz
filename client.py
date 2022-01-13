#!/usr/bin/env python3
import socket, sys
import base64
from stegano import lsb

IP = ""
PORT = 9000


def main():
    if (len(sys.argv)>1):
        IP = sys.argv[1]
        sct = socket.socket()
        sct.connect((IP, PORT))
        mess = input("Input message:")
        mess_utf = mess.encode("utf-8")
        mess_b64 = base64.b64encode(mess_utf)
        print(f'Encoded String : '+ mess_b64.decode("utf-8"))
        mess_b64dec = mess_b64.decode("utf-8")
        img = lsb.hide("dementor.png", message=mess_b64dec)
        img.save("dementorStego.png")
        img_decode = lsb.reveal("dementorStego.png")
        print(img_decode)
        print("Message injected successfully!!")
        file = open("dementorStego.png", "rb")
        sct.recv(1024).decode("utf-8")
        while True:
            SendData = file.read(1024)
            if not SendData:
                break
            sct.sendall(SendData)
        file.close()
        print("Done sending")
        # sct.send("Thank You")
        sct.close()
    else:
        print("You must run this file like python3 client.py <IP>")
        exit(1)


if __name__ == '__main__':
    main()
    