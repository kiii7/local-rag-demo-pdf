from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA

# 1.配置本地模型，确保ollama已经拉取模型，例如 ollama pull qwen2:1.5b-instruct
embedding = OllamaEmbeddings(model="all-minilm")
llm = OllamaLLM(model="qwen2:1.5b-instruct")
# 2.加载pdf，把你的pdf文件名改成这里，例如demo.pdf
loader = PyPDFLoader("demo.pdf")
docs = loader.load()

# 3.文档切分
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
split_docs = text_splitter.split_documents(docs)

# 4.FAISS构建向量库（无sqlite依赖）
vector_db = FAISS.from_documents(split_docs, embedding)
vector_db.save_local("faiss_index")

# 5.检索问答链
retriever = vector_db.as_retriever(search_kwargs={"k":3})
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 交互循环
print("====本地RAG已就绪，输入问题提问，exit退出====")
while True:
    question = input("\n请输入问题：")
    if question.strip() == "exit":
        break
    res = qa_chain.invoke({"query": question})
    print("\n回答：", res["result"])