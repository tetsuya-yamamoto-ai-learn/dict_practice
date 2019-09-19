def main():
    """
    `address_books` を使って、次のような出力をするコードを実装してください。
    `address_books` は面倒なのでコピペしてください。

    東京タワー 〒1050011 東京都港区芝公園４丁目２−８
    スカイツリー 〒1310045 東京都墨田区押上１丁目１−２
    通天閣タワー 〒5560002 大阪府大阪市浪速区恵美須東１丁目１８−６
    """

    address_books = [
        {'name': '東京タワー',
         'location': '東京都港区芝公園４丁目２−８',
         'zipcode': '1050011'},

        {'name': 'スカイツリー',
         'location': '東京都墨田区押上１丁目１−２',
         'zipcode': '1310045'},

        {'name': '通天閣タワー',
         'location': '大阪府大阪市浪速区恵美須東１丁目１８−６',
         'zipcode': '5560002'},
    ]

    # 東京タワー
    print(f'{address_books[0]["name"]} 〒{address_books[0]["zipcode"]} {address_books[0]["location"]}')

    # スカイツリー
    print(f'{address_books[1]["name"]} 〒{address_books[1]["zipcode"]} {address_books[1]["location"]}')

    # 通天閣タワー
    print(f'{address_books[2]["name"]} 〒{address_books[2]["zipcode"]} {address_books[2]["location"]}')

    #for book in address_books

if __name__ == '__main__':
    main()
