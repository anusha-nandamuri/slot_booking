from datetime import datetime


def test_get_available_slot_details_return_available_slot_dtos(
        snapshot, create_slots, create_washing_machine, create_slots_for_user
):
    # Arrange
    user_id = 1
    bookable_days = ["Monday", "Tuesday"]
    storage = StorageImplementation()

    # Act
    available_slots_dtos = storage.get_available_slot_details(user_id=user_id, bookable_days=bookable_days)

    # Assert
    snapshot.assert_match(available_slots_dtos, 'list_of_dtos')
