FROM svizor/zoomcamp-model:3.11.5-slim
LABEL authors="rd"

WORKDIR /app
COPY ["./Pipfile", "./Pipfile.lock", "./"]
RUN pip install pipenv
RUN pipenv install --system --deploy
COPY ["./homework5/predict.py", "./homework5/model1.bin", "./homework5/dv.bin", "./"]
EXPOSE 9696
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]

