# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestValidPasswordReturnUserIdAndRoleDto.test_invalid_password_raises_exception dto'] = GenericRepr("UserIdentityDto(user_id=1, is_admin=False)")

snapshots['TestValidPasswordReturnUserIdAndRoleDto.test_valid_password_return_user_id_and_role_dto dto'] = GenericRepr("UserIdentityDto(user_id=1, is_admin=False)")
