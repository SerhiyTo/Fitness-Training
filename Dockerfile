FROM python:3.11.4

ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /usr/src/app

# Copy project files into the container
COPY pyproject.toml poetry.lock /usr/src/app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install

# Copy the project code into the container
COPY . .
