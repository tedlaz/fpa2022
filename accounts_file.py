import os


def read_accounts_file(filename, raise_exeption=True):
    acc_ds = {}
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            flines = f.readlines()
            for fline in flines:
                if len(fline.strip()) < 4:
                    continue
                account, *fpapar = fline.split()
                if fpapar != []:
                    acc_ds[account] = fpapar[0]
                else:
                    if raise_exeption:
                        raise ValueError(
                            f'Παρακαλώ δώστε κωδικό στο λογαριασμό {account}')
                    else:
                        acc_ds[account] = ''
    return acc_ds


def create_accounts_file(filename, accounts):
    acc_ds = {}

    if os.path.exists(filename):
        try:
            acc_ds = read_accounts_file(filename, raise_exeption=False)
        except ValueError as e:
            pass

    for acc in accounts:
        if acc not in acc_ds.keys():
            acc_ds[acc] = ''

    new_acc_list = []
    for key in sorted(acc_ds.keys()):
        new_acc_list.append(f'{key} {acc_ds[key]}')

    with open(filename, 'w', encoding='utf8') as f:
        f.write('\n'.join(new_acc_list))
