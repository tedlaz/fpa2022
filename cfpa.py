import argparse

from calculate2html import html_final_plain
from isozygio_parse import dict_for_fpa
from python_init import F2_HTML, PARAMS


def run():
    parser = argparse.ArgumentParser("Υπολογισμός ΦΠΑ από Ισοζύγιο")
    parser.add_argument(
        'isofile',
        help='Το αρχείο που περιέχει τo Ισοζύγιο περιόδου'
    )
    parser.add_argument(
        '-c',
        '--credit',
        help='Πιστωτικό υπόλοιπο προηγούμενης περιόδου'
    )

    args = parser.parse_args()

    pistotiko = float(args.credit) if args.credit else 0.0
    isozygio_file_path = args.isofile
    data = dict_for_fpa(isozygio_file_path, 'accfpa.txt', pistotiko)

    html_file_path = isozygio_file_path.replace('.txt', '.html')
    html_final_plain(data, PARAMS, F2_HTML, html_file_path)


if __name__ == "__main__":
    run()
