import os
import time
from typing import List
from fastapi import FastAPI, WebSocket, Path
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

import dataaccess.session as database_session
from api.routers import test

prefix = "/v1"

# Setup FastAPI app
app = FastAPI(
    title="API Service",
    description="API Service",
    version="v1"
)

# Enable CORSMiddleware
# we want the middleware so the frontend and backend talk from different domains
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Custom exception hooks
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": str(exc)
        }
    )

# Application start/stop hooks


@app.on_event("startup")
async def startup():
    ...
    # Connect to database
    #await database_session.connect()



@app.on_event("shutdown")
async def shutdown():
    ...
    # Disconnect from database
    #await database_session.disconnect()

# Routes
@app.get(
    "/",
    summary="Index",
    description="Root api"
)
async def get_index():
    return {
        "message": "Welcome to the API Service"
    }

# Additional routers here
app.include_router(test.router, prefix=prefix)
