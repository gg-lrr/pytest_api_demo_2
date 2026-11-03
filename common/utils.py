import yaml
import os
from loguru import logger

# 获取项目根目录，解决本地Windows、CI的Linux路径不一致的报错
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_yaml(file_path):
    """
    读取yaml文件通用方法
    :param file_path: 文件相对路径，例如 "config/env.yaml"
    :return: 解析后的字典
    """
    full_path = os.path.join(BASE_PATH, file_path)
    with open(full_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_env_config():
    """读取当前选中环境的base_url域名"""
    env_data = read_yaml("config/env.yaml")
    env_name = env_data["current_env"]
    return env_data[env_name]

# 日志配置：日志保存到report/run.log，文件超过500KB自动分割
logger.add("report/run.log", rotation="500KB", encoding="utf-8")