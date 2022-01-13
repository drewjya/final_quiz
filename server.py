import socket
import base64
from stegano import lsb

PORT = 9000
IP = ""

def main():
    sct = socket.socket()
    print("Server is listening on port : ", PORT, "\n")
    sct.bind((IP, PORT))
    sct.listen(10)
    print("Copied filename will be recv.png on the server")
    while True:
        conn, addr = sct.accept()
        msg = "Hi Client [IP]:"+addr[0] + "\n Welcome to the Server"
        conn.send(msg.encode())
        with open("recv.png", "wb") as file:
            print("FIle opened")
            while True:
                recv = conn.recv(1024)
                if not recv:
                    break
                file.write(recv)    
        file.close()
        print("File copied successfully")
        conn.close()
        print("Break connection")
        imgDecode = lsb.reveal("recv.png")
        print("Message Found")
        print("Enrypted message is " + imgDecode)
        msgEncrypted = imgDecode.encode("utf-8")
        msgDecode = base64.b64decode(msgEncrypted)
        print("Decode message is : " + msgDecode.decode("utf-8"))
        break

if __name__ == '__main__':
    main()
    