from mocherry.library.commands import BaseCommand
from mocherry.library.databases import DatabaseConnection
from mocherry.settings import CONFIG
from faker import Faker

from app.models import SampleData

class Command(BaseCommand):
    def handle(self, *args):
        self.__create_sample_dataset(sample_data_length=15)

    def __create_sample_dataset(self, sample_data_length):
        alias = 'default'
        database_conn_uri = CONFIG.get('database').get(alias).get('uri')
        with DatabaseConnection(uri=database_conn_uri, alias=alias):
            print('Database: {}\n'.format(database_conn_uri))
            faker = Faker()
            for i in range(0, sample_data_length):
                data_info = SampleData()
                data_info.first_name = faker.first_name()
                data_info.last_name = faker.last_name()
                data_info.email = faker.email()
                data_info.phone_numbers = [faker.phone_number(), faker.phone_number()]
                data_info.enabled = True
                data_info.save()
                print('New Sample Data: {}'.format(data_info.pk))


        