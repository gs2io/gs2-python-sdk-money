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

class Wallet(object):

    def __init__(self, params=None):
        if params is None:
            self.__price = None
            self.__count = None
        else:
            self.set_price(params['price'] if 'price' in params.keys() else None)
            self.set_count(params['count'] if 'count' in params.keys() else None)


    def get_price(self):
        """
        単価を取得
        :return: 単価
        :rtype: float
        """
        return self.__price

    def set_price(self, price):
        """
        単価を設定
        :param price: 単価
        :type price: float
        """
        self.__price = price

    def get_count(self):
        """
        所持数を取得
        :return: 所持数
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        所持数を設定
        :param count: 所持数
        :type count: int
        """
        self.__count = count

    def to_dict(self):
        return { 
            "price": self.__price,
            "count": self.__count,
        }