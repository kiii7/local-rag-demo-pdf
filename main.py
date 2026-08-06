from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
import gradio as gr

PDF_FILE = "rag_test_doc.pdf"
MODEL_NAME = "qwen2:1.5b"
EMBED_MODEL = "shibing624/text2vec-base-chinese"
TOP_K = 4

#加载PDF
loader = PyPDFLoader(PDF_FILE)
documents = loader.load()
print(f"✅读取PDF页数：{len(documents)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=80
)
split_docs = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
db = FAISS.from_documents(split_docs, embeddings)
retriever = db.as_retriever(search_kwargs={"k": TOP_K})
llm = Ollama(model=MODEL_NAME)


def chat(user_query):
    docs = retriever.invoke(user_query)
    context = "\n".join([d.page_content for d in docs])
    print(f"====检索上下文====\n{context}\n")

    prompt = f"""只能依据下面【文档】内容回答。
文档没有答案就输出：文档中没有找到相关信息。
禁止使用外部知识，禁止编造。

【文档】
{context}

问题：{user_query}
回答：
"""
    ans = llm.invoke(prompt)
    return ans.strip()


demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="输入问题"),
    outputs=gr.Textbox(label="回答"),
    title="本地RAG‑PDF问答Demo"
)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)