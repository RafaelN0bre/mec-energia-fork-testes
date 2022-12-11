import pytest
from rest_framework.test import APIClient

from tests.test_utils.create_objects_util import CreateObjectsUtil

@pytest.mark.django_db
class TestContractEndpoint:
    def setup_method(self):
        self.university, self.user = CreateObjectsUtil.create_university_and_user()
        
        self.client = APIClient()
        self.client.login(
            email = CreateObjectsUtil.login_university_user['email'], 
            password = CreateObjectsUtil.login_university_user['password'])

        self.university_to_be_created = {
            'name': 'Universidade de Brasília',
            'cnpj': '00038174000143'
        }

        _, self.distributor = CreateObjectsUtil.create_distributor_object(self.university, 0)

        (self.consumer_unit_test_dict,
        self.consumer_unit_test) = CreateObjectsUtil.create_consumer_unit_object(
                                        consumer_unit_dict_index = 0,
                                        university = self.university)

        self.contract_test_1 = CreateObjectsUtil.create_contract_object(
                                contract_dict_index = 0, distributor=self.distributor,
                                consumer_unit = self.consumer_unit_test)

        self.contract_test_2 = CreateObjectsUtil.create_contract_object(
                                contract_dict_index = 1, distributor=self.distributor,
                                consumer_unit = self.consumer_unit_test)

    # TODO:
    # Fazer testes de endpoint de contratos