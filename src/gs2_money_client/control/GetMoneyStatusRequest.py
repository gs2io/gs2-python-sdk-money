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


class GetMoneyStatusRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "GetMoneyStatus"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetMoneyStatusRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)

    def get_money_name(self):
        """
        取得する課金通貨の名前を取得
        :return: 取得する課金通貨の名前
        :rtype: unicode
        """
        return self.__money_name

    def set_money_name(self, money_name):
        """
        取得する課金通貨の名前を設定
        :param money_name: 取得する課金通貨の名前
        :type money_name: unicode
        """
        if money_name is not None and not (isinstance(money_name, str) or isinstance(money_name, unicode)):
            raise TypeError(type(money_name))
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        取得する課金通貨の名前を設定
        :param money_name: 取得する課金通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: GetMoneyStatusRequest
        """
        self.set_money_name(money_name)
        return self
