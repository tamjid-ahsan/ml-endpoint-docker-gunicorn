FROM python:3.8-slim-bookworm

WORKDIR /app

RUN pip install pandas==1.3.5 scikit-learn==0.23.2 flask==1.1.4 gunicorn xgboost==1.7.3 markupsafe==2.0.1 numpy==1.19.2
RUN pip install --upgrade Jinja2
RUN pip install -U flask

ADD ./data ./data
ADD server.py server.py

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "server:app" ]