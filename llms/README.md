# 1. LangChain

LangChain开发入门教程

## DeepSeek 配置

教程中的聊天与工具调用通过 DeepSeek 的 OpenAI 兼容接口运行。当前 `langchain-stu` 环境已在环境内保存密钥，打开 Notebook 即可使用（默认内核为 `Python (langchain-stu)`）。在其他环境中运行时，可在项目根目录的终端设置密钥：

```bash
conda activate langchain-stu
export DEEPSEEK_API_KEY="你的 DeepSeek API Key"
```

默认使用 `deepseek-flash`。如需切换，可设置 `DEEPSEEK_MODEL`。向量检索示例使用本地的 `BAAI/bge-small-zh-v1.5` 嵌入模型，无需另一个 API Key；首次使用会下载模型到 conda 环境的 `share/fastembed` 目录。

`langchain_tutorial` 下的 Notebook 在生成回答时统一调用 DeepSeek。文档加载、文本切分、向量化和检索仍在本地执行，得到的内容再交给 DeepSeek 完成问答或解释。每个 Notebook 的最后一个代码单元都展示了完整调用。

可用以下命令验证聊天调用：

```bash
python -c 'from llms.langchain_tutorial.deepseek import get_deepseek_chat; print(get_deepseek_chat().invoke("你好").content)'
```

## 1.1 Model I/O

- [prompt_templates.ipynb](https://github.com/QunBB/DeepLearning/tree/main/llms/langchain_tutorial/prompt_templates.ipynb)
- [llms.ipynb](https://github.com/QunBB/DeepLearning/tree/main/llms/langchain_tutorial/llms.ipynb)
- [chatmodel.ipynb](https://github.com/QunBB/DeepLearning/tree/main/llms/langchain_tutorial/chatmodel.ipynb)
- [output_parser.ipynb](https://github.com/QunBB/DeepLearning/tree/main/llms/langchain_tutorial/output_parser.ipynb)

## 2.2 RAG/Retrieval

- [document_loaders.ipynb](https://github.com/QunBB/DeepLearning/blob/main/llms/langchain_tutorial/document_loaders.ipynb)
- [text_splitter.ipynb](https://github.com/QunBB/DeepLearning/blob/main/llms/langchain_tutorial/text_splitter.ipynb)
- [embeddings.ipynb](https://github.com/QunBB/DeepLearning/blob/main/llms/langchain_tutorial/embeddings.ipynb)
- [vector_store.ipynb](https://github.com/QunBB/DeepLearning/blob/main/llms/langchain_tutorial/vector_store.ipynb)
- [retrievers.ipynb](https://github.com/QunBB/DeepLearning/blob/main/llms/langchain_tutorial/retrievers.ipynb)

## 3.3 Tools/Agents

- [tools_agents.ipynb](https://github.com/QunBB/DeepLearning/blob/main/llms/langchain_tutorial/tools_agents.ipynb)

# 2. LLM训练

## 2.1 复现DeepSeek-R1的思维链

- [sft+grpo微调](https://github.com/QunBB/DeepLearning/tree/main/llms/train/deepseek-train)
