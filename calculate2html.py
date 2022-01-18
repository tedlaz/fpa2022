from configparser import RawConfigParser


def read_ini(config_file: str) -> dict:
    config = RawConfigParser()
    config.optionxform = str
    config.read(config_file, encoding='utf8')
    return dict(config['TEMPLATE'])


def dec2str(val):
    """
    Returns string with Greek Formatted decimal (12345.67 becomes 12.345,67)
    """
    if val == 0:
        return ""
    return f"{val:,.2f}".replace(".", "|").replace(",", ".").replace("|", ",")


def dict2gr(adic: dict) -> dict:
    """
    Μετατρέπει τις τιμές του adic που το κλειδί τους ξεκινά απο D σε Ελληνικό
    φορμάτ. Η παραδοχή είναι ότι όλες αυτές οι τιμές είναι Δεκαδικές.
    """
    final = {}
    for key, val in adic.items():
        if key.startswith('D'):
            final[key] = dec2str(val)
            continue
        final[key] = val
    return final


def parse(text, dname):
    """
    Παρσάρουμε τις τιμές κειμένου
    το "D123 * D345 + 3" γίνεται "dname['D123'] * dname['D345'] + 3"
    """
    tokens = text.split()
    expr = []
    for token in tokens:
        if token.startswith('D'):
            expr.append(f"{dname}['{token}']")
            continue
        expr.append(token)
    return ' '.join(expr)


def calculate(template: dict, values: dict) -> dict:
    res = {}
    for key, val in template.items():

        if val == 's':  # Είναι τιμές κειμένου οπότε δεν κάνει τίποτα
            res[key] = values.get(key, '')
            continue

        if val == '':  # Αν η τιμή είναι '' θεωρούνται απλά αριθμοί
            res[key] = values.get(key, 0)
            continue

        res[key] = round(eval(parse(val, 'res')), 2)

    return res


def readhtml(html_tmplate: str) -> str:
    with open(html_tmplate, 'r', encoding='utf8') as f:
        html = f.read()
    return html


def parsetxt2dict(txt_file: str):
    final = {}
    perigrafes = {}
    with open(txt_file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                continue
            if len(line) < 10:
                continue
            first, val = line.split('=')
            code, *perigrafi = first.split()
            if code.startswith('D'):
                try:
                    val = float(val)
                except ValueError:
                    val = 0
            final[code] = val
            perigrafes[code] = ' '.join(perigrafi)
    return final, perigrafes


def html_final(txt_file: str, inidata: dict, html_template: str) -> None:
    html_file = txt_file.replace('.txt', '.html')
    vals, _ = parsetxt2dict(txt_file)
    results = calculate(inidata, vals)
    html = html_template.format(**dict2gr(results))
    with open(html_file, 'w', encoding='utf8') as f:
        f.write(html)


def html_final_plain(data: dict, inidata: dict, html_template: str, html_file: str) -> None:
    results = calculate(inidata, data)
    html = html_template.format(**dict2gr(results))
    with open(html_file, 'w', encoding='utf8') as f:
        f.write(html)


def calc2html_from_files(txt_file: str, ini_file: str, html_template: str) -> None:
    template_dict = read_ini(ini_file)
    html_templ = readhtml(html_template)
    html_final(txt_file, template_dict, html_templ)


if __name__ == '__main__':
    calc2html_from_files('fpa_example2.txt', 'fpa.ini', 'fpa_template.html')
