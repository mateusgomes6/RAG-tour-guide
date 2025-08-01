from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class TourismRAG:
    def __init__(self, vector_db):
        self.retriever = vector_db.as_retriever(search_kwargs={"k": 3})
        
        template = """Você é um guia de turismo especializado. Use as seguintes informações para responder à pergunta.
        Contexto: {context}
        Pergunta: {question}
        Resposta:"""
        
        self.qa_prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
        
        self.llm = OpenAI(temperature=0.7)
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            chain_type_kwargs={"prompt": self.qa_prompt},
            return_source_documents=True
        )