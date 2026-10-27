
# 1. Start with a Python environment
FROM python:3.12-slim

# 2. Configure Python for container execution
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Set the application's working directory
WORKDIR /app

# 4. Copy dependencies first to improve build caching
COPY requirements.txt .

# 5. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the application source code
COPY app/ ./app/

# 7. Create a non-root user and a writable data directory
RUN groupadd --system appuser \
    && useradd --system --gid appuser \
       --home-dir /home/appuser --create-home appuser \
    && mkdir -p /app/data \
    && chown appuser:appuser /app/data

# 8. Run the application without root privileges
USER appuser

# 9. Document the application's listening port
EXPOSE 8000

# 10. Start FastAPI using Uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
