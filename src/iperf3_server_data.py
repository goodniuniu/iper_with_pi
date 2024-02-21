import json
from datetime import datetime

def log_test_result(result, filename="iperf_results.json"):
    # 添加时间戳和测试来源地址
    result['test_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result['source_address'] = result['start']['connected'][0]['local_host']
    # 将结果追加到文件
    with open(filename, "a") as file:
        json.dump(result, file)
        file.write('\n')

log_test_result(test_result)
