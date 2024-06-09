FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Install telnet and netcat-traditional
RUN apt-get update && apt-get install -y telnet netcat-traditional

# Add the wait-for-it script
COPY entrypoint.sh /entrypoint.sh
COPY scripts/seed_db.py seed_db.py

RUN chmod +x /entrypoint.sh

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app/src

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
