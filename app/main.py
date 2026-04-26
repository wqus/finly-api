from fastapi import FastAPI

app = FastAPI(title='finly-api')

@app.get('/health')
async def health():
    return {"status": "ok"}