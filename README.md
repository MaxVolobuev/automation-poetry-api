# PoetryDB API Test Suite

Automated REST API tests for [PoetryDB](https://github.com/thundercomb/poetrydb) and [JSONPlaceholder](https://jsonplaceholder.typicode.com) mock API, using Python, `requests`, and `pytest`.

---

## Test Cases

### PoetryDB (`GET` only)

| # | Test Case              | Endpoint                  | Expected Result                                     |
|---|------------------------|---------------------------|----------------------------------------------------|
| 1 | Get poems by author    | `/author/Shakespeare`     | 200 OK, list of poems, author = "Shakespeare"      |
| 2 | Search poems by word   | `/lines/hope`             | 200 OK, poems with lines containing "hope"         |

### Mock JSON API (`GET + POST`)

| # | Test Case              | Endpoint                  | Expected Result                                     |
|---|------------------------|---------------------------|----------------------------------------------------|
| 3 | Get a random user      | `/users`                  | 200 OK, user object                                |
| 4 | Create post for user   | `/posts` (POST)           | 201 Created, JSON matches input                    |

---

## Tools Used

- `Python 3.10+`
- `pytest`
- `requests`
- `.env` for config-based switching

---

## Config Structure

Environment configs are stored in `.env` and loaded via `config/config_loader.py`.

Example `.env`:

```
ENV=prod
```

Based on `ENV`, the config will load:

| ENV  | BASE_URL (Poetry)         | MOCK_API_URL (JSON Placeholder)      |
|------|----------------------------|---------------------------------------|
| dev  | https://dev.poetrydb.org   | https://jsonplaceholder.typicode.com |
| stg  | https://stg.poetrydb.org   | https://jsonplaceholder.typicode.com |
| prod | https://poetrydb.org       | https://jsonplaceholder.typicode.com |

You can modify the URLs in `config_loader.py` to point to your own mock servers if needed.

---

## Validation Approach

All tests validate:
- HTTP response codes (`200`, `201`)
- Response structure and data types (`list`, `dict`)
- Specific business logic (author match, keyword presence)

---

## ▶ How to Run Tests

### Install dependencies

```bash
git clone https://github.com/MaxVolobuev/automation-poetry-api
cd automation-poetry-api

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Create a .env file in the project root:
echo "ENV=prod" > .env
```

### One-line test run (recommended)

```bash
make test
```

---

## Project Structure

```
automation-poetry-api/
├── api/
│   ├── poetry_service.py
│   └── placeholder_service.py
├── config/
│   └── config_loader.py
├── tests/
│   ├── test_poetry_api.py
│   └── test_mock_post.py
├── .gitignore
├── Makefile
├── .env
├── requirements.txt
└── README.md
```

---

## For Contributors

If you add or update dependencies, please update `requirements.txt` using:

```bash
pip list --format=freeze > requirements.txt
```

> This ensures the file stays clean and only contains top-level project dependencies.

---

## Author

**Maksym Volobuiev**  
Made with ❤️ for automation and API design

---

## License

MIT — free to use, improve, share.  
Give credit if helpful
