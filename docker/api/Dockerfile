# Base image
FROM python:3.8.10

ARG SENTRY_DSN
ARG IO_VERSION
ARG IO_STAGE
ARG MATOMO_ID
ARG MATOMO_TOKEN

ENV FLASK_API_SENTRY_DSN $SENTRY_DSN
ENV FLASK_API_VERSION $IO_VERSION
ENV FLASK_API_STAGE $IO_STAGE
ENV FLASK_API_MATOMO_ID $MATOMO_ID
ENV FLASK_API_MATOMO_TOKEN $MATOMO_TOKEN

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ America/Sao_Paulo
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8

RUN apt-get update

# locale
RUN export LANG=C.UTF-8
RUN apt-get install -y locales
RUN echo 'pt_BR.UTF-8 UTF-8' >> /etc/locale.gen
RUN locale-gen pt_BR.UTF-8

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY app.py /app
COPY requirements.txt /app
COPY serialized_files /app/serialized_files
COPY model_support /app/model_support

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]