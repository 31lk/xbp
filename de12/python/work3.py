name=input("名前を教えて下さい")
waist=float(input("腹囲は？"))
age=int(input("年齢は？"))

print(name, "さんは腹囲", waist, "cmで年齢は" ,age, "歳ですね")

if waist>=85:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、内部脂肪蓄積注意です")