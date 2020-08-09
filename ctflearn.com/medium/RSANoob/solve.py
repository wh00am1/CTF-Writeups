#!/usr/bin/env python2

import binascii
import gmpy2

e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083
p = 416064700201658306196320137931
q = n / p

phi_n = (p - 1)*(q - 1)
d = gmpy2.invert(e, phi_n)

text = pow(c, d, n)
print binascii.unhexlify(hex(text)[2:])
