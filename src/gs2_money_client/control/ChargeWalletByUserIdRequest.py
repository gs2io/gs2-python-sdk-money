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


class ChargeWalletByUserIdRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "ChargeWalletByUserId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ChargeWalletByUserIdRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
        if params is None:
            self.__slot = None
        else:
            self.set_slot(params['slot'] if 'slot' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__price = None
        else:
            self.set_price(params['price'] if 'price' in params.keys() else None)
        if params is None:
            self.__count = None
        else:
            self.set_count(params['count'] if 'count' in params.keys() else None)
        if params is None:
            self.__transaction_id = None
        else:
            self.set_transaction_id(params['transactionId'] if 'transactionId' in params.keys() else None)

    def get_money_name(self):
        """
        課金通貨の名前を取得
        :return: 課金通貨の名前
        :rtype: unicode
        """
        return self.__money_name

    def set_money_name(self, money_name):
        """
        課金通貨の名前を設定
        :param money_name: 課金通貨の名前
        :type money_name: unicode
        """
        if money_name and not (isinstance(money_name, str) or isinstance(money_name, unicode)):
            raise TypeError(type(money_name))
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        課金通貨の名前を設定
        :param money_name: 課金通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: ChargeWalletByUserIdRequest
        """
        self.set_money_name(money_name)
        return self

    def get_slot(self):
        """
        ウォレットのスロット番号を取得
        :return: ウォレットのスロット番号
        :rtype: int
        """
        return self.__slot

    def set_slot(self, slot):
        """
        ウォレットのスロット番号を設定
        :param slot: ウォレットのスロット番号
        :type slot: int
        """
        if slot and not isinstance(slot, int):
            raise TypeError(type(slot))
        self.__slot = slot

    def with_slot(self, slot):
        """
        ウォレットのスロット番号を設定
        :param slot: ウォレットのスロット番号
        :type slot: int
        :return: this
        :rtype: ChargeWalletByUserIdRequest
        """
        self.set_slot(slot)
        return self

    def get_user_id(self):
        """
        ウォレットのユーザIDを取得
        :return: ウォレットのユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ウォレットのユーザIDを設定
        :param user_id: ウォレットのユーザID
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ウォレットのユーザIDを設定
        :param user_id: ウォレットのユーザID
        :type user_id: unicode
        :return: this
        :rtype: ChargeWalletByUserIdRequest
        """
        self.set_user_id(user_id)
        return self

    def get_price(self):
        """
        支払金額を取得
        :return: 支払金額
        :rtype: float
        """
        return self.__price

    def set_price(self, price):
        """
        支払金額を設定
        :param price: 支払金額
        :type price: float
        """
        if price and not isinstance(price, float):
            raise TypeError(type(price))
        self.__price = price

    def with_price(self, price):
        """
        支払金額を設定
        :param price: 支払金額
        :type price: float
        :return: this
        :rtype: ChargeWalletByUserIdRequest
        """
        self.set_price(price)
        return self

    def get_count(self):
        """
        課金通貨付与量を取得
        :return: 課金通貨付与量
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        課金通貨付与量を設定
        :param count: 課金通貨付与量
        :type count: int
        """
        if count and not isinstance(count, int):
            raise TypeError(type(count))
        self.__count = count

    def with_count(self, count):
        """
        課金通貨付与量を設定
        :param count: 課金通貨付与量
        :type count: int
        :return: this
        :rtype: ChargeWalletByUserIdRequest
        """
        self.set_count(count)
        return self

    def get_transaction_id(self):
        """
        トランザクションIDを取得
        :return: トランザクションID
        :rtype: unicode
        """
        return self.__transaction_id

    def set_transaction_id(self, transaction_id):
        """
        トランザクションIDを設定
        :param transaction_id: トランザクションID
        :type transaction_id: unicode
        """
        if transaction_id and not (isinstance(transaction_id, str) or isinstance(transaction_id, unicode)):
            raise TypeError(type(transaction_id))
        self.__transaction_id = transaction_id

    def with_transaction_id(self, transaction_id):
        """
        トランザクションIDを設定
        :param transaction_id: トランザクションID
        :type transaction_id: unicode
        :return: this
        :rtype: ChargeWalletByUserIdRequest
        """
        self.set_transaction_id(transaction_id)
        return self
