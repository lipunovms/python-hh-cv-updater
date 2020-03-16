FROM python:3

env OPENSSL_CONF=/etc/ssl/
env PHANTOM_JS=phantomjs-2.1.1-linux-x86_64

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 &&\
    tar xvjf $PHANTOM_JS.tar.bz2 &&\
    rm $PHANTOM_JS.tar.bz2 &&\
    mv $PHANTOM_JS /usr/local/share &&\
    ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

WORKDIR /app

COPY requirements.txt cvupdater.py ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./cvupdater.py" ]

