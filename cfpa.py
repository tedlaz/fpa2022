import argparse

import calculate2html as c2h
import python_init as pini


def main():
    parser = argparse.ArgumentParser("fpa.main")
    parser.add_argument(
        '-i',
        '--ini',
        help='Το αρχείο που περιέχει τις παραμέτρους του προγράμματος'
    )
    parser.add_argument(
        '-t',
        '--template',
        help='Το αρχείο που περιέχει το πρότυπο του html'
    )
    parser.add_argument(
        '-f',
        '--file',
        help='Το αρχείο που περιέχει τις τιμές που θα υπολογίζονται',
        required=True
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="fpa.main version:1.0"
    )
    args = parser.parse_args()

    if args.ini:
        PARAMS = c2h.read_ini(args.ini)
    else:
        PARAMS = pini.PARAMS

    if args.template:
        F2_HTML = c2h.readhtml(args.template)
    else:
        F2_HTML = pini.F2_HTML

    c2h.html_final(args.file, PARAMS, F2_HTML)


if __name__ == '__main__':
    main()
