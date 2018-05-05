#!/usr/bin/env python
#-*-coding:utf-8-*-
product_list=[
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),
]

saving=input('please input your money:')
shopping_cart=[]
if saving.isdigit():
    saving=int(saving)
    while True:
    
        for i,v in enumerate(product_list,1):
            #print(product_list.index(i),i)
            print(i,'>>>>',v)
        choice=input('选择购买商品编号[退出:q]:')
        if choice.isdigit():
            choice=int(choice)
            if choice>0 and choice<=len(product_list):
                p_item=product_list[choice-1]
                if p_item[1] < saving:
                    saving-=p_item[1]
                    shopping_cart.append(p_item)
                else:
                    print("余额不足，还剩%s" %saving)
                print(p_item)
            else:
                print('编码不存在')
        elif choice == 'q':
            print('-------您已购买商品--------')
            for i in shopping_cart:
                print(i)
            print('您还剩钱%s元'%saving)
            break
        else:
            print("invalid input")
