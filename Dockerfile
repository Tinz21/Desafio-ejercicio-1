FROM python:3-alpine3.12

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP="run.py"
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]