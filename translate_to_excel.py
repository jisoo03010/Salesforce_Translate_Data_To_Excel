import pandas as pd
import re

file_path = '' # 추출한 stf 파일 경로 입력

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.readlines()

data_start = 0
for idx, line in enumerate(file_content):
    if not line.startswith('#') and line.strip():
        data_start = idx
        break

data_lines = file_content[data_start:]
header_found = False
data_rows = []

for line in data_lines:
    # 헤더 행을 발견하면 이후 데이터 추출
    if line.startswith("# 키"):
        header_found = True
        continue
    if header_found and line.strip(): 
        if not line.startswith('#') and re.search(r'\t', line): 
            data_rows.append(line.strip())

# 데이터를 DataFrame으로 변환
columns = ["키", "레이블", "번역", "만료"]
data = [row.split("\t") for row in data_rows]
df = pd.DataFrame(data, columns=columns)

# 엑셀 파일로 저장
output_file = "./translated_data_ko.xlsx"
df.to_excel(output_file, index=False)

print(f"엑셀 파일로 저장 완료: {output_file}")
