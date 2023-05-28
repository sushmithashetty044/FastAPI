
1.Install fastAPI
    pip install fastapi
    Also install uvicorn to work as the server
    pip install "uvicorn[standard]

2.The basis to follow:
    Import FastAPI.
    Create an app instance.
    Write a path operation decorator (like @app.get("/")).
    Write a path operation function (like def root(): ... above).
    Run the development server (like uvicorn main:app --reload).


