FROM docker.dev.dszn.cz/debian:buster

EXPOSE 8000

WORKDIR /source
COPY debian debian/
COPY sklik_goalkeeper sklik_goalkeeper
COPY *requirements.* setup.* MANIFEST.in app_build_info.py .env ./
COPY Dockerfile /Dockerfile

RUN apt update && \
    cat requirements.apt | xargs apt install -y && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install -i https://pypi.kancelar.seznam.cz/simple/ -r install-requirements.txt -r requirements.txt && \
    python3 setup.py develop

RUN VCS_REF=$VCS_REF COMMIT_BRANCH=$COMMIT_BRANCH COMMIT_TAG=$COMMIT_TAG python3 ./app_build_info.py

CMD ["gunicorn","--worker-class","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:8000","sklik_goalkeeper:app"]

ARG BUILD_TYPE="manual"
ARG BUILD_DATE=
ARG VERSION=
ARG VCS_REF=
ARG BUILD_NUMBER
ARG BUILD_HOSTNAME=
LABEL org.label-schema.schema-version="1.0.0-rc.1" \
      org.label-schema.vendor="Seznam a.s." \
      org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.build-type="$BUILD_TYPE" \
      org.label-schema.build-host-name="$BUILD_HOSTNAME" \
      org.label-schema.build-ci-build-id="$BUILD_NUMBER" \
      org.label-schema.version="$VERSION" \
      org.label-schema.vcs-url="git@gitlab.seznam.net:aleksey.rembish/goalkeeper.git" \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.description="Sklik Goalkeeper web application" \
      org.label-schema.usage="https://gitlab.seznam.net/aleksey.rembish/goalkeeper" \
      org.label-schema.url="https://gitlab.seznam.net/aleksey.rembish/goalkeeper" \
      org.label-schema.docker.cmd="docker run -d -p 8000:8000"
ARG COMMIT_TAG="<undefined>"
ARG COMMIT_BRANCH="<undefined>"
