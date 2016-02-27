import sys

def glue_stick(left, right, outfile):
    import cv2
    import numpy as np
    import imutils
    
    left = cv2.imread(left)
    right = cv2.imread(right)
    
    left = imutils.resize(left, height=500)
    right = imutils.resize(right, height=500)
    
    output = np.concatenate((left, right), axis=1)
    
    cv2.imwrite(outfile, output)
    
if __name__=="__main__":
    left = sys.argv[1]
    right = sys.argv[2]
    outfile = sys.argv[3]

    glue_stick(left, right, outfile)