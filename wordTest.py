import time
import numpy as np

if __name__ == "__main__":
    q = np.array([])
    a = np.array([])

    cQ = np.array([])
    icQ = np.array([])

    cA = np.array([])
    icA = np.array([])

    files = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']

    yes = 0
    no = 0
    qu = 0

    print("セッション番号 (1-5) >>> ", end='')
    session = int(input())

    if session in [1, 2, 3, 4, 5]:
        f1 = open(files[session-1], 'r', encoding = 'utf-8')
        lines = f1.readlines()
        f1.close()

        for i in range(len(lines) // 2):
            q = np.append(q, lines[i * 2].replace('\n', '').replace('\ufeff', ''))
            a = np.append(a, lines[i * 2 + 1].replace('\n', '').replace('\ufeff', ''))
        
        print("問題数:{}問\n".format(len(q)))
        while len(q) > 0:
            print("------第{}問------".format(qu+1))
            n = np.random.randint(0, len(q))
            print(q[n])
            x = input()
            if x == a[n]:
                print("正解 　", end='')
                yes += 1
                cQ = np.append(cQ, q[n])
                cA = np.append(cA, a[n])
            else:
                print("不正解 ", end='')
                no += 1
                icQ = np.append(icQ, q[n])
                icA = np.append(icA, a[n])
            print("解答:" + str(a[n]))
            qu += 1
            q = np.delete(q, n, axis = 0)
            a = np.delete(a, n, axis = 0)
            print()
        print("正答率:" + str(100 * yes / qu) + "%")

        print("----------正解した問題----------")
        if (len(cQ) == 0):
            print("なし\n")
        for i in range(len(cQ)):
            print("問題: {}\n正答: {}\n\n".format(cQ[i], cA[i]))
        print("----------不正解の問題----------")
        if (len(icQ) == 0):
            print("なし\n")
        for i in range(len(icQ)):
            print("問題: {}\n正答: {}\n\n".format(icQ[i], icA[i]))

        f1 = open(files[session-1], 'w', encoding = 'utf-8')
        f1.write('')
        f1.close()

        f1 = open(files[0], 'r', encoding = 'utf-8')
        lines = f1.readlines()
        f1.close()

        for i in range(len(lines) // 2):
            icQ = np.append(icQ, lines[i * 2].replace('\n', '').replace('\ufeff', ''))
            icA = np.append(icA, lines[i * 2 + 1].replace('\n', '').replace('\ufeff', ''))

        f1 = open(files[0], 'w', encoding = 'utf-8')
        for i in range(len(icQ)):
            f1.write(icQ[i])
            f1.write('\n')
            f1.write(icA[i])
            if (i != len(icQ) - 1):
                f1.write('\n')
        f1.close()

        if (session == 5):
            session = 4

        f2 = open(files[session], 'r', encoding = 'utf-8')
        lines = f2.readlines()
        f2.close()

        for i in range(len(lines) // 2):
            cQ = np.append(cQ, lines[i * 2].replace('\n', '').replace('\ufeff', ''))
            cA = np.append(cA, lines[i * 2 + 1].replace('\n', '').replace('\ufeff', ''))

        f2 = open(files[session], 'w', encoding = 'utf-8')
        for i in range(len(cQ)):
            f2.write(cQ[i])
            f2.write('\n')
            f2.write(cA[i])
            if (i != len(cQ) - 1):
                f2.write('\n')
        f2.close()
    else:
        print("[error] 正しい番号が入力されませんでした")