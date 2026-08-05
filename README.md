\# 简易本地RAG Demo

零云API，完全本地运行，基于PDF文档做知识库问答。



\## 技术栈

\- Python、LangChain、FAISS向量库

\- Ollama本地大模型



\## 项目功能

1.加载PDF文档，文本切分

2.本地构建向量库

3.基于文档内容问答，只回答PDF内的信息



\## 运行说明

1.安装项目依赖

2.自行下载 qwen2‑1\_5b‑instruct‑q4\_k\_m.gguf 放到项目根目录

3.执行 python rag\_demo.py



> 注意：本仓库不携带大模型权重文件，需要使用者自行下载模型。

