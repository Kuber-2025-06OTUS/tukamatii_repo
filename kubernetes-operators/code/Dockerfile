FROM python:3.12-slim
WORKDIR /app
RUN pip install kopf kubernetes pyyaml
COPY operator.py .
CMD ["kopf", "run", "operator.py", "--verbose"]
