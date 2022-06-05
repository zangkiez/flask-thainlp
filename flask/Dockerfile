FROM python:3.9-buster

WORKDIR /app

ADD . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list

# Create a uwsgi log directory and files
# RUN mkdir /var/log/uwsgi
# RUN touch /var/log/uwsgi/uwsgi_access.log
# RUN touch /var/log/uwsgi/uwsgi_error.log

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]