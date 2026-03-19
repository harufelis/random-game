import sys
import os


def print_usage():
    print("使い方:")
    print("  reverse inputpath outputpath")
    print("  copy inputpath outputpath")
    print("  duplicate-contents inputpath n")
    print("  replace-string inputpath needle newstring")


def validate_input_file(path):
    if not os.path.exists(path):
        print(f"エラー: 入力ファイル '{path}' は存在しません。")
        sys.exit(1)

    if not os.path.isfile(path):
        print(f"エラー: '{path}' はファイルではありません。")
        sys.exit(1)


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, contents):
    with open(path, "w", encoding="utf-8") as f:
        f.write(contents)


def reverse_file(inputpath, outputpath):
    validate_input_file(inputpath)
    contents = read_file(inputpath)
    reversed_contents = contents[::-1]
    write_file(outputpath, reversed_contents)


def copy_file(inputpath, outputpath):
    validate_input_file(inputpath)
    contents = read_file(inputpath)
    write_file(outputpath, contents)


def duplicate_contents(inputpath, n):
    validate_input_file(inputpath)

    if not n.isdigit():
        print("エラー: n は 0 以上の整数である必要があります。")
        sys.exit(1)

    times = int(n)
    contents = read_file(inputpath)
    duplicated = contents * times
    write_file(inputpath, duplicated)


def replace_string(inputpath, needle, newstring):
    validate_input_file(inputpath)

    if needle == "":
        print("エラー: needle には空文字列を指定できません。")
        sys.exit(1)

    contents = read_file(inputpath)
    replaced = contents.replace(needle, newstring)
    write_file(inputpath, replaced)


def main():
    # コマンドが指定されていない場合は、使い方を表示してユーザー入力を促す。
    if len(sys.argv) < 2:
        print_usage()
        user_input = input("コマンドを入力してください（例: reverse inputpath outputpath）: ").strip()
        if not user_input:
            print("エラー: コマンドが指定されていません。")
            sys.exit(1)

        parts = user_input.split()
        # 「python3 file_manipulator.py reverse ...」のようにコピペされた場合にも動くように調整
        if len(parts) >= 2 and parts[0] in ("python", "python3") and parts[1].endswith("file_manipulator.py"):
            parts = parts[2:]

        command = parts[0]
        args = parts[1:]
    else:
        command = sys.argv[1]
        args = sys.argv[2:]

    if command == "reverse":
        if len(args) != 2:
            print("エラー: reverse には inputpath と outputpath が必要です。")
            print_usage()
            sys.exit(1)

        inputpath, outputpath = args
        reverse_file(inputpath, outputpath)

    elif command == "copy":
        if len(args) != 2:
            print("エラー: copy には inputpath と outputpath が必要です。")
            print_usage()
            sys.exit(1)

        inputpath, outputpath = args
        copy_file(inputpath, outputpath)

    elif command == "duplicate-contents":
        if len(args) != 2:
            print("エラー: duplicate-contents には inputpath と n が必要です。")
            print_usage()
            sys.exit(1)

        inputpath, n = args
        duplicate_contents(inputpath, n)

    elif command == "replace-string":
        if len(args) != 3:
            print("エラー: replace-string には inputpath, needle, newstring が必要です。")
            print_usage()
            sys.exit(1)

        inputpath, needle, newstring = args
        replace_string(inputpath, needle, newstring)

    else:
        print(f"エラー: 不明なコマンド '{command}' です。")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()