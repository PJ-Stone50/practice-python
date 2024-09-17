# 2.ให้เขียนโปรแกรมรับจำนวนเต็ม N และ K จากนั้นพิมพ์เลขตั้งแต่ 1 ถึง N ที่ K หารลงตัว

# Sample output

# Enter N: 10
# Enter K: 3
# 3
# 6
# 9
# **********************************************************

for i in range(5):
    N = int(input("Enter N: "))
    K = int(input("Enter K: "))

    # print(N//K)
    round = N//K

    for i in range(1,round+1):
        print(K * i)