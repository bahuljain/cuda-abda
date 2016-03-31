# CUDA - Homework 3

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
