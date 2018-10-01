FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN set -ex \
    && pip install -r /app/requirements.txt
CMD [ "python","/app/fetch.py" ]