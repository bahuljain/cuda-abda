# CUDA - Homework 3

Bahul Jain - bkj2111

### Instructions

- After launching an EC2 instance running a GPU and with CUDA installed on it, I
first installed PyCuda on it.

- Here are the set of commands that I needed to run to install PyCuda.

  ```bash
  $ sudo apt-get install libboost-all-dev
  $ sudo apt-get install build-essential python-dev python-setuptools libboost-python-dev libboost-thread-dev -y
  $ tar xzvf pycuda-VERSION.tar.gz
  $ cd pycuda-VERSION
  $ ./configure.py --cuda-root=/usr/local/cuda --cudadrv-lib-dir=/usr/lib/x86_64-linux-gnu --boost-inc-dir=/usr/include --boost-lib-dir=/usr/lib --boost-python-libname=boost_python --boost-thread-libname=boost_thread --no-use-shipped-boost
  $ make -j 4
  $ sudo python setup.py install
  $ sudo pip install .
  ```

- In this assignment I have taken a large dataset containing over 4000 images of
different types of objects, that need to be preprocessed before running an
object recognition algorithm on it.

- The main preprocessing required is that the images are all inverted and we need
to rotate it by 180 degrees to make them straight.

- The data folder contains various folders each containing inverted images of different object.

- The output folder will be provided in the same directory structure as the data folder but with the rotated images. This following snippet ensures the output folder structure is similar to that of the data folder.

  ```python
  for root, dirs, files in os.walk('./data/', topdown=False):
    for name in files:
        input_filename = (os.path.join(root, name))

        rotimg = rotate_image_file(input_filename)

        output_filename = (os.path.join('./output/' + root[7:], name))
  ```

- To run the given code, you need to copy the data folder in the project folder and the following command.

  ```bash
  python rotate.py > logs.txt
  ```

- The output folder will be automatically generated with the rotated images.

- The above command also generates a logs.txt file with all the logs and the time taken to perform the given task of rotating such huge number of images.
