import os
import glob
import subprocess as sp

from apps.leases.models import LeaseTemplate
from apps.people.models import Person


def create_latex(template: LeaseTemplate, owner: Person):
    template_path = template.path.path
    tmp_path = template_path.replace(".template", "_tmp.tex")

    if tmp_path == template_path:
        return None

    # owner = read_json(opts.owner)
    # garage = read_json(opts.garage)
    # resident = read_json(opts.resident)
    # template = f"{opts.template}.template"

    with open(template_path, "r") as f:
        template_content = f.read()

    template_content = owner.populate_template(template_content, role="Owner")

    # for k, v in owner.items():
    #     template = template.replace(f"Owner{k}", v)
    #
    # for k, v in resident.items():
    #     template = template.replace(f"Resident{k}", v)
    #
    # for k, v in garage.items():
    #     template = template.replace(k, v)
    #
    with open(tmp_path, "w") as f:
        f.write(template_content)

    compile_pdf(tmp_path)


def check_tex(fn: str) -> bool:
    """Check for some possible errors, before going head-on to compile."""

    # Pre-parse:
    line_num = 0
    errors = False
    with open(f'{fn}.tex') as f:
        for line in f:
            line_num += 1

            # Some errors:
            if "begin{tabular}" in line:
                if "begin{tabular}{" not in line:
                    print(f'Missing column specification in tabular environment (line {line_num})')
                    errors = True

    if errors:
        return False

    return True


def do(command) -> bool:
    try:
        sp.run(command, shell=True, check=True)
    except sp.CalledProcessError:
        return False

    return True


def compile_pdf(full_path):
    base_path = full_path.replace(".tex", "")

    # Check common errors:
    check_tex(base_path)

    dir_name, fn = os.path.split(base_path)

    # Compile:
    do(f"cd {dir_name} && pdflatex -halt-on-error {fn}.tex")

    # Clean up:
    for ext in ['toc', 'dvi', 'log', 'out', 'mat', 'aux', 'mtc*', 'maf']:
        file_list = glob.glob(f'{base_path}.{ext}')
        for filename in file_list:
            os.remove(filename)
