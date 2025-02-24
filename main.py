import os

from src.resume_scorer import ResumeScorer


if __name__ == "__main__":
    frontend = "data/job_description/frontend1.txt"
    backend = "data/job_description/backend1.txt"
    with open(frontend) as f:
        job_description = f.read()

    resume_directory = "data/resumes/"
    resume_paths = [os.path.join(resume_directory, f) for f in os.listdir(resume_directory) if f.endswith('.pdf')]

    scorer = ResumeScorer(job_description)
    results = scorer.score_resumes(resume_paths)

    print("Ranking of resumes:")
    for idx, (path, score) in enumerate(results, 1):
        print(f"{idx}. {path}: {score:.4f}")