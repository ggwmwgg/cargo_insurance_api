FROM python:3
ENV PYTHONUNBUFFERED=1
LABEL authors="GGwM"
WORKDIR /cargo_insurance
COPY . /cargo_insurance
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]