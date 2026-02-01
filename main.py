from fastapi import FastAPI

app = FastAPI(title="FastAPI on Azure")

@app.get("/")
def read_root():
    return {
        "message": "FastAPI is running successfully on Azure App Service 🚀"
    }

@app.get("/health")
def health_check():
    return {"status": "OK"}
