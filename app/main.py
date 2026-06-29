from fastapi import FastAPI
import os

app = FastAPI(title="Cloud API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Cloud API - deployed via CI/CD pipeline", "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/info")
def info():
    return {
        "app": "cloud-api",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "local"),
    }
