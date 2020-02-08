FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN cp ./patch/validation.fixed.py /usr/local/lib/python3.6/site-packages/connexion/decorators/validation.py
RUN python -m database

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
