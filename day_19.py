#!/usr/bin/env python
import re
from collections import defaultdict

molecule1 = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
molecule2 = "e"
replacements = defaultdict(list)
reverse_replacements = {}

with open("day_19_input") as f:
        for line in f.readlines():
            frm, _, to = line.strip().split()
            replacements[frm].append(to)
            reverse_replacements[to] = frm

reverse_keys = list(reverse_replacements.keys())
reverse_keys.sort(key=lambda x:len(x))
reverse_keys.reverse()



def one_step_mutations_count(atoms):
    previous_combs = set()
    current_combs = set()
    total = 0

    for idx, atom in enumerate(atoms):
        current_combs.clear()
        if atom in replacements:
            for to_atom in replacements[atom]:
                new_list = list(atoms)
                new_list[idx] = to_atom
                new_comb = "".join(new_list)
                current_combs.add(new_comb)

        intersect_len = len(current_combs.intersection(previous_combs))
        current_combs_len = len(current_combs)
        # we have to remove the same combination as with previous atom mutation
        total += current_combs_len - intersect_len
        previous_combs = list(current_combs)

    print("Task1: One step mutation count", total)


# Not working... stupido idea!!!
def find_chops(mol):
    all_chops = []
    print("mol:", mol)
    for atom in reverse_replacements:
        print(atom)
        if mol.startswith(atom):

            rest = mol[len(atom):]
            if len(rest) == 0:
                all_chops.append(atom)
            else:
                rest_chops_with_atom_prefix = find_chops(rest)
                mol_chops_with_atom_prefix = [[atom] + chop for chop in rest_chops_with_atom_prefix]
                all_chops += mol_chops_with_atom_prefix

    return all_chops


def find_previous(mol, atom):
    prevs = []
    repl = reverse_replacements[atom]
    for pos in previous_positions(mol, atom):
        new_mol = mol[:pos] + repl + mol[pos + len(atom):]
        prevs.append(new_mol)
    return prevs


def previous_positions(mol, atom):
    """
    Finds all positions of atom within molecule, including overlapping positions
    see https://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
    :param mol:
    :param atom:
    :return:
    """
    return [m.start() for m in re.finditer('(?=' + atom + ')', mol)]


def find_e(mol, it=0):
    if mol == "e":
        print("'e' found, it=%d" % it)
        return it
    # No way we find "e" from here
    elif len(mol) <= 1:
        return None

    vals = []
    for atom in reverse_keys:
        for new_mol in find_previous(mol, atom):
            val = find_e(new_mol, it + 1)
            if val is not None:
                vals.append(val)
    if len(vals) == 0:
        return None
    else:
        return min(vals)


# waaaay to slow, too many combinations, stupid
def find2(mol):
    mols = {mol}
    for i in range(1, 50):
        if "e" in mols:
            print("bujakasha", i)
            return
        new_mols = set()
        for processed_mol in mols:
            for atom in reverse_replacements:
                # print(atom, processed_mol)
                for new_mol in find_previous(processed_mol, atom):
                    new_mols.add(new_mol)
        mols = new_mols
        print("round %d, mols count %d" % (i, len(mols)))


def main():
    atoms = re.findall(r'[A-Z][a-z]*', molecule1)

    # Only first part works
    # find_e(molecule1)


if __name__ == '__main__':
    main()
