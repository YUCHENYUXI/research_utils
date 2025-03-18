import os


def save_directory_structure(root_path, output_file, blacklist):
    """递归遍历目录，并以最简形式保存到 content.txt"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for dirpath, dirnames, filenames in os.walk(root_path):
            dirnames[:] = [d for d in dirnames if d not in blacklist]  # 过滤黑名单目录
            level = dirpath.replace(root_path, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f"{indent}{os.path.basename(dirpath)}/\n")
            sub_indent = ' ' * 4 * (level + 1)
            for filename in filenames:
                if filename not in blacklist:
                    f.write(f"{sub_indent}{filename}\n")


def is_text_file(file_path):
    """判断文件是否为文本文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(1024)  # 读取部分内容以判断是否为文本
        return True
    except:
        return False


def save_text_files(root_path, output_file, blacklist):
    """递归遍历目录，并将文本文件内容保存到 texts.txt"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for dirpath, dirnames, filenames in os.walk(root_path):
            dirnames[:] = [d for d in dirnames if d not in blacklist]  # 过滤黑名单目录
            for filename in filenames:
                if filename in blacklist:
                    continue
                file_path = os.path.join(dirpath, filename)
                if is_text_file(file_path):
                    relative_path = os.path.relpath(file_path, root_path)
                    f.write(f"{relative_path}\n")
                    # f.write("新文件："f"{relative_path}\n")
                    with open(file_path, 'r', encoding='utf-8') as file:
                        # f.write("\n文件开始\n"+file.read() + "\n文件结束\n")
                        f.write(file.read())


def main(repo_path):
    # repo_path = input("请输入本地代码仓库路径: ").strip()
    if not os.path.isdir(repo_path):
        print("错误: 请输入有效的目录路径！")
        return

    blacklist = {'.git', 'node_modules', '__pycache__', '.idea', '.vscode'}  # 黑名单目录和文件
    save_directory_structure(repo_path, 'content.txt', blacklist)
    save_text_files(repo_path, 'texts.txt', blacklist)
    print("处理完成，目录结构已保存至 content.txt，文本文件内容已保存至 texts.txt")


if __name__ == "__main__":
    repo_path = r"A:\OpenPAR\VTFPAR++"
    main(repo_path)
