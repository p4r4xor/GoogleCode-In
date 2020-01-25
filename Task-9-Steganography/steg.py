from __future__ import print_function
from PIL import Image
import binascii
import sys

def text2bin(text):
    binary = ''.join(format(ord(x), 'b').zfill(8) for x in text)
    return binary

def bin2text(bin):
    a = int(bin, 2)
    hex_string = '%x' % a
    n = len(hex_string)
    z = binascii.unhexlify(hex_string.zfill(n + (n & 1)))
    text=z.decode('ascii')
    return text

def bin2int(bin):
    return int(bin,2)

def int2bin(integer):
        bin = "{0:b}".format(integer)
        while(len(bin) < 32):
            bin = '0' + bin
        return bin


if sys.argv[1] == '-d':
    if len(sys.argv) < 3:
        print("Missing argument or flag")
        sys.exit()
    
    im = Image.open(sys.argv[2])
    px = im.load()
    im_w, im_h = im.size

    text_len = ''
    count = 0
    for j in range(im_h - 1, 0, -1):
        for i in range(im_w-1,0,-1):
            
            R,G,B = px[i,j]

            #RED
            bin_R = text2bin(str(R))
            text_len = text_len + bin_R[len(bin_R)-1:]
            count +=1

            #GREEN
            bin_G = text2bin(str(G))
            text_len = text_len + bin_G[len(bin_G)-1:]
            count +=1
        
            if count == 32 :
                break

            #BLUE
            bin_B = text2bin(str(B))
            text_len = text_len + bin_B[len(bin_B)-1:]
            count +=1
        
        if count == 32:
            break
    
    text_len
    text_len = bin2int(text_len)

    #Decode the hidden message
    count = 0
    skip_count = 0
    hidden_msg =''
    for j in range(im_h -1, 0, -1):
        for i in range(im_w - 1, 0, -1):
            R,G,B = px[i,j]

            if count != text_len and skip_count >= 33:
                bin_R = text2bin(str(R))
                hidden_msg = hidden_msg + bin_R[len(bin_R)-1:]
                count+=1
            skip_count += 1

            if count != text_len and skip_count >= 33:
                bin_G = text2bin(str(G))
                hidden_msg = hidden_msg + bin_G[len(bin_G)-1:]
                count+=1
            skip_count += 1

            if count != text_len and skip_count >= 33:
                bin_B = text2bin(str(B))
                hidden_msg = hidden_msg + bin_B[len(bin_B)-1:]
                count+=1
            skip_count += 1
            
            if count == text_len:
                break
        if count == text_len:
            break

    hidden_msg = bin2text(hidden_msg)

    
    print(hidden_msg)

elif sys.argv[1] == '-e':

    if len(sys.argv) < 7:
        print("Missing argument or flag")
        sys.exit()
    im = Image.open(sys.argv[4])
    msg = sys.argv[2]
    px = im.load()
    im_w, im_h = im.size
    msg_bin = text2bin(msg)
    msg_len = len(msg_bin)
    msg_len_bin = int2bin(msg_len)
    
    max_px = (im_w * im_h)* 3

    if max_px < 33:
        print("Image length will not fit in Image")
        sys.exit()
    if max_px - 33 <= msg_len:
        print("Supplied data will not fit image")
        sys.exit()
    


    count = 0
    for j in range(im_h-1, 0, -1):
        for i in range(im_w-1,0,-1):
            R,G,B = px[i,im_h-1]
            
            
            bin_R = text2bin(str(R))
            bin_R = bin_R[:len(bin_R)-1] + msg_len_bin[count]
            R = bin2text(bin_R)
            count +=1

            bin_G = text2bin(str(G))
            bin_G = bin_G[:len(bin_G)-1] + msg_len_bin[count]
            G = bin2text(bin_G)     
            count+=1

            if count != 32:
                bin_B = text2bin(str(B))
                bin_B = bin_B[:len(bin_B)-1] + msg_len_bin[count]
                B = bin2text(bin_B)    
                count+=1
            px[i,j] = (int(R),int(G),int(B))
            if count == 32:
                break
        if count == 32: 
            break
    

    count = 0
    skip_count = 0
    for j in range(im_h -1, 0, -1):
        for i in range(im_w - 1, 0, -1):
            R,G,B = px[i,j]

            
            if count != msg_len and skip_count >= 33:
                bin_R = text2bin(str(R))
                bin_R = bin_R[:len(bin_R)-1] + msg_bin[count]
                R = bin2text(bin_R)
                count +=1
            skip_count += 1

            if count != msg_len and skip_count >= 33:
                bin_G = text2bin(str(G))
                bin_G = bin_G[:len(bin_G)-1] + msg_bin[count]
                G = bin2text(bin_G)  
                count+=1
            skip_count += 1

            if count != msg_len and skip_count >= 33:
                bin_B = text2bin(str(B))
                bin_B = bin_B[:len(bin_B)-1] + msg_bin[count]
                B = bin2text(bin_B)   
                count+=1
            skip_count += 1

            
            px[i,j] = (int(R),int(G),int(B))
            if count == msg_len:
                break
        if count == msg_len:
            break


    im.save(sys.argv[6])
else:
    
    print("-d for decrypt")
    print("-e for encrypt")