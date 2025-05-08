from mcp.server.fastmcp import FastMCP
import requests
import json

def get_quill_generation(context: str) -> str:
    request_data = {
        "text":context        
    }
    try:
        response = requests.post(
            'http://47.98.193.198:80/api/quill',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(request_data)
        )

        # 检查响应状态
        response.raise_for_status()

        # 获取 JSON 响应内容
        response_data = response.json()
        print("响应数据：", response_data)

    except requests.exceptions.RequestException as e:
        print("请求出错：", e)

    return response_data

mcp = FastMCP("QUILL_MCP_SERVER")

@mcp.tool(
    description="This tool is used to get the generation of a quotation from a context.",
)
def generation(context: str) -> str:
    """
    This tool is used to get the generation of a quotation from a context.
    """
    return get_quill_generation(context) 

if __name__ == "__main__":
    mcp.run()