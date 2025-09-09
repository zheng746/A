import random
import json
import os


class UserManager:
    def __init__(self):
        self.current_user = None
        self.data_file = "current_user.txt"

    def generate_random_phone(self):
        """生成随机手机号"""
        phone = f"134{random.randint(10000000, 99999999)}"
        if self.current_user is None:
            self.current_user = {}
        self.current_user['phone'] = phone
        self.current_user['password'] = '123456'
        return phone

    def save_user_info(self):
        """保存用户信息到文件"""
        if self.current_user:
            try:
                with open(self.data_file, "w", encoding='utf-8') as f:
                    json.dump(self.current_user, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"保存用户信息时出错: {e}")

    def load_user_info(self):
        """从文件加载用户信息"""
        try:
            with open(self.data_file, "r", encoding='utf-8') as f:
                content = f.read().strip()
                if content:  # 检查文件是否为空
                    self.current_user = json.loads(content)
                    return self.current_user
                else:
                    return None
        except FileNotFoundError:
            return None
        except json.JSONDecodeError as e:
            print(f"JSON解码错误: {e}")
            print("文件内容可能不是有效的JSON格式，将删除文件并重新创建")
            # 删除损坏的文件
            if os.path.exists(self.data_file):
                os.remove(self.data_file)
            return None
        except Exception as e:
            print(f"加载用户信息时出错: {e}")
            return None


# 创建全局实例
user_manager = UserManager()
