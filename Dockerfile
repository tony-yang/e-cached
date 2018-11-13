# My personal dev env Docker image from my baremetal-init repo
FROM ubuntu-dev

RUN pip3 install --upgrade \
    coverage \
    pip \
    setuptools \
 && mkdir /var/log/py_cached

ADD . /root/

RUN pip install -e /root/py_cached/.
