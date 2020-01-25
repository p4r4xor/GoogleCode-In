#Issue with celery=4.2.1 with Py3.7 hence Py3.6.8 used
FROM python:3.6.8-alpine

# Set current working directory
WORKDIR /app

#Install required system packages
RUN apk add --update --no-cache build-base bash readline libffi-dev ncurses-dev python2-dev postgresql-dev

# Install required Python packages
COPY ./requirements /app/requirements
RUN pip install -r requirements/dev.txt

# Set correct DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=happinesspackets.settings.dev

# Set the path for fedora-messaging configuration file
ENV FEDORA_MESSAGING_CONF=/app/config.toml

# Copy project files into container
COPY . /app

# Check if client_secrets.json is present, and generate if not
RUN apk add --update --no-cache curl
RUN chmod +x generate_client_secrets.sh
RUN ./generate_client_secrets.sh

RUN ./manage.py collectstatic --noinput

# Expose Django port
EXPOSE 8000
