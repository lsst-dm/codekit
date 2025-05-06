FROM docker.io/python:3.13

ARG CODEKIT_REPO
ARG CODEKIT_REF

USER root
RUN pip install "git+https://github.com/${CODEKIT_REPO}@${CODEKIT_REF}" --no-cache-dir
# hadolint ignore=DL3059
RUN useradd -m codekit
USER codekit
WORKDIR /home/codekit

CMD ["/usr/local/bin/github-tag-release"]
