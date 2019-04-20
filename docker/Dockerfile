FROM python:3

ADD src/ /

RUN pip3 install requests
RUN pip3 install bs4
RUN pip3 install todoist-python

CMD [ "python", "./dashboard.py" ]
