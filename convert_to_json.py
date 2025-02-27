
import pandas as pd

excel_file = r"C:\Users\admin\Desktop\大宰府プロジェクト\dazaihupuroject\data\AIタグ付け短歌・俳句.xlsx"


df = pd.read_excel(excel_file)


df = df[["句", "データ元", "年齢", "在住地","AIタグ","場所"]]


json_file = "poems.json"
df.to_json(json_file, orient="records", force_ascii=False, indent=4)

print(f"データが {json_file} に変換されました！")