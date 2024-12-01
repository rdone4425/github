import sys
import os
import asyncio

# 获取项目根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# 添加到 Python 路径
sys.path.insert(0, ROOT_DIR)

from GitHub.src.main import main

if __name__ == "__main__":
    try:
        # 设置项目根目录环境变量
        os.environ["GITHUB_MANAGER_ROOT"] = ROOT_DIR
        # 打印导入路径以便调试
        print("Python path:", sys.path)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程序已退出")
    except Exception as e:
        print(f"\n发生错误: {e}")
        import traceback
        traceback.print_exc() 