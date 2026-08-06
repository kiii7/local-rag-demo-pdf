✨项目介绍
基于 Python + LangChain + Ollama + FAISS + Gradio 搭建，所有模型全部本地运行，不调用任何第三方云端接口。
支持 PDF 文档解析、文本分块
FAISS 本地向量库存储文档向量
检索文档片段，结合本地大模型生成回答
Gradio 网页交互界面，开箱即用
🛠环境要求
安装 Ollama，后台服务正常启动
本地拉取模型：ollama pull qwen2:1.5b
Python >=3.10
📦安装依赖
bash
git clone https://github.com/kiii7/local-rag-demo-pdf.git
cd local-rag-demo-pdf
pip install -r requirements.txt
🚀运行项目
将你的 PDF 文档放到项目根目录，重命名为 rag_test_doc.pdf
确认 Ollama 程序处于开启状态
执行启动命令
bash
python main.py
浏览器打开 Gradio 给出本地地址，即可基于 PDF 文档进行问答。
📁项目结构
plaintext
local‑rag‑demo‑pdf
├── main.py              # 主程序
├── rag_test_doc.pdf     # 测试PDF知识库
├── requirements.txt     # 依赖清单
├── .gitignore           # 忽略向量缓存、临时文件
└── README.md            # 项目说明
faiss_db、vector_store 等向量缓存目录会被.gitignore过滤，不会提交到仓库。
💡测试提问示例
文档里面核心观点是什么？
根据文档内容，简述流程步骤。
⚠️只会回答 PDF 文档内存在的内容，超出文档范围会如实告知。
📝技术栈
Python LangChain Ollama FAISS Sentence‑Transformers Gradio
📌注意事项
Ollama 必须保持后台运行，否则程序连接失败
更换 PDF 文件后，需要重启程序，重新生成向量库
