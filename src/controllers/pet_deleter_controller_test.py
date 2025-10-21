from unittest.mock import Mock

from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

from .pet_deleter_controller import PetDeleterController


def test_delete_pet():
    mock_repository: PetsRepositoryInterface = Mock(spec=PetsRepositoryInterface)
    controller = PetDeleterController(mock_repository)
    controller.delete("amiguinho")
    mock_repository.delete_pet.assert_called_once_with("amiguinho")
