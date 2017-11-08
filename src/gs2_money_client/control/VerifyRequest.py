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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_money_client.Gs2Money import Gs2Money


class VerifyRequest(Gs2UserRequest):

    class Constant(Gs2Money):
        FUNCTION = "Verify"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(VerifyRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
            self.__slot = None
            self.__receipt = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
            self.set_slot(params['slot'] if 'slot' in params.keys() else None)
            self.set_receipt(params['receipt'] if 'receipt' in params.keys() else None)

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
        if not isinstance(money_name, unicode):
            raise TypeError(type(money_name))
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        仮想通貨の名前を設定
        :param money_name: 仮想通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: VerifyRequest
        """
        self.set_money_name(money_name)
        return self

    def get_slot(self):
        """
        スロット番号を取得
        :return: スロット番号
        :rtype: int
        """
        return self.__slot

    def set_slot(self, slot):
        """
        スロット番号を設定
        :param slot: スロット番号
        :type slot: int
        """
        if not isinstance(slot, int):
            raise TypeError(type(slot))
        self.__slot = slot

    def with_slot(self, slot):
        """
        スロット番号を設定
        :param slot: スロット番号
        :type slot: int
        :return: this
        :rtype: VerifyRequest
        """
        self.set_slot(slot)
        return self

    def get_receipt(self):
        """
        レシートデータを取得
        :return: レシートデータ
        :rtype: unicode
        """
        return self.__receipt

    def set_receipt(self, receipt):
        """
        レシートデータを設定
        :param receipt: レシートデータ
        :type receipt: unicode
        """
        if not isinstance(receipt, unicode):
            raise TypeError(type(receipt))
        self.__receipt = receipt

    def with_receipt(self, receipt):
        """
        レシートデータを設定
        :param receipt: レシートデータ
        :type receipt: unicode
        :return: this
        :rtype: VerifyRequest
        """
        self.set_receipt(receipt)
        return self
