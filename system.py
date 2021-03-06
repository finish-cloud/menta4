import pandas as pd
import sys
import datetime

# 商品クラス
now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
receipt_path = './receipt/receipt_' + now + '.txt'
ITEM_MASTER_CSV_PATH = "./item_master.csv"


class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price

    def get_price(self):
        return self.price


# オーダークラス


class Order:
    def __init__(self, item_master):
        self.item_order_list = []
        self.item_master = item_master

    def add_item_order(self, item_code):
        self.item_order_list.append(item_code)

    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    # オーダー番号から商品情報を取得する（課題１）
    def view_items(self):
        print("商品一覧")
        print('--------------------')
        for item in self.item_master:
            print(str(item.item_code) + ',' +
                  str(item.item_name) + ',' + str(item.price))
        print('--------------------')

    def input_order(self):
        check = 'n'
        self.all_order_price = 0
        while check == 'n':
            order_code = int(input('オーダーする商品コードを入力してください：'))
            selected_menu = self.item_master[order_code-1]
            your_order = str(selected_menu.item_code) + \
                ',' + str(selected_menu.item_name)
            print('選択されたメニュー:')
            print(your_order)
            while check == 'y' or 'n':
                check = input('オーダーを終了しますかy/n：')
                if check == 'y':
                    break
                elif check == 'n':
                    break
                else:
                    print('無効な入力です。再度入力してください')

# マスタ登録(課題３)


def add_item_master_by_csv(csv_path):
    print("------- マスタ登録開始 ---------")
    item_master = []
    count = 0
    try:
        # CSVでは先頭の0が削除されるためこれを保持するための設定
        item_master_df = pd.read_csv(csv_path, dtype={"item_code": object})
        for item_code, item_name, price in zip(list(item_master_df["item_code"]), list(item_master_df["item_name"]), list(item_master_df["price"])):
            item_master.append(Item(item_code, item_name, price))
            print("{}({})".format(item_name, item_code))
            count += 1
        print("{}品の登録を完了しました。".format(count))
        print("------- マスタ登録完了 ---------")
        return item_master
    except:
        print("マスタ登録が失敗しました")
        print("------- マスタ登録完了 ---------")
        sys.exit()


def main():
    # マスタ登録(課題３)
    item_master = add_item_master_by_csv(ITEM_MASTER_CSV_PATH)  # CSVからマスタへ登録
    order = Order(item_master)  # マスタをオーダーに登録

    # マスタ登録
    # item_master = []
    # item_master.append(Item("001", "りんご", 100))
    # item_master.append(Item("002", "なし", 120))
    # item_master.append(Item("003", "みかん", 150))

    # # オーダー登録
    # order = Order(item_master)
    # order.add_item_order("001")
    # order.add_item_order("002")
    # order.add_item_order("003")

    # 課題2
    # order.view_items()
    order.input_order()


if __name__ == "__main__":
    main()
