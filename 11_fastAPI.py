
#* FastAPI in Python
# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
# It is designed to be easy to use and to provide automatic interactive API documentation.
# FastAPI leverages Python type hints to validate request data, serialize response data, and generate OpenAPI documentation automatically.

#* Key Features of FastAPI:
    # 1. High performance, on par with Node.js and Go.
    # 2. Automatic interactive API documentation (Swagger UI and ReDoc).
    # 3. Easy request validation and response serialization using Python type hints.
    # 4. Dependency injection system for managing components and services.
    # 5. Asynchronous support for handling concurrent requests efficiently.
    # 6. Easy integration with databases, authentication, and other web technologies.

#* Install
    # pip install "fastapi[standard]"    # includes uvicorn (the server) + extras

#* Running the app
    # uvicorn 11_fastAPI:app --reload
    #   - "11_fastAPI" is this file's name (module), "app" is the FastAPI() instance
    #   - --reload restarts the server automatically when code changes (dev only)
    # Then visit:
    #   http://127.0.0.1:8000          - the API itself
    #   http://127.0.0.1:8000/docs     - auto-generated interactive Swagger UI
    #   http://127.0.0.1:8000/redoc    - auto-generated ReDoc documentation
    # Both docs pages are built automatically from your type hints and
    # Pydantic models - no extra work needed.


from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Path, Depends, status
from pydantic import BaseModel


app = FastAPI()


#* Basic route - path operation decorators
# @app.get / @app.post / @app.put / @app.patch / @app.delete map directly
# to HTTP methods. The function below the decorator is called a
# "path operation function".
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


#* Fake in-memory "database" so the examples below have something to work with
fake_items_db = {
    1: {"name": "Keyboard", "price": 49.99, "in_stock": True},
    2: {"name": "Monitor", "price": 199.99, "in_stock": False},
}


#* Path parameters
# {item_id} in the route is captured as a function argument. The type
# hint (int) is used for automatic validation AND conversion - a
# request to /items/abc gets an automatic 422 error, no manual parsing
# needed.
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in fake_items_db:
        # HTTPException is how you return proper error responses -
        # this sends a 404 with a JSON body: {"detail": "Item not found"}
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]


#* Path parameter validation with Path()
# Use Path(...) to add constraints/metadata beyond just the type -
# here we require item_id to be at least 1.
@app.get("/items-validated/{item_id}")
def get_item_validated(item_id: int = Path(..., ge=1, description="The ID of the item")):
    return fake_items_db.get(item_id, {"error": "not found"})


#* Query parameters
# Any function parameter NOT part of the path is treated as a query
# parameter, e.g. /search?keyword=mon&limit=5
# Optional[str] = None makes it optional; giving it a default makes it
# optional automatically too.
@app.get("/search")
def search_items(keyword: Optional[str] = None, limit: int = 10):
    results = list(fake_items_db.values())
    if keyword:
        results = [item for item in results if keyword.lower() in item["name"].lower()]
    return results[:limit]


#* Query parameter validation with Query()
# Similar to Path(), but for query params - add constraints like
# min/max length, numeric ranges, regex patterns, etc.
@app.get("/search-validated")
def search_items_validated(
    keyword: str = Query(..., min_length=2, max_length=50),
    limit: int = Query(10, ge=1, le=100),
):
    results = [item for item in fake_items_db.values() if keyword.lower() in item["name"].lower()]
    return results[:limit]


#* Request body - plain dict vs Pydantic model
# A `dict` type hint (as below) works, but gives you NO validation and
# NO auto-generated docs about the expected shape - FastAPI has no idea
# what keys/types it should contain.
@app.post("/items/")
def create_item_raw(item: dict):
    return {"item": item}


# Prefer a Pydantic model instead (see 7_pydantic.py for the
# fundamentals). FastAPI reads the request body, validates it against
# this model, and gives you a typed Python object - invalid data gets
# an automatic 422 response listing exactly what's wrong, and the
# expected shape shows up correctly in /docs.
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True  # default value -> field becomes optional


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    new_id = max(fake_items_db.keys()) + 1
    fake_items_db[new_id] = item.model_dump()
    return {"id": new_id, **item.model_dump()}


#* Combining path params + query params + request body in one endpoint
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, notify: bool = False):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_items_db[item_id] = item.model_dump()
    return {"id": item_id, "notified": notify, **item.model_dump()}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_items_db[item_id]
    return {"deleted": item_id}


#* response_model - control/validate what gets sent back
# Even if your function returns extra internal fields, response_model
# filters the output to only the declared fields - useful for hiding
# internal data (e.g. password hashes) from API responses.
class ItemOut(BaseModel):
    name: str
    price: float


@app.get("/items/{item_id}/public", response_model=ItemOut)
def get_item_public(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]  # "in_stock" gets dropped automatically


#* Dependency Injection with Depends()
# A dependency is just a function FastAPI calls for you before the path
# operation runs, and its return value is injected as an argument.
# Common uses: shared pagination params, auth/current-user checks,
# database session handling.
def common_pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/items-paginated")
def list_items_paginated(pagination: dict = Depends(common_pagination)):
    values = list(fake_items_db.values())
    return values[pagination["skip"]: pagination["skip"] + pagination["limit"]]


#* async def vs def
# FastAPI supports both. Use `async def` when your endpoint does async
# I/O (e.g. `await` an async DB driver or HTTP call) so the server can
# handle other requests while waiting. Plain `def` endpoints are run in
# a threadpool automatically - fine for normal (sync/blocking) code.
@app.get("/async-example")
async def async_example():
    return {"message": "this endpoint is async"}


#* A note on testing FastAPI apps (ties back to pytest)
# FastAPI's TestClient (from fastapi.testclient) lets you call your API
# in-process - no real server needed - which makes it easy to write
# pytest tests for your endpoints, e.g.:
#
#   from fastapi.testclient import TestClient
#   client = TestClient(app)
#   def test_read_root():
#       response = client.get("/")
#       assert response.status_code == 200
#       assert response.json() == {"message": "Hello, World!"}


#* Quick sanity check without starting a real server
# Running this file directly (python3 11_fastAPI.py) exercises a few
# endpoints via TestClient so you can see they work without needing
# `uvicorn --reload` running. This is NOT how you'd normally use the
# app - normally you just run it with uvicorn as noted above.
if __name__ == "__main__":
    from fastapi.testclient import TestClient

    client = TestClient(app)

    print(client.get("/").json())
    print(client.get("/items/1").json())
    print(client.get("/items/999").status_code)  # 404
    print(client.post("/items/", json={"anything": "goes, no validation"}).json())
    print(client.post("/items", json={"name": "Mouse", "price": 25.5}).json())
    print(client.get("/items/1/public").json())  # in_stock dropped
