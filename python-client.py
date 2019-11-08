## http://stackoverflow.com/questions/24564587/communicate-between-a-processing-sketch-and-a-python-program/24565160?noredirect=1#comment38049611_24565160

import time, sys, serial, socket
import constants


self.sock.send(message)
self.host = constants.HOST_BTLE
self.port = constants.PORT_BTLE
self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
self.NUM_ROBOTS = constants.NUM_ROBOTS
COLOR_TYPE = 20

sock = socket.socket()
sock.connect((self.host,self.port))

def step():
    message = ""
    for i in range(0, self.NUM_ROBOTS):
        message = "0,20,90,90"
        self.sock.send(message)

def main():
    while 1:
        try:
            s.step()
            time.sleep(0.02)
        except (socket.error, KeyboardInterrupt):
            s.closeSocket()
            sys.exit()

if __name__ == '__main__':
    main()
