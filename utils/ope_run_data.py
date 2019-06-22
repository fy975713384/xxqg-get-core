# -*- coding: utf-8 -*-
from pathlib import Path
import yaml


class OpeRunData:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OpeRunData, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.file = Path(__file__).parent.parent.joinpath('data').joinpath('run_data.yml')
        if not self.file.is_file():
            raise ValueError('run_data.yml 文件路径错误！')

    def _read_data(self):
        with self.file.open() as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_value(self, k1, k2):
        data = self._read_data()
        return data[k1][k2]

    @classmethod
    def _data_template(cls, index, port, bp, device):
        data = {
            f'device_{str(index)}': {
                'port': port,
                'bp': bp,
                'udid': device
            }
        }
        return data

    def write_data(self, index, port, bo, device):
        data = self._data_template(index, port, bo, device)
        with self.file.open('a') as f:
            yaml.dump(data, f)

    def clear_yaml(self):
        with self.file.open('w') as f:
            f.truncate()
