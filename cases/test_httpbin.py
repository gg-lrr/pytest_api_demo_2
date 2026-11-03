import pytest
from common.http_client import HttpClient
from common.utils import read_yaml, get_env_config

# 读取环境域名
env_cfg = get_env_config()
# 实例化请求客户端
client = HttpClient(base_url=env_cfg["base_url"])
# 读取yaml里全部用例
case_data = read_yaml("data/case_data.yaml")

def get_value_by_key(data, key_path):
    """
    解析 a.b.c 这种层级字符串，逐层取json里面的值
    例如 args.name → 先取args，再取name
    """
    keys = key_path.split(".")
    res = data
    for k in keys:
        res = res[k]
    return res

# 参数化：自动遍历yaml里所有用例，一条case_name执行一次
@pytest.mark.parametrize("case_name", case_data.keys())
def test_api(case_name):
    case = case_data[case_name]
    resp = client.send(
        path=case["url"],
        method=case["method"],
        params=case.get("params"),
        json=case.get("json")
    )
    # 断言1：接口返回状态码200
    assert resp.status_code == 200
    # 获取实际返回字段
    actual = get_value_by_key(resp.json(), case["assert_key"])
    # 断言2：返回值等于预期值
    assert actual == case["assert_value"]