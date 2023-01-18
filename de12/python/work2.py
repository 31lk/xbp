name="aaa"
waist=84
age=44

print(name, "さんは腹囲", waist, "cmで年齢は" ,age, "歳ですね")

if waist>=85:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")

if age >= 40 and waist >=85:
    print("True")
else:
    print("False")
