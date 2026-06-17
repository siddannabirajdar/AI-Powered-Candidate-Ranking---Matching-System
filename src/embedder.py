from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


# Load model once at startup

MODEL_NAME = (
    "BAAI/bge-base-en-v1.5"
)

model = SentenceTransformer(
    MODEL_NAME
)


def get_embedding(text):

    return model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )


def similarity(text1, text2):

    emb1 = get_embedding(
        text1
    )

    emb2 = get_embedding(
        text2
    )

    score = cosine_similarity(
        [emb1],
        [emb2]
    )[0][0]

    return float(score)