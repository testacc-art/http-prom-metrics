FROM python:3.8-alpine

ARG GIT_COMMIT
ARG GIT_TAGREF

ENV ASYNCWORKER_HTTP_HOST 0.0.0.0
ENV GIT_COMMIT ${GIT_COMMIT}
ENV GIT_TAGREF ${GIT_TAGREF}

WORKDIR /app
COPY . /app

RUN apk -U add --virtual .deps \
      gcc \
      make \
      python3-dev \
      linux-headers \
      musl-dev \
&& pip install pipenv \
&& pipenv install --system --deploy --ignore-pipfile \
&& apk del --purge .deps

CMD ["python", "-m", "httpmetrics"]
