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

class Item(object):

    def __init__(self, params=None):
        if params is None:
            self.__item_id = None
            self.__money_id = None
            self.__name = None
            self.__count = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_item_id(params['itemId'] if 'itemId' in params.keys() else None)
            self.set_money_id(params['moneyId'] if 'moneyId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_count(params['count'] if 'count' in params.keys() else None)
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
        self.__name = name

    def get_count(self):
        """
        付与する仮想通貨の数を取得
        :return: 付与する仮想通貨の数
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        付与する仮想通貨の数を設定
        :param count: 付与する仮想通貨の数
        :type count: int
        """
        self.__count = count

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
            "count": self.__count,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }