list = ["cat", "blue", "skt", "umbrells", "paddy"]
list2 = ["cat", "blue", "sky", "umbrella", "paddy"]



def clone(msv, msv2):
    for num in msv:
        for num2 in msv2:
            if num == num2:
                print("1")
                break
        else:
            print("-1")


clone(list,list2)

