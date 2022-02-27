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
RUN npm install
RUN npm run build
WORKDIR /app
RUN rm -r vuegui

ENV VUE_DISTRIBUTION_DIR=/app/vue
ENV PYTHONUNBUFFERED=TRUE

# Enables open shift container user (which is not root) to write distribution dir
RUN chgrp -R 0 $VUE_DISTRIBUTION_DIR && \
    chmod -R g=u $VUE_DISTRIBUTION_DIR

EXPOSE 4005

# OpenShift picks up this label and creates a service
LABEL io.openshift.expose-services="4005/http"


ENTRYPOINT ["gunicorn", "--log-level", "debug", "-b", "localhost:4005", "multilangdia.app:app"]