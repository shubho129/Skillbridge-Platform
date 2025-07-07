FROM python:3.10-slim
WORKDIR /code
COPY . .
RUN pip install fastapi uvicorn pydantic
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
