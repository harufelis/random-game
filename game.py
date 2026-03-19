import sys
import random

# 入力 stdin
sys.stdout.write("最小値を入力してください： ")
sys.stdout.flush()  # 出力をフラッシュしてから入力を待つ
n = int(sys.stdin.readline())

sys.stdout.write("最大値を入力してください： ")
sys.stdout.flush()  # 出力をフラッシュしてから入力を待つ
m = int(sys.stdin.readline())

# バリデーション
if n > m:
  sys.stdout.write("エラー：最小値は最大値以下でなければなりません。\n")
  sys.stdout.flush()  # 出力をフラッシュしてから終了
  sys.exit(1)

# 乱数生成
answer =random.randint(n, m)

# ループ
while True:
  sys.stdout.write("最小値から最大値の範囲で設定された乱数を当ててください： ")
  sys.stdout.flush()  # 出力をフラッシュしてから入力を待つ
  guess = int(sys.stdin.readline())
  if guess < answer:
    sys.stdout.write("もっと大きい数です。\n")
    sys.stdout.flush()  # 出力をフラッシュしてから次の入力を待つ
  elif guess > answer:
    sys.stdout.write("もっと小さい数です。\n")
    sys
  else:
    sys.stdout.write("正解です！\n")
    sys
    break

