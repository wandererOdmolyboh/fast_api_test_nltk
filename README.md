# fast_api_test_nltk
This is a FastAPI application that uses the Natural Language Toolkit (NLTK) for Named Entity Recognition (NER).
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Docker (optional)

### Installation
#### Clone the repository:
```shell
git clone https://github.com/wandererOdmolyboh/fast_api_test_nltk
```

```shell
cd fast_api_test_nltk
```
### Running the Application

You can run the application in two ways:

### 1. Running with Docker
```shell
  docker-compose up 
```
after you need wait)

### 2. Running with local
1.1. Create venv
```shell
python3 -m venv venv 
````
or
```shell
python -m venv venv 
```

```shell
source venv/bin/activate
```

1.2. Install the required Python packages:
```shell
pip install -r requirements.txt
```

1.3. Download the necessary NLTK data:
```python
python tests/download_data.py
```

1.4. Using Uvicorn:
```shell
uvicorn src.main:app --reload
```

how check:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

