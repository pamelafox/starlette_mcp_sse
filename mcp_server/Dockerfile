FROM python:3.13
WORKDIR /code
EXPOSE 8000
COPY ./pyproject.toml /code/pyproject.toml

RUN pip install --no-cache-dir --upgrade uv

RUN uv pip install -r pyproject.toml

COPY ./src /code/src

CMD ["uv", "run", "start"]