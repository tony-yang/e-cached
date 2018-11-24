# My personal dev env Docker image from my baremetal-init repo
FROM go-dev

RUN pip3 install --upgrade \
    coverage \
    pip \
    setuptools \
 && mkdir /var/log/py_cached

ADD . /root/

RUN mv /root/go_cached/ecached ${HOME}/dev/src \
 && pip install -e /root/py_cached/.
