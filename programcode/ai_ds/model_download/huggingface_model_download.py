# 模型名称，例如 "shibing624/text2vec-base-chinese"
model_name = "stabilityai/sd-turbo"

from huggingface_hub import snapshot_download
snapshot_download(
   repo_id=model_name,
   local_dir="D:\\workspace\\code\\Huggingface_model\\sd-turbo",
   endpoint="https://hf-mirror.com"
)