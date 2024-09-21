from numeron import Numeron

# python3 -m unittest 

def main():
    print("main")
    # 
    
    numeron = Numeron()
    now_ans = numeron.initial_ans
    cnt = 0

    while(len(now_ans) > 1):
        number = str(input("あなたの予想は？"))
        

        # 数字かどうかを判別
        if not numeron.is_number(number):
            print("数字を入力してください")
            continue
            
        # 3桁かどうかを判別
        if not numeron.is_xxx(number):
            print("3桁で入力してください")

        kouho = [int(d) for d in str(number)]
        print("候補")
        print(kouho)
        E = input("何イートですか")

        if not numeron.is_number(E):
            print("数字を入力してください")
            continue


        B = input("何バイトですか")
        if not numeron.is_number(B):
            print("数字を入力してください")
            continue

        E,B = int(E),int(B)

        if E == 0 and B == 0:
            print("0E0B")
            now_ans = numeron.result_0E0B(kouho,now_ans)
        if E == 0 and B == 1:
            print("0E1B")
            now_ans = numeron.result_0E1B(kouho,now_ans)
        if E == 0 and B == 2:
            print("0E2B")
            now_ans = numeron.result_0E2B(kouho,now_ans)
        if E == 0 and B == 3:
            print("0E3B")
            now_ans = numeron.result_0E3B(kouho,now_ans)

        if E == 1 and B == 0:
            print("1E0B")
            now_ans = numeron.result_1E0B(kouho,now_ans)

        if E == 2 and B == 0:
            print("2E0B")
            now_ans = numeron.result_2E0B(kouho,now_ans)

        if E == 1 and B == 1:
            print("1E1B")
            now_ans = numeron.result_1E1B(kouho,now_ans)
        if E == 1 and B == 2:
            print("1E2B")
            now_ans = numeron.result_1E2B(kouho,now_ans)
        if E == 3 and B == 0:
            now_ans = [kouho] 

        cnt +=1 
        print(now_ans)
        for i in range(len(now_ans)):
            print(now_ans[i])

        print(len(now_ans),"パターンです")

    print("----------現在の候補数",len(now_ans),  "[",cnt,"]回目","----------")
    print()
    print("相手の手は",now_ans[0],"で確定です")

    # 何も考えずに適当に候補から選ぶと勝率4割ほど
    # 最適なやつを選ぶと、7~8ぐらい？

    # 　
    # 012からスタートして候補の一番下のやつのみを選び続けた場合
    # 5手勝、4手勝,5手勝(0) 勝

    # 4手負け(1)4手負け(4)



if __name__ == "__main__":
    main()