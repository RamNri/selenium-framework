from framework_logging.log_utils import LogUtils


class TestLogUtils:

    def test_mask_sensitive_top_level_field(self):
        data = {
            "username": "admin",
            "password": "secret123",
        }

        result = LogUtils.mask_sensitive_data(data)

        assert result["username"] == "admin"
        assert result["password"] == "********"

    def test_mask_sensitive_nested_field(self):
        data = {
            "user": {
                "credentials": {
                    "password": "secret123",
                }
            }
        }

        result = LogUtils.mask_sensitive_data(data)

        assert result["user"]["credentials"]["password"] == "********"

    def test_mask_sensitive_fields_inside_list(self):
        data = [
            {
                "username": "user1",
                "token": "abc123",
            },
            {
                "username": "user2",
                "token": "xyz456",
            },
        ]

        result = LogUtils.mask_sensitive_data(data)

        assert result[0]["username"] == "user1"
        assert result[0]["token"] == "********"

        assert result[1]["username"] == "user2"
        assert result[1]["token"] == "********"

    def test_masking_does_not_modify_original_data(self):
        data = {
            "username": "admin",
            "password": "secret123",
        }

        LogUtils.mask_sensitive_data(data)

        assert data["password"] == "secret123"

    def test_non_sensitive_data_remains_unchanged(self):
        data = {
            "username": "admin",
            "booking_id": 1234,
            "active": True,
        }

        result = LogUtils.mask_sensitive_data(data)

        assert result == data