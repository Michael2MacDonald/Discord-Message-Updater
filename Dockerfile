FROM python:3

COPY message_updater.py /bin/message_updater
COPY requirements.txt /tmp/requirements.txt
RUN chmod +x /bin/message_updater && pip install -r /tmp/requirements.txt

CMD ["/bin/message_updater"]
