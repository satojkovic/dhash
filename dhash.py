#!-*- coding: utf-8 -*-

"""
Usage: dhash.py <IMAGE>
       dhash.py -h | --help
       dhash.py --version
Options:
       -h --help    show this screen
       --version    show version
"""

from docopt import docopt
import sys
import cv2

RESIZE_W = 9
RESIZE_H = 8


def main():
    opts = docopt(__doc__, version='1.0')
    img_file = opts['<IMAGE>']
    if not img_file:
        print 'not found: %s' % img_fil
        sys.exit(1)

    # read the image
    img = cv2.imread(img_file)

    # Reduce size
    img = cv2.resize(img, (RESIZE_W, RESIZE_H))

    # Reduce color
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Compute the difference and Assign bits
    bits = []
    for row in xrange(img.shape[0]):
        for col in xrange(img.shape[1]-1):
            l = img[row][col]
            r = img[row][col+1]
            bits.append('1') if l > r else bits.append('0')

    dhash = ''
    for i in xrange(0, len(bits), 4):
        dhash += hex(int(''.join(bits[i:i+4]), 2))
    print 'dhash = %s' % dhash.replace('0x', '')

if __name__ == '__main__':
    main()
