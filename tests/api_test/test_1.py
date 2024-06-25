import nltk
import pytest
from starlette import status
from fastapi.testclient import TestClient

from src.main import app

nltk.download('all')

client = TestClient(app)


@pytest.mark.asyncio
async def test_post_tokenize():
    test_text = 'Apple Inc. is planning to open a new store in San Francisco.'
    test_data = {
        'text': test_text
    }

    response = client.post("/tokenize/", json=test_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()

    assert data.get("text") is not None

    control_tokens = nltk.word_tokenize(test_text)
    assert data["text"] == control_tokens


@pytest.mark.asyncio
async def test_post_pos_tag():
    test_text = 'Barack Obama was the President of the United States.'
    test_data = {
        'text': test_text
    }

    response = client.post("/pos_tag/", json=test_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()

    assert data.get("pos_tags") is not None

    control_tokens = nltk.word_tokenize(data.text)
    control_pos_tags = nltk.pos_tag(control_tokens)
    assert data["pos_tag"] == control_pos_tags

@pytest.mark.asyncio
async def test_post_pos_tag():
    test_text = "Apple Inc. is planning to open a new store in San Francisco."
    test_data = {
        'text': test_text
    }

    response = client.post("/pos_tag/", json=test_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()

    assert data.get("pos_tags") is not None

    control_tokens = nltk.word_tokenize(data.text)
    control_pos_tags = nltk.pos_tag(control_tokens)
    assert data["pos_tag"] == control_pos_tags
