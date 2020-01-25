# StegTask

### Requirements

`
pip3 install Pillow
`

### Usage

This works only for **PNG** images.

To execute encoding:

python steg.py -e [message] -i [image] -o [output]

- message: The message you want to embed
- image: The path to the image you want to embed the message into
- output: The path you want to output your embedded message

To execute Decoding:

python steg.py -d [image]

- image: path to image you want to decode


### Limitations 

Make sure your image is big enough to encode the message into. (This is overlooked at most places, included just in case.)
`
(Image pixel height * Image pixel width * 3) - 33 >= length of the message * byte_size(8)
`
