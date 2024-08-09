from haystack_integrations.components.retrievers.elasticsearch import ElasticsearchEmbeddingRetriever
from haystack_integrations.document_stores.elasticsearch import ElasticsearchDocumentStore

from haystack.document_stores.types import DuplicatePolicy
from haystack import Document, Pipeline
from haystack.components.embedders import SentenceTransformersTextEmbedder, SentenceTransformersDocumentEmbedder
import os
document_store = ElasticsearchDocumentStore(hosts= "http://localhost:9200/")

model = "BAAI/bge-large-en-v1.5"

data_path = "C:\\Users\\anubhav\\Desktop\\RAG-Pipeline\\data"
documents = []

for filename in os.listdir(data_path):
    if filename.endswith(".json"):
        with open(os.path.join(data_path, filename), 'r',encoding='utf-8') as file:
            content = file.read()
            documents.append(Document(content=content, meta={"filename": filename}))

document_embedder = SentenceTransformersDocumentEmbedder(model=model)  
document_embedder.warm_up()
documents_with_embeddings = document_embedder.run(documents)

document_store.write_documents(documents_with_embeddings.get("documents"), policy=DuplicatePolicy.SKIP)

query_pipeline = Pipeline()
query_pipeline.add_component("text_embedder", SentenceTransformersTextEmbedder(model=model))
query_pipeline.add_component("retriever", ElasticsearchEmbeddingRetriever(document_store=document_store))
query_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")

query = "Tell me latest movies?"

result = query_pipeline.run({"text_embedder": {"text": query}})

output = result['retriever']['documents'][0]
print(output.)