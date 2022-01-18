import re
from collections import namedtuple

import accounts_file as acf
from read_parser_ini import read_ini

GREEK_NUMBER_RE = r"[\d\.]+,\d{2}"  # r'[0-9]+(\.[0-9]+)?(\,[0-9]+)?')"
GREEK_ACCOUNT_RE = r"[0-9\.]+"
CFG = read_ini()
ILine = namedtuple('ILine', 'acc per xre pis ypo normal_ypo')


def is_greek_number(txtval: str):
    res = re.fullmatch(GREEK_NUMBER_RE, txtval)
    if res:
        return True
    return False


def is_greek_account(txtval: str):
    res = re.fullmatch(GREEK_ACCOUNT_RE, txtval)
    if res:
        return True
    return False


def gr2f(txtNumber):
    """
    Convert Greek formatted number to float
    """
    return float(txtNumber.replace('.', '').replace(',', '.'))


def parse_header(line: str, slic: slice) -> str:
    return line[slic].strip()


def parse_line(line: str):
    acc = line[CFG.acc].strip()
    per = line[CFG.per].strip()
    xre = line[CFG.xre].strip()
    pis = line[CFG.pis].strip()
    if all([is_greek_account(acc), is_greek_number(xre), is_greek_number(pis)]):
        dxre = gr2f(xre)
        dpis = gr2f(pis)
        ypo = round(dxre - dpis, 2)
        omada = acc[0]
        normal_ypo = ypo
        if omada in CFG.fpa.negative_omades:
            normal_ypo = -ypo
        return ILine(acc, per, dxre, dpis, ypo, normal_ypo)
    return None


def parse_file(isozygio_file: str):
    name = ''
    apo = ''
    eos = ''
    lines = []
    with open(isozygio_file, 'r', encoding='WINDOWS-1253') as f:
        flines = f.readlines()
        for i, line in enumerate(flines):
            if i == CFG.name.line_no:
                name = parse_header(line, CFG.name.slice)
            if i == CFG.apo.line_no:
                apo = parse_header(line, CFG.apo.slice)
            if i == CFG.eos.line_no:
                eos = parse_header(line, CFG.eos.slice)
            lin = parse_line(line)
            if lin:
                lines.append(lin)
    return name, apo, eos, lines


def filter_low_level(accounts: list) -> list:
    low_level = []
    for i, acc in enumerate(accounts):
        if i == 0:
            low_level.append(acc)
            continue
        if acc.startswith(low_level[-1]):
            low_level.pop()
            low_level.append(acc)
            continue
        else:
            low_level.append(acc)
    return low_level


def filter_fpa(accounts: list) -> list:
    only_fpa = []
    for acc in accounts:
        if acc[0] in CFG.fpa.omades:
            only_fpa.append(acc)
    return only_fpa


def filter_lines(lines: list, filter_func):
    accounts = [line.acc for line in lines]
    lines_dict = {l.acc: l for l in lines}
    filtered_accounts = filter_func(accounts)
    filtered = []
    for acc, line in lines_dict.items():
        if acc in filtered_accounts:
            filtered.append(line)
    return filtered


def calculate_fpa_from_isozygio(low_level: list):
    total = 0
    for lin in low_level:
        if lin.acc.startswith(CFG.fpa.exception):
            continue
        if lin.acc.startswith(CFG.fpa.account):
            total += lin.ypo
    return round(-total, 2)


def dict_for_fpa(isozygio_file: str, acc_file: str, pistotiko: float = 0) -> dict:
    name, apo, eos, lines = parse_file(isozygio_file)
    low_level = filter_lines(lines, filter_low_level)
    only_fpa = filter_lines(low_level, filter_fpa)
    fpa = calculate_fpa_from_isozygio(low_level)
    accounts = [line.acc for line in only_fpa]
    acf.create_accounts_file(acc_file, accounts)
    acc_fpa = acf.read_accounts_file(acc_file)
    fpa_final = {
        'epon': name,
        'apo': apo,
        'eos': eos,
        'D401': pistotiko,
        'D5400': fpa,
    }
    for line in only_fpa:
        key = acc_fpa[line.acc]
        fpa_final[key] = round(fpa_final.get(key, 0) + line.normal_ypo, 2)
    return fpa_final


if __name__ == '__main__':
    print(dict_for_fpa('is2021d.txt', 'accfpa.txt', pistotiko=0))
