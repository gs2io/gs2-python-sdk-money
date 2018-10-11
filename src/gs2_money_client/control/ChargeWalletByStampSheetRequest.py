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


class ChargeWalletByStampSheetRequest(Gs2UserRequest):

    class Constant(Gs2Money):
        FUNCTION = "ChargeWalletByStampSheet"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ChargeWalletByStampSheetRequest, self).__init__(params)
        if params is None:
            self.__slot = None
            self.__sheet = None
            self.__key_name = None
        else:
            self.set_slot(params['slot'] if 'slot' in params.keys() else None)
            self.set_sheet(params['sheet'] if 'sheet' in params.keys() else None)
            self.set_key_name(params['keyName'] if 'keyName' in params.keys() else None)

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
        if slot is not None and not isinstance(slot, int):
            raise TypeError(type(slot))
        self.__slot = slot

    def with_slot(self, slot):
        """
        取得するウォレットのスロット番号を設定
        :param slot: 取得するウォレットのスロット番号
        :type slot: int
        :return: this
        :rtype: ChargeWalletByStampSheetRequest
        """
        self.set_slot(slot)
        return self

    def get_sheet(self):
        """
        スタンプシートを取得
        :return: スタンプシート
        :rtype: unicode
        """
        return self.__sheet

    def set_sheet(self, sheet):
        """
        スタンプシートを設定
        :param sheet: スタンプシート
        :type sheet: unicode
        """
        if sheet is not None and not (isinstance(sheet, str) or isinstance(sheet, unicode)):
            raise TypeError(type(sheet))
        self.__sheet = sheet

    def with_sheet(self, sheet):
        """
        スタンプシートを設定
        :param sheet: スタンプシート
        :type sheet: unicode
        :return: this
        :rtype: ChargeWalletByStampSheetRequest
        """
        self.set_sheet(sheet)
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
        if key_name is not None and not (isinstance(key_name, str) or isinstance(key_name, unicode)):
            raise TypeError(type(key_name))
        self.__key_name = key_name

    def with_key_name(self, key_name):
        """
        スタンプの暗号鍵を設定
        :param key_name: スタンプの暗号鍵
        :type key_name: unicode
        :return: this
        :rtype: ChargeWalletByStampSheetRequest
        """
        self.set_key_name(key_name)
        return self
