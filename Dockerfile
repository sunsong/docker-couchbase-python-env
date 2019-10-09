FROM ubuntu:18.04

ADD sources.list /etc/apt/sources.list
ADD pip.conf /root/.pip/pip.conf
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    python3 \
    python3-dev \
    python3-pip \
    curl \
    git \
    htop \
    wget \
    zsh \
    vim

RUN wget -O - http://packages.couchbase.com/ubuntu/couchbase.key | apt-key add -
# Adding Ubuntu 18.04 repo to apt/sources.list of 18.10 or 19.04
RUN echo "deb http://packages.couchbase.com/ubuntu bionic bionic/main" | tee /etc/apt/sources.list.d/couchbase.list

RUN apt-get update
RUN apt-get install -y \
    libcouchbase-dev \
    libcouchbase2-bin

RUN pip3 install couchbase
RUN pip3 install ipython

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

ADD . /app/

CMD ["zsh"]
