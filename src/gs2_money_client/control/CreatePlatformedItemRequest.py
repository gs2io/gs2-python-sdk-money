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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_money_client.Gs2Money import Gs2Money


class CreatePlatformedItemRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "CreatePlatformedItem"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreatePlatformedItemRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
            self.__item_name = None
            self.__platform = None
            self.__price = None
            self.__name = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)
            self.set_platform(params['platform'] if 'platform' in params.keys() else None)
            self.set_price(params['price'] if 'price' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)

    def get_money_name(self):
        """
        仮想通貨の名前を取得
        :return: 仮想通貨の名前
        :rtype: unicode
        """
        return self.__money_name

    def set_money_name(self, money_name):
        """
        仮想通貨の名前を設定
        :param money_name: 仮想通貨の名前
        :type money_name: unicode
        """
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        仮想通貨の名前を設定
        :param money_name: 仮想通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: CreatePlatformedItemRequest
        """
        self.set_money_name(money_name)
        return self

    def get_item_name(self):
        """
        商品の名前を取得
        :return: 商品の名前
        :rtype: unicode
        """
        return self.__item_name

    def set_item_name(self, item_name):
        """
        商品の名前を設定
        :param item_name: 商品の名前
        :type item_name: unicode
        """
        self.__item_name = item_name

    def with_item_name(self, item_name):
        """
        商品の名前を設定
        :param item_name: 商品の名前
        :type item_name: unicode
        :return: this
        :rtype: CreatePlatformedItemRequest
        """
        self.set_item_name(item_name)
        return self

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

    def with_platform(self, platform):
        """
        販売プラットフォームを設定
        :param platform: 販売プラットフォーム
        :type platform: unicode
        :return: this
        :rtype: CreatePlatformedItemRequest
        """
        self.set_platform(platform)
        return self

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

    def with_price(self, price):
        """
        販売価格を設定
        :param price: 販売価格
        :type price: float
        :return: this
        :rtype: CreatePlatformedItemRequest
        """
        self.set_price(price)
        return self

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

    def with_name(self, name):
        """
        アプリ内課金IDを設定
        :param name: アプリ内課金ID
        :type name: unicode
        :return: this
        :rtype: CreatePlatformedItemRequest
        """
        self.set_name(name)
        return self
