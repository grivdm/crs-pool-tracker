from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "crs-pool-tracker"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
