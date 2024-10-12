# fastapi
from fastapi import FastAPI
from app.core.modules import init_routers, make_middleware

import os


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="fastapi-starter",
        description="fastapi-starter that is needed for every fastapi project.",
        version="1.0.0",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
        docs_url=None if os.getenv("APP_ENV") == "production" else "/docs",  # is enabled?  /docs
        redoc_url=None if os.getenv("APP_ENV") == "production" else "/redoc",  # is enabled? /redoc
    )
    init_routers(app_=app_)
    return app_


app = create_app()
