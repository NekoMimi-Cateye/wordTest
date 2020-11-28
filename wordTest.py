import time
import numpy as np

if __name__ == "__main__":
    ##問題・解答データ
    q = np.array([])
    a = np.array([])
    ##正解した問題・解答データ
    cQ = np.array([])
    icQ = np.array([])
    ##不正解した問題・解答データ
    cA = np.array([])
    icA = np.array([])
    ##ファイル(5セッション分)
    files = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']
    ##正解数・不正解数・問題数
    yes = 0
    no = 0
    qu = 0

    ##セッション番号を入力する
    print("セッション番号 (1-5) >>> ", end='')
    session = int(input())

    ##条件分岐
    if session in [1, 2, 3, 4, 5]:
        ##ファイル内のデータを読み込む
        f1 = open(files[session-1], 'r', encoding = 'utf-8')
        lines = f1.readlines()
        f1.close()
        ##問題データと解答データに分ける
        for i in range(len(lines) // 2):
            q = np.append(q, lines[i * 2].replace('\n', '').replace('\ufeff', ''))
            a = np.append(a, lines[i * 2 + 1].replace('\n', '').replace('\ufeff', ''))
        
        ##出題部
        while len(q) > 0:
            n = np.random.randint(0, len(q))
            print(q[n])
            x = input()
            if x == a[n]:
                print("正解")
                yes += 1
                cQ = np.append(cQ, q[n])
                cA = np.append(cA, a[n])
            else:
                print("不正解")
                no += 1
                icQ = np.append(icQ, q[n])
                icA = np.append(icA, a[n])
            print("解答:" + str(a[n]))
            qu += 1
            q = np.delete(q, n, axis = 0)
            a = np.delete(a, n, axis = 0)
        
        ##正答率表示
        print("正答率:" + str(100 * yes / qu) + "%")

        ##正解した問題・不正解した問題を分けて表示
        print("----------正解した問題----------")
        for i in range(len(cQ)):
            print("問題: {}\n正答: {}\n\n".format(cQ[i], cA[i]))
        print("----------不正解の問題----------")
        for i in range(len(icQ)):
            print("問題: {}\n正答: {}\n\n".format(icQ[i], icA[i]))

        #ライトナーシステム
        ##不正解データをsession1に収納
        ###session番号: 1...上書き/other...追加
        if (session != 1):
            f1 = open(files[0], 'r', encoding = 'utf-8')
            lines = f1.readlines()
            f1.close()
            ###問題データと解答データに分ける
            for i in range(len(lines) // 2):
                icQ = np.append(icQ, lines[i * 2].replace('\n', '').replace('\ufeff', ''))
                icA = np.append(icA, lines[i * 2 + 1].replace('\n', '').replace('\ufeff', ''))
        ###ファイル書き込み
        f1 = open(files[0], 'w', encoding = 'utf-8')
        for i in range(len(icQ)):
            f1.write(icQ[i])
            f1.write('\n')
            f1.write(icA[i])
            if (i != len(icQ) - 1):
                f1.write('\n')
        f1.close()
        ##正解データを次のsessionに収納
        ###session番号: 5...上書き/other...追加
        if (session == 5):
            f2 = open(files[4], 'r', encoding = 'utf-8')
        else:
            f2 = open(files[session], 'r', encoding = 'utf-8')
            lines = f2.readlines()
            f2.close()
            ###問題データと解答データに分ける
            for i in range(len(lines) // 2):
                cQ = np.append(cQ, lines[i * 2].replace('\n', '').replace('\ufeff', ''))
                cA = np.append(cA, lines[i * 2 + 1].replace('\n', '').replace('\ufeff', ''))
        ###ファイル書き込み
        f2 = open(files[0], 'w', encoding = 'utf-8')
        for i in range(len(cQ)):
            f2.write(cQ[i])
            f2.write('\n')
            f2.write(cA[i])
            if (i != len(cQ) - 1):
                f2.write('\n')
        f2.close()
    else:
        print("[error] 正しい番号が入力されませんでした")