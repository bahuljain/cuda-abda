import os

def ensure_dir(file):
    d = os.path.dirname(file)
    if not os.path.exists(d):
        os.makedirs(d)

for root, dirs, files in os.walk('./data/', topdown=False):
    for name in files:
        filename = (os.path.join('./output/' +root[7:], name))
        ensure_dir(filename)
