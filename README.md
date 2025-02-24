# Resume Scorer

## Features:
1. **Semantic Similarity**: Uses Sentence Transformers to generate embeddings and compute the similarity between job descriptions and resumes. The LocalEmbeddingModel class uses the SentenceTransformer library to generate embeddings locally.

2. **Local Execution**: Runs entirely on your machine without needing any external API calls.
3. **Lightweight Model**: The model all-MiniLM-L6-v2 is a lightweight and efficient model for semantic similarity tasks.
5. **Open-Source and Free**: Sentence Transformers is free to use and open-source under the Apache 2.0 license.
6. **Pre-trained Models**: Offers a variety of pre-trained models optimized for semantic similarity.
### Alternative Models
   If you want to experiment with other models, you can replace the model_name in the LocalEmbeddingModel class with any of the following:
   - all-mpnet-base-v2: Higher accuracy, larger model. 
   - paraphrase-MiniLM-L6-v2: Optimized for paraphrase detection. 
   - multi-qa-MiniLM-L6-cos-v1: Optimized for question-answer retrieval.
8. **Performance Considerations**:
    - **Hardware Requirements**: Sentence Transformers models run efficiently on CPUs, but for faster performance, you can use a GPU (if available on your machine).
    - **Model Size**: Smaller models like all-MiniLM-L6-v2 are ideal

### Batch Processing
If processing many resumes, consider batching the embedding generation for better performance.

### Installation:
**Install Dependencies from requirements.txt:**
```bash
conda create --name new_env_name --file requirements.txt
````

**Install Dependencies from environment.yml (recommended):**
```bash
conda env create --file environment.yml
````
