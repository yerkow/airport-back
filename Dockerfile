FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN python -m venv /venv

RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 8003

ENV PATH="/venv/bin:$PATH"
ENV FLASK_APP=scrapper.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8003"]
