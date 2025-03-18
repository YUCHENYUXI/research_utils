import os
import hashlib


def get_file_hash(file_path, algorithm='sha256', chunk_size=8192):
    """计算文件的哈希值，支持多种哈希算法"""
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"无法读取文件 {file_path}: {e}")
        return None


def find_duplicate_files(target_file, search_path, algorithm='sha256'):
    """查找与目标文件相同内容的文件"""
    if not os.path.isfile(target_file):
        print(f"错误: {target_file} 不是一个有效的文件。")
        return []

    target_hash = get_file_hash(target_file, algorithm)
    if target_hash is None:
        return []

    duplicates = []
    for root, _, files in os.walk(search_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path == target_file:
                continue  # 跳过自身

            file_hash = get_file_hash(file_path, algorithm)
            if file_hash == target_hash:
                duplicates.append(file_path)

    return duplicates


if __name__ == "__main__":
    target_file = r"P:\PAR\pad_mars_dataset\pad_mars_dataset\0001C1T00010001C1T0001F001.jpg"  # 目标文件路径
    search_path = r"P:\PAR\pad_mars_dataset"  # 需要搜索的目录

    duplicates = find_duplicate_files(target_file, search_path)
    if duplicates:
        print("找到相同的文件:")
        for dup in duplicates:
            print(dup)
    else:
        print("未找到相同的文件。")
