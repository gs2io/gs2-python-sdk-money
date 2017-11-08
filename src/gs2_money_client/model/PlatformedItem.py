# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

class PlatformedItem(object):

    def __init__(self, params=None):
        if params is None:
            self.__item_id = None
            self.__money_id = None
            self.__name = None
            self.__platformed_item_id = None
            self.__price = None
            self.__platform = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_item_id(params['itemId'] if 'itemId' in params.keys() else None)
            self.set_money_id(params['moneyId'] if 'moneyId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_platformed_item_id(params['platformedItemId'] if 'platformedItemId' in params.keys() else None)
            self.set_price(params['price'] if 'price' in params.keys() else None)
            self.set_platform(params['platform'] if 'platform' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)


    def get_item_id(self):
        """
        商品IDを取得
        :return: 商品ID
        :rtype: unicode
        """
        return self.__item_id

    def set_item_id(self, item_id):
        """
        商品IDを設定
        :param item_id: 商品ID
        :type item_id: unicode
        """
        self.__item_id = item_id

    def get_money_id(self):
        """
        仮想通貨IDを取得
        :return: 仮想通貨ID
        :rtype: unicode
        """
        return self.__money_id

    def set_money_id(self, money_id):
        """
        仮想通貨IDを設定
        :param money_id: 仮想通貨ID
        :type money_id: unicode
        """
        self.__money_id = money_id

    def get_name(self):
        """
        アプリ内課金IDを取得
        :return: アプリ内課金ID
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        アプリ内課金IDを設定
        :param name: アプリ内課金ID
        :type name: unicode
        """
        self.__name = name

    def get_platformed_item_id(self):
        """
        プラットフォーム個別商品IDを取得
        :return: プラットフォーム個別商品ID
        :rtype: unicode
        """
        return self.__platformed_item_id

    def set_platformed_item_id(self, platformed_item_id):
        """
        プラットフォーム個別商品IDを設定
        :param platformed_item_id: プラットフォーム個別商品ID
        :type platformed_item_id: unicode
        """
        self.__platformed_item_id = platformed_item_id

    def get_price(self):
        """
        販売価格を取得
        :return: 販売価格
        :rtype: float
        """
        return self.__price

    def set_price(self, price):
        """
        販売価格を設定
        :param price: 販売価格
        :type price: float
        """
        self.__price = price

    def get_platform(self):
        """
        販売プラットフォームを取得
        :return: 販売プラットフォーム
        :rtype: unicode
        """
        return self.__platform

    def set_platform(self, platform):
        """
        販売プラットフォームを設定
        :param platform: 販売プラットフォーム
        :type platform: unicode
        """
        self.__platform = platform

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def to_dict(self):
        return { 
            "itemId": self.__item_id,
            "moneyId": self.__money_id,
            "name": self.__name,
            "platformedItemId": self.__platformed_item_id,
            "price": self.__price,
            "platform": self.__platform,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }