FROM mcr.microsoft.com/devcontainers/python:1-3.12

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV CLOUDSDK_PYTHON /usr/bin/python3.10

# Install pipenv and compilation dependencies
RUN \
    apt-get update \
    && sudo apt-get install -y gnupg software-properties-common nodejs npm \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    gcc zsh wget nano procps htop python3-venv python3-dev git zsh tree \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER vscode

WORKDIR /home/vscode

ENV PATH="/home/vscode/venv/bin:$PATH"
ENV TERM xterm



# Install python dependencies in venv
COPY setup.py .
RUN python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip 

RUN mkdir /home/vscode/commandhistory && touch /home/vscode/commandhistory/.zsh_history

WORKDIR /home/app

ENV SHELL /bin/zsh

# Install application into container
COPY . /home/app
COPY ./images/.zshrc /home/vscode/.zshrc

CMD [ "tail", "-f", "/dev/null" ]