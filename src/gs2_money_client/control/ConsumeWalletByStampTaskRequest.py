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


class ConsumeWalletByStampTaskRequest(Gs2UserRequest):

    class Constant(Gs2Money):
        FUNCTION = "ConsumeWalletByStampTask"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ConsumeWalletByStampTaskRequest, self).__init__(params)
        if params is None:
            self.__slot = None
            self.__task = None
            self.__key_name = None
            self.__transaction_id = None
        else:
            self.set_slot(params['slot'] if 'slot' in params.keys() else None)
            self.set_task(params['task'] if 'task' in params.keys() else None)
            self.set_key_name(params['keyName'] if 'keyName' in params.keys() else None)
            self.set_transaction_id(params['transactionId'] if 'transactionId' in params.keys() else None)

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
        if slot and not isinstance(slot, int):
            raise TypeError(type(slot))
        self.__slot = slot

    def with_slot(self, slot):
        """
        取得するウォレットのスロット番号を設定
        :param slot: 取得するウォレットのスロット番号
        :type slot: int
        :return: this
        :rtype: ConsumeWalletByStampTaskRequest
        """
        self.set_slot(slot)
        return self

    def get_task(self):
        """
        スタンプタスクを取得
        :return: スタンプタスク
        :rtype: unicode
        """
        return self.__task

    def set_task(self, task):
        """
        スタンプタスクを設定
        :param task: スタンプタスク
        :type task: unicode
        """
        if task and not (isinstance(task, str) or isinstance(task, unicode)):
            raise TypeError(type(task))
        self.__task = task

    def with_task(self, task):
        """
        スタンプタスクを設定
        :param task: スタンプタスク
        :type task: unicode
        :return: this
        :rtype: ConsumeWalletByStampTaskRequest
        """
        self.set_task(task)
        return self

    def get_key_name(self):
        """
        スタンプの暗号鍵を取得
        :return: スタンプの暗号鍵
        :rtype: unicode
        """
        return self.__key_name

    def set_key_name(self, key_name):
        """
        スタンプの暗号鍵を設定
        :param key_name: スタンプの暗号鍵
        :type key_name: unicode
        """
        if key_name and not (isinstance(key_name, str) or isinstance(key_name, unicode)):
            raise TypeError(type(key_name))
        self.__key_name = key_name

    def with_key_name(self, key_name):
        """
        スタンプの暗号鍵を設定
        :param key_name: スタンプの暗号鍵
        :type key_name: unicode
        :return: this
        :rtype: ConsumeWalletByStampTaskRequest
        """
        self.set_key_name(key_name)
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
        :rtype: ConsumeWalletByStampTaskRequest
        """
        self.set_transaction_id(transaction_id)
        return self
