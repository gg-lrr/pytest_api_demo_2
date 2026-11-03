import requests
from common.utils import logger

class HttpClient:
    def __init__(self, base_url):
        # 初始化，传入域名
        self.base_url = base_url
        # session会话：自动维持cookie、登录态，适合需要token的接口
        self.session = requests.Session()
        # 默认请求头，json格式
        self.headers = {"Content-Type": "application/json"}

    def send(self, path, method, **kwargs):
        """
        统一发送请求方法
        :param path: 接口路径 /get
        :param method: 请求方式 GET POST
        :param kwargs: 可变参数，可以传params / json
        :return: response响应对象
        """
        url = self.base_url + path
        logger.info(f"【请求地址】：{url}")
        logger.info(f"【请求参数】：{kwargs}")
        resp = self.session.request(method=method, url=url, headers=self.headers, **kwargs)
        logger.info(f"【响应码】：{resp.status_code},【响应结果】：{resp.json()}")
        return resp