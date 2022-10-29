def task_info(task_name):
    print(task_name)


def task_iter_info(N, h_N, I_h_N, precision, epsilon, nodes):
    if not N:
        head_print()
        return
    if len(nodes) > 24:
        nodes = nodes[0:24]
        nodes.append('...')

    print(f"{N:<3}|{h_N:<10.7f}|{I_h_N:<22}|{precision:<24}|{epsilon:<10}|{nodes}")


def head_print():
    print(f"{'N':<3}|{'h_N':<10}|{'I_h_N':<22}|{'precision':<24}|{'epsilon':<10}|{'nodes':<24}")
