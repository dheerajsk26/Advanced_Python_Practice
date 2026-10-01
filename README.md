# Advanced_Python_Practice

A personal collection of self-study notes and runnable examples covering core Python, OOP, and libraries/tools commonly used in data engineering work (Pydantic, FastAPI, pytest, the `os` module, API requests). Each file is heavily commented and meant to be read top-to-bottom as a mini reference, with small runnable snippets to try things out.

## Contents

| File | Topic |
|---|---|
| [1_fundamentals_of_python.py](1_fundamentals_of_python.py) | Data types, built-in/method functions, string formatting & slicing, `random` module, `isinstance`, comparison operators, conditionals, loops, `match`-`case`, `break`/`continue`/`pass`, shallow vs. deep copy |
| [2_datastructures_in_python.py](2_datastructures_in_python.py) | Lists, tuples, sets, dictionaries, unpacking, `all`/`any`, `remove`/`pop`, iterables vs. iterators, `map`/`filter`/`zip`, lambda functions |
| [3_functions_in_python.py](3_functions_in_python.py) | User-defined functions, function types, `*args`/`**kwargs`, return statements, best practices |
| [4_decorators_&_generators.py](4_decorators_&_generators.py) | Decorators (incl. a timer decorator example), generators |
| [5_oops_in_python.py](5_oops_in_python.py) | Object-oriented programming: classes/objects, encapsulation, method types, polymorphism, duck typing |
| [6_multi_threading.py](6_multi_threading.py) | Multi-threading for I/O-bound tasks, the GIL |
| [7_pydantic.py](7_pydantic.py) | Data validation/parsing with Pydantic, type-hint-based schemas |
| [8_async_in_python.py](8_async_in_python.py) | `async`/`await`, concurrency for I/O-heavy workloads |
| [9_api_requests.py](9_api_requests.py) | Making HTTP requests with the `requests` library: GET/POST/PUT/PATCH/DELETE, query params, headers, auth, error handling, timeouts |
| [10_os_module.py](10_os_module.py) | The `os` module for filesystem work: paths, directories, environment variables, `os.walk`, file metadata — with a data-engineering lens (scanning/organizing data files) |
| [11_fastAPI.py](11_fastAPI.py) | Building APIs with FastAPI: path/query params, request bodies with Pydantic, validation, `response_model`, dependency injection, async endpoints, testing with `TestClient` |
| [data_engineering_principles.txt](data_engineering_principles.txt) | Notes on core data engineering principles (validation, idempotency, observability, incremental processing, etc.) |
| [practice_1.py](practice_1.py), [practice_2.py](practice_2.py) | Small scratch scripts (`__main__` entry point behavior, quick `os` checks) |
| [pytest_practice/](pytest_practice/) | Standalone pytest practice project — `main.py` (sample app code) + `test_main.py` (pytest notes: fixtures, parametrise, marks, `pytest.raises`, `capsys`, etc.) |

## Requirements

- Python 3.9+
- Third-party packages used across these files:
  ```bash
  pip install requests pytest "fastapi[standard]" pydantic
  ```

## Running the examples

Most files are standalone scripts:
```bash
python3 9_api_requests.py
python3 10_os_module.py
```

Pytest examples:
```bash
cd pytest_practice
pytest -v
```

FastAPI app (from the repo root):
```bash
uvicorn 11_fastAPI:app --reload
# then visit http://127.0.0.1:8000/docs
```

## Notes

- `__pycache__/`, `.pytest_cache/`, and `os_practice_sandbox/` are generated while running the examples and aren't meant to be tracked in git.
