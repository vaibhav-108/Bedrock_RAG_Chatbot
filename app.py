import json
import os 
import sys
import boto3
import streamlit as st

from langchain_aws import BedrockLLM,BedrockEmbeddings


from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains import retrieval_qa

from langchain_community.vectorstores import FAISS

from QA_system.ingestion import data_ingestion,get_vector_store

from QA_system.retrieval_generation import get_llama2_llm,get_response_llm

bedrock=boto3.client(service_name="bedrock-runtime",region_name="us-east-1")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0",client=bedrock)

def main():
    st.set_page_config("QA with DOC")
    st.header("QA with doc using langchain and bedrock")
    
    user_question=st.text_input("Ask a question from the pdf files")
    
    
    with st.sidebar:
        st.title("update or create the vector store")
        if st.button("vectors update"):
            with st.spinner("processing..."):
                docs=data_ingestion()
                get_vector_store(docs)
                st.success("done")
        if st.button("llama model"):
            with st.spinner("processing..."):
                faiss_index=FAISS.load_local("faiss_index",bedrock_embeddings,allow_dangerous_deserialization=True)
                llm=get_llama2_llm()
                
                st.write(get_response_llm(llm,faiss_index,user_question))
                st.success("Done")
                
    

if __name__=="__main__":
    main()