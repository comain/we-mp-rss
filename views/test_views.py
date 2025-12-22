#!/usr/bin/env python3
"""
测试网页预览功能
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from views.home import home_view
from views.articles import articles_view, article_detail_view
from fastapi import Request
from starlette.testclient import TestClient

# 创建测试请求
def create_test_request(path: str, query_params: dict = None):
    """创建测试请求对象"""
    class MockRequest:
        def __init__(self, path: str, query_params: dict = None):
            self.path = path
            self.query_params = query_params or {}
            self.base_url = "http://localhost:8001"
    
    return MockRequest(path, query_params)

async def test_home_view():
    """测试首页"""
    print("测试首页...")
    try:
        request = create_test_request("/views/home")
        response = await home_view(request, page=1, limit=10)
        print(f"✅ 首页测试成功，状态码: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ 首页测试失败: {e}")
        return False

async def test_articles_view():
    """测试文章列表"""
    print("测试文章列表...")
    try:
        request = create_test_request("/views/articles")
        response = await articles_view(
            request, 
            page=1, 
            limit=10,
            mp_id=None,
            tag_id=None,
            keyword=None,
            sort="publish_time",
            order="desc"
        )
        print(f"✅ 文章列表测试成功，状态码: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ 文章列表测试失败: {e}")
        return False

if __name__ == "__main__":
    import asyncio
    
    print("开始测试网页预览功能...")
    print("=" * 50)
    
    async def main():
        home_ok = await test_home_view()
        articles_ok = await test_articles_view()
        
        print("=" * 50)
        if home_ok and articles_ok:
            print("🎉 所有测试通过！")
        else:
            print("⚠️ 部分测试失败，请检查错误信息")
    
    asyncio.run(main())