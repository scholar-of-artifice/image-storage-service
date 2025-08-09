from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    print("root => ")
    message = "Hello from image-storage-service!"
    return {"message": message}
