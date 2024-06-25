from fastapi import APIRouter

from src.nltk.schema import Token

router = APIRouter(tags=["ntlk"])


@router.post("/tokenize")
async def tokenize(data: Token):
    test = ['text']
    return {"tokens": test}


@router.post("/pos_tag")
async def pos_tag_text(data: Token):
    return {"pos_tags": ''}


@router.post("/ner")
async def ner_text(data: Token):
    return {"entities": ''}
