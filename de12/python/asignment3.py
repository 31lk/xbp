q1=int(input("大型が好き=1 小型が好き=2 A/")) 

if q1 == 1:
    print("長毛=3 短毛=4") #大型好き>q2
if q1 == 2:
    print("長毛=5 短毛=6") #小型好き>q3



q2=int(input(" "))

if q2 == 3:
    print("可愛い=7 かっこいい=8") #大型の長毛>a1
if q2 == 4:
    print("可愛い=9 かっこいい=10") #大型の短毛>a2

for q2 in range(20):
    print( )
    if q2 <= 4:
        pass
        print("再度同じ数字を入力 A/")


q3=int(input(" "))

if q3 == 5:
    print("可愛い=11 かっこいい=12") #小型の長毛>q4
if q3 == 6:
    print("可愛い=13 かっこいい=14") #小型の短毛>q5


q4=int(input(" "))

if q4 == 11:
    print("A.トイプードル") #可愛い小型の長毛>a3
elif q4 == 12:
    print("A.オーストランテリア") #かっこいい小型の長毛>a4
elif q4 == 7:
    print("A.サモエド") #可愛い大型の長毛
elif q4 == 8:
    print("A.ボーダー・コリー") #かっこいい大型の長毛
elif q4 == 13:
    print("A.チワワ")
elif q4 == 14:
    print("A.パグ")
elif q4 == 9:
    print("A.ゴールデンレトリバー")
elif q4 == 10:
    print("A.シベリアンハスキー")



