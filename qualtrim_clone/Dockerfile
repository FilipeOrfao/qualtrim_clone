FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /usr/src/qualtrim_clone/

# Install dependencies
COPY requirements.txt /usr/src/qualtrim_clone/requirements.txt
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /qualtrim_clone/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]