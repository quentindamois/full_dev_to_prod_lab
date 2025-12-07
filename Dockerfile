FROM python:3.10-alpine

WORKDIR /flask-app

COPY . .

RUN pip install -r requirements.txt

ENV DATABASE_URL=$DATABASE_URL

EXPOSE 5000

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]