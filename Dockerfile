FROM python:3.10.2-bullseye


RUN mkdir /app
WORKDIR /app

COPY Pipfile.lock .
COPY Pipfile .

RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --deploy --system

RUN apt-get update
RUN apt-get install -y nodejs npm

COPY multilangdia/ multilangdia/
COPY vuegui/ vuegui/

RUN echo "module.exports = { " \
          "  outputDir : \"/app/vue\" " \
          "}" \
          > vuegui/vue.config.js

WORKDIR /app/vuegui
RUN npm run build
WORKDIR /app
RUN rm -r vuegui

