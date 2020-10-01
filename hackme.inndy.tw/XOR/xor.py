#!/usr/bin/env python2

xorkey = 'hackmepls'
flag = ''
with open('xor', 'rb') as f:
    data = f.read()
    for i in range(0, len(data)):
        flag += chr(ord(data[i]) ^ ord(xorkey[i % len(xorkey)]))

print 'flag : {}'.format(flag)
