FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY script.py script.py
COPY healthcheck.py healthcheck.py

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD python healthcheck.py || exit 1

CMD ["python", "script.py"]
