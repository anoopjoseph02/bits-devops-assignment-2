FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV FLASK_APP=aceest.__init__:create_app
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "aceest.__init__:create_app()"]
