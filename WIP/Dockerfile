# Use the base image with python 3.8
# FROM python:3.8-slim-bookworm
FROM python:3.9

# Install the NGINX
RUN apt-get -y update && apt-get install -y --no-install-recommends nginx && rm -rf /var/lib/apt/lists/* 
# Copy the nginx.conf to the configuration file location
COPY conf/nginx.conf /etc/nginx/sites-enabled/default 

# Install python packages
RUN pip install pandas==1.3.5 scikit-learn==0.23.2 flask==1.1.4 gunicorn xgboost==1.7.3 markupsafe==2.0.1 numpy==1.19.2 uwsgi 
RUN pip install --upgrade Jinja2
RUN pip install -U flask

# Set the working directory as app and copy the required files
WORKDIR /app
ADD ./data ./data
ADD server.py server.py

EXPOSE 5000

# CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "server:app" ]

#Start the nginx service and python application
CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --manage-script-name --mount /=server:app