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


class Summary(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__slot = None
            self.__paid = None
            self.__free = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_slot(params['slot'] if 'slot' in params.keys() else None)
            self.set_paid(params['paid'] if 'paid' in params.keys() else None)
            self.set_free(params['free'] if 'free' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

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
        self.__slot = slot

    def get_paid(self):
        """
        有償仮想通貨所持量を取得
        :return: 有償仮想通貨所持量
        :rtype: int
        """
        return self.__paid

    def set_paid(self, paid):
        """
        有償仮想通貨所持量を設定
        :param paid: 有償仮想通貨所持量
        :type paid: int
        """
        self.__paid = paid

    def get_free(self):
        """
        無償仮想通貨所持量を取得
        :return: 無償仮想通貨所持量
        :rtype: int
        """
        return self.__free

    def set_free(self, free):
        """
        無償仮想通貨所持量を設定
        :param free: 無償仮想通貨所持量
        :type free: int
        """
        self.__free = free

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
            "userId": self.__user_id,
            "slot": self.__slot,
            "paid": self.__paid,
            "free": self.__free,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
