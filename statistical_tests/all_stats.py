from statistical_tests import (
    binary_random,
    chi_squared,
    dic,
    doublets,
    frequency,
    ioc,
    lr,
    normor,
    quadruplets,
    rod,
    sdd,
    shannon_entropy,
    triplets,
    rdi,
    dbic,
    mic,
    mka,
    edi,
    ldi
)


algos = {
    "IOC": ioc.get_ioc,
    "MIC": mic.get_max_periodic_ic,
    "MKA": mka.get_kappa,
    "DIC": dic.get_dic,
    "EDI": edi.get_even_dic,
    "LR": lr.get_lr,
    "ROD": rod.get_rod,
    "LDI": ldi.get_ldi,
    "SDD": sdd.get_sdd,
    "NORMOR": normor.get_normor,
    "RDI": rdi.get_rdi,
    # "Doublets": doublets.get_doublets,
    # "DBIC": dbic.get_dbic,
}


def get_all_stats(text):
    results = {}
    for algo in algos:
        results[algo] = algos[algo](text)
    return results
