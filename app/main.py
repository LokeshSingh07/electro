from fastapi import FastAPI, Request
from app.config.db import check_db_connection, Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app.config.env import settings
from time import time
from app.routers.auth import router as auth_router

app = FastAPI(
    title="My FastAPI Application",
    description="FastAPI Backend API",
    version="1.0.0"
)



# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)



# Custom middleware -> GLOBAL
@app.middleware("http")
async def request_logger(req: Request, call_next):
    start_time  = time()
    print(f"--> {req.method} {req.url.path}")

    # Pass request to next middleware / route
    response = await call_next(req)

    # After request
    process_time = time() - start_time

    # Add custom response header
    response.headers["X-Process-Time"] = str(
        round(process_time, 4)
    )

    return response




# API ROUTES


app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Auth v1"]
)




# default route
@app.get("/")
def home(req: Request):
    is_connected = check_db_connection()
    port = req.url.port

    if not is_connected:
        message = f"Server is running on PORT {port} but Database connection failed"
    else:
        message = f"Server is running on PORT {port} & Database connected successfully"

    return {
        "message": message,
        "db_status": "Connected" if is_connected else "Failed"
    }




