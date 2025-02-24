from sentence_transformers import SentenceTransformer


class LocalEmbeddingModel:
    """
    all-mpnet-base-v2: Higher accuracy, larger model.
    paraphrase-MiniLM-L6-v2: Optimized for paraphrase detection.
    multi-qa-MiniLM-L6-cos-v1: Optimized for question-answer retrieval.
    all-MiniLM-L6-v2: are ideal for local execution, while larger models may require more resources.
    """
    def __init__(self, model_name='all-mpnet-base-v2'):
        # Load a pre-trained Sentence Transformer model
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text):
        # Generate embeddings using the local model
        return self.model.encode(text)