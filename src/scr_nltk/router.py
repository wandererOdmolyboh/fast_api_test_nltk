import nltk
from fastapi import APIRouter, HTTPException

from src.scr_nltk.schema import Token

router = APIRouter(tags=["ntlk"])


@router.post("/tokenize")
async def tokenize(data: Token):
    try:
        data = nltk.word_tokenize(data.text)

        return {"tokens": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/pos_tag")
async def pos_tag_text(data: Token):
    try:
        tokens = nltk.word_tokenize(data.text)
        pos_tags = nltk.pos_tag(tokens)

        return {"pos_tags": pos_tags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ner")
async def ner_text(data: Token):

    tokens = nltk.word_tokenize(data.text)
    tagged_tokens = nltk.pos_tag(tokens)
    entities_tree = nltk.ne_chunk(tagged_tokens)

    entities = []
    for subtree in entities_tree.subtrees():
        entity_name = ' '.join(c[0] for c in subtree.leaves())
        entity_type = subtree.label()
        entities.append((entity_name, entity_type))

    return {"entities": entities}
