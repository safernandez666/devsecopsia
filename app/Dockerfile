FROM python:3.9-slim

WORKDIR /app

# Variables de build
ARG CI_COMMIT_SHORT_SHA=dev
ARG CI_COMMIT_SHA=local
ARG CI_PIPELINE_ID=N/A
ARG CI_PIPELINE_URL=#
ARG CI_JOB_ID=N/A
ARG CI_COMMIT_MESSAGE="Local build Mac"
ARG CI_COMMIT_AUTHOR="Developer"

ENV CI_COMMIT_SHORT_SHA=${CI_COMMIT_SHORT_SHA} \
    CI_COMMIT_SHA=${CI_COMMIT_SHA} \
    CI_PIPELINE_ID=${CI_PIPELINE_ID} \
    CI_PIPELINE_URL=${CI_PIPELINE_URL} \
    CI_JOB_ID=${CI_JOB_ID} \
    CI_COMMIT_MESSAGE=${CI_COMMIT_MESSAGE} \
    CI_COMMIT_AUTHOR=${CI_COMMIT_AUTHOR}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

# ⭐ Usar Gunicorn en vez de Flask dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]