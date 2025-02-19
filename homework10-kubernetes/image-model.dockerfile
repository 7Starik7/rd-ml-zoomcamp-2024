FROM emacski/tensorflow-serving:2.5.1

COPY clothing-model /models/clothing-model/1
ENV MODEL_NAME="clothing-model"