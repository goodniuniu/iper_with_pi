import subprocess
import json

def run_iperf_test(server_ip):
    # 使用 iperf3 进行测速，结果输出为 JSON 格式
    result = subprocess.run(["iperf3", "-c", server_ip, "-J"], capture_output=True, text=True)
    # 解析 JSON 结果
    json_result = json.loads(result.stdout)
    return json_result

# 替换成你的 iperf 服务器 IP
server_ip = '8.134.202.27'
test_result = run_iperf_test(server_ip)
print(test_result)
