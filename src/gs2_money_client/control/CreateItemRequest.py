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


class CreateItemRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "CreateItem"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateItemRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__count = None
        else:
            self.set_count(params['count'] if 'count' in params.keys() else None)

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
        if money_name is not None and not (isinstance(money_name, str) or isinstance(money_name, unicode)):
            raise TypeError(type(money_name))
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        課金通貨の名前を設定
        :param money_name: 課金通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: CreateItemRequest
        """
        self.set_money_name(money_name)
        return self

    def get_name(self):
        """
        商品名を取得
        :return: 商品名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        商品名を設定
        :param name: 商品名
        :type name: unicode
        """
        if name is not None and not (isinstance(name, str) or isinstance(name, unicode)):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        商品名を設定
        :param name: 商品名
        :type name: unicode
        :return: this
        :rtype: CreateItemRequest
        """
        self.set_name(name)
        return self

    def get_count(self):
        """
        付与する課金通貨の数を取得
        :return: 付与する課金通貨の数
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        付与する課金通貨の数を設定
        :param count: 付与する課金通貨の数
        :type count: int
        """
        if count is not None and not isinstance(count, int):
            raise TypeError(type(count))
        self.__count = count

    def with_count(self, count):
        """
        付与する課金通貨の数を設定
        :param count: 付与する課金通貨の数
        :type count: int
        :return: this
        :rtype: CreateItemRequest
        """
        self.set_count(count)
        return self
