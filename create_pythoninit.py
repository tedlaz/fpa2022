from calculate2html import read_ini


def create_pyini(fil='fpa.ini'):
    dictval = read_ini(fil)
    fvals = ['PARAMS = {\n']
    for k, v in dictval.items():
        fvals.append(f"    '{k}': '{v}',\n")
    fvals.append('}\n')
    return ''.join(fvals)


def get_html_template(fil='fpa_template.html'):
    with open(fil, 'r', encoding='utf8') as f:
        txt = f.read()

    final = 'F2_HTML = """\n'
    final += txt
    final += '\n"""\n'
    return final


def create_python_init(inifile='fpa.ini', htmlfile='fpa_template.html'):
    fvals = create_pyini(inifile)
    htmpar = get_html_template(htmlfile)
    with open('python_init.py', 'w', encoding='utf8') as f:
        f.write('\n'.join([fvals, htmpar]))


if __name__ == '__main__':
    create_python_init()
