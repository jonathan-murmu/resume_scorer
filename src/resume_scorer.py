from sklearn.metrics.pairwise import cosine_similarity

from src.embedding_model import LocalEmbeddingModel
from src.pdf_parser import PDFParser


class ResumeScorer:
    def __init__(self, job_description):
        self.embedding_model = LocalEmbeddingModel()
        self.job_desc = job_description
        self.job_embedding = None

    def _get_similarity(self, resume_embedding):
        return cosine_similarity(
            [self.job_embedding],
            [resume_embedding]
        )[0][0]

    def score_resumes(self, resume_paths):
        # Get job description embedding
        self.job_embedding = self.embedding_model.get_embedding(self.job_desc)

        # Process resumes
        scores = []
        for path in resume_paths:
            try:
                text = PDFParser.extract_text(path)
                resume_embedding = self.embedding_model.get_embedding(text)
                similarity = self._get_similarity(resume_embedding)
                scores.append((path, similarity))
            except Exception as e:
                print(f"Error processing {path}: {str(e)}")

        # Sort by descending score
        return sorted(scores, key=lambda x: x[1], reverse=True)