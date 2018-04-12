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


class ConsumeWalletByUserIdRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "ConsumeWalletByUserId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ConsumeWalletByUserIdRequest, self).__init__(params)
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
            self.__count = None
        else:
            self.set_count(params['count'] if 'count' in params.keys() else None)
        if params is None:
            self.__use = None
        else:
            self.set_use(params['use'] if 'use' in params.keys() else None)
        if params is None:
            self.__paid_only = None
        else:
            self.set_paid_only(params['paidOnly'] if 'paidOnly' in params.keys() else None)

    def get_money_name(self):
        """
        取得する仮想通貨の名前を取得
        :return: 取得する仮想通貨の名前
        :rtype: unicode
        """
        return self.__money_name

    def set_money_name(self, money_name):
        """
        取得する仮想通貨の名前を設定
        :param money_name: 取得する仮想通貨の名前
        :type money_name: unicode
        """
        if not isinstance(money_name, unicode):
            raise TypeError(type(money_name))
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        取得する仮想通貨の名前を設定
        :param money_name: 取得する仮想通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: ConsumeWalletByUserIdRequest
        """
        self.set_money_name(money_name)
        return self

    def get_slot(self):
        """
        取得するウォレットのスロット番号を取得
        :return: 取得するウォレットのスロット番号
        :rtype: int
        """
        return self.__slot

    def set_slot(self, slot):
        """
        取得するウォレットのスロット番号を設定
        :param slot: 取得するウォレットのスロット番号
        :type slot: int
        """
        if not isinstance(slot, int):
            raise TypeError(type(slot))
        self.__slot = slot

    def with_slot(self, slot):
        """
        取得するウォレットのスロット番号を設定
        :param slot: 取得するウォレットのスロット番号
        :type slot: int
        :return: this
        :rtype: ConsumeWalletByUserIdRequest
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
        if not isinstance(user_id, unicode):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ウォレットのユーザIDを設定
        :param user_id: ウォレットのユーザID
        :type user_id: unicode
        :return: this
        :rtype: ConsumeWalletByUserIdRequest
        """
        self.set_user_id(user_id)
        return self

    def get_count(self):
        """
        仮想通貨消費量を取得
        :return: 仮想通貨消費量
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        仮想通貨消費量を設定
        :param count: 仮想通貨消費量
        :type count: int
        """
        if not isinstance(count, int):
            raise TypeError(type(count))
        self.__count = count

    def with_count(self, count):
        """
        仮想通貨消費量を設定
        :param count: 仮想通貨消費量
        :type count: int
        :return: this
        :rtype: ConsumeWalletByUserIdRequest
        """
        self.set_count(count)
        return self

    def get_use(self):
        """
        用途IDを取得
        :return: 用途ID
        :rtype: int
        """
        return self.__use

    def set_use(self, use):
        """
        用途IDを設定
        :param use: 用途ID
        :type use: int
        """
        if not isinstance(use, int):
            raise TypeError(type(use))
        self.__use = use

    def with_use(self, use):
        """
        用途IDを設定
        :param use: 用途ID
        :type use: int
        :return: this
        :rtype: ConsumeWalletByUserIdRequest
        """
        self.set_use(use)
        return self

    def get_paid_only(self):
        """
        有償仮想通貨のみ消費対象としたい場合に true を指定しますを取得
        :return: 有償仮想通貨のみ消費対象としたい場合に true を指定します
        :rtype: bool
        """
        return self.__paid_only

    def set_paid_only(self, paid_only):
        """
        有償仮想通貨のみ消費対象としたい場合に true を指定しますを設定
        :param paid_only: 有償仮想通貨のみ消費対象としたい場合に true を指定します
        :type paid_only: bool
        """
        if not isinstance(paid_only, bool):
            raise TypeError(type(paid_only))
        self.__paid_only = paid_only

    def with_paid_only(self, paid_only):
        """
        有償仮想通貨のみ消費対象としたい場合に true を指定しますを設定
        :param paid_only: 有償仮想通貨のみ消費対象としたい場合に true を指定します
        :type paid_only: bool
        :return: this
        :rtype: ConsumeWalletByUserIdRequest
        """
        self.set_paid_only(paid_only)
        return self
