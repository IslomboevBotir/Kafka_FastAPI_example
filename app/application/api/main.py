from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title='Kafka messages Chart',
        docs_url="/api/docs",
        description="DDD example + Kafka Messages API",
        debug=True
    )
    return app
