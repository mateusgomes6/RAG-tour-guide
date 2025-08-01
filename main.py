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
    
    def generate_itinerary(self, days, interests, budget):
        prompt = f"""Crie um roteiro de {days} dias para um turista interessado em {interests} 
        com orçamento {budget}. Inclua atrações principais, dicas de transporte, 
        sugestões de restaurantes e horários recomendados."""
        
        response = self.qa_chain({"query": prompt})
        return response['result']
    
    def get_attraction_info(self, attraction_name):
        prompt = f"""Forneça informações detalhadas sobre {attraction_name}, incluindo:
        - Descrição histórica
        - Horário de funcionamento
        - Preços de ingressos
        - Dicas de visitação
        - Avaliações de visitantes"""
        
        response = self.qa_chain({"query": prompt})
        return response['result']