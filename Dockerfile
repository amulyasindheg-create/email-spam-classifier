FROM python:3.9

WORKDIR /app

COPY inference.py /app/inference.py

RUN pip install numpy openai gradio==4.44.1 huggingface_hub==0.23.5

CMD ["python", "inference.py"]
