import subprocess
import json
import requests
import socket
from datetime import datetime

def get_local_ip():
    # 获取本机IP地址
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 使用一个不存在的地址，目的是获取本地到该地址的路由IP
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def run_iperf_test(server_ip):
    # 使用 iperf3 进行测速，结果输出为 JSON 格式
    result = subprocess.run(["iperf3", "-c", server_ip, "-J"], capture_output=True, text=True)
    # 解析 JSON 结果
    if result.stdout:
        json_result = json.loads(result.stdout)
        return json_result
    else:
        print("iperf3 test failed or no output returned.")
        return None

if __name__ == '__main__':
    server_ip = '8.134.202.27'  # 替换成你的 iperf 服务器 IP
    local_ip = get_local_ip()
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{local_ip}_{current_time}.json"
    
    test_result = run_iperf_test(server_ip)
    if test_result:
        print(test_result)
        # 保存测试结果到文件
        with open(filename, 'w') as f:
            json.dump(test_result, f)
        
        # 上传文件
        try:
            with open(filename, 'rb') as f:
                files = {'file': (f.name, f)}
                response = requests.post(f"http://{server_ip}:5000/upload", files=files)
                print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Failed to upload results: {e}")
    else:
        print("No test result to upload.")
