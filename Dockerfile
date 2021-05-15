FROM python:3.8
LABEL MAINTAINER="mojtaba nafez | @mojtaba_nafez"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /consultant
WORKDIR /consultant
COPY . /consultant

# Installing requirements
ADD requirements.txt /consultant
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "Consultant", "--bind", ":8000", "Consultant.wsgi:application"]