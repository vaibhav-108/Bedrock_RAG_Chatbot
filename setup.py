from setuptools import find_packages, setup

setup(
    name="qasystem",
    version="0.0.1",
    author="vaibhav-108",
    author_email="vaibhav.b108@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchainhub","langchain_aws","bs4","tiktoken","openai","boto3==1.38.3","langchain_community","chromadb","awscli",
"streamlit",
"pypdf",
"faiss-cpu"]
)
    