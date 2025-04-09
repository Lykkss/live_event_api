FROM python:3.12-slim

# Create and set the work directory
WORKDIR /app

# Copy dependency list and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run migrations and start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]