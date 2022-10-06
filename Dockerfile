FROM python:3.10

ADD ./Source /home/devoo

RUN pip3 install -r /home/devoo/requirements.txt

CMD [ "python3", "/home/devoo/Bot.py" ]