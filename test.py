import cronpi

# 毎日午後5時半に実行する処理を登録
cronpi.run_every_day(r'python .\app\main.py').on("5:30pm")
print("ddddddddddddddddddd")