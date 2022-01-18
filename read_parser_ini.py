from collections import namedtuple
from configparser import ConfigParser

HData = namedtuple('HData', 'line_no slice')
PData = namedtuple('PData', 'name apo eos acc per xre pis fpa')
FPA = namedtuple('FPA', 'account exception omades negative_omades')


def split_header_data(text: str) -> tuple:
    line, apo, eos = text.split()
    apoeos = slice(int(apo) - 1, int(eos) - 1)
    return HData(int(line) - 1, apoeos)


def split_line_data(text: str) -> slice:
    apo, eos = text.split()
    return slice(int(apo) - 1, int(eos) - 1)


def read_ini(config_file: str = 'parser.ini') -> PData:
    config = ConfigParser()
    config.read(config_file, encoding='utf8')

    name = split_header_data(config['PARSE']['name'])
    apo = split_header_data(config['PARSE']['apo'])
    eos = split_header_data(config['PARSE']['eos'])

    acc = split_line_data(config['PARSE']['acc'])
    per = split_line_data(config['PARSE']['per'])
    xre = split_line_data(config['PARSE']['xre'])
    pis = split_line_data(config['PARSE']['pis'])

    fpa = FPA(
        config['FPA']['fpa_acc'],
        config['FPA']['fpa_acc_exception'],
        config['FPA']['omades'],
        config['FPA']['negative_omades'])
    return PData(name, apo, eos, acc, per, xre, pis, fpa)


if __name__ == '__main__':
    cfg = read_ini()
    print(cfg)
