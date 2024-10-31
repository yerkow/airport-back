FROM python:3.12

WORKDIR /app

COPY . /app

# Create and activate a virtual environment
RUN python -m venv /venv

# Install dependencies
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose port 8003
EXPOSE 8003

# Set environment variables for the virtual environment and Flask app
ENV PATH="/venv/bin:$PATH"
ENV FLASK_APP=scrapper.py

# Start the app by directly running scrapper.py
CMD ["python", "scrapper.py"]
