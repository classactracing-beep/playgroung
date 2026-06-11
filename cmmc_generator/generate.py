#!/usr/bin/env python3
"""CMMC Level 2 documentation generator.

Generates a branded Standard Practices and Procedures (SPP) document,
14 domain policies, procedure packages (procedures, forms, logs, and
checklists) for all 14 CMMC Level 2 domains, and a control mapping
matrix in Word and Excel, all driven by company_profile.json.

Usage examples:
  python generate.py spp
  python generate.py policy --domain AC
  python generate.py policy --all
  python generate.py procedures --domain IR
  python generate.py procedures --all
  python generate.py matrix
  python generate.py binder
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cmmc_gen import builders
from cmmc_gen.practices import DOMAINS
from cmmc_gen.profile import load_profile

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PROFILE = os.path.join(HERE, "company_profile.json")
DEFAULT_OUT = os.path.join(HERE, "output")


def _domain_arg(value):
    v = value.upper()
    if v not in DOMAINS:
        raise argparse.ArgumentTypeError(
            f"Unknown domain '{value}'. Choose from: {', '.join(DOMAINS)}")
    return v


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="CMMC Level 2 SPP, policy, procedure, and matrix generator")
    parser.add_argument("--profile", default=DEFAULT_PROFILE,
                        help="Path to company_profile.json")
    parser.add_argument("--out", default=DEFAULT_OUT,
                        help="Output directory (default: ./output)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("spp", help="Generate the branded SPP Word document")

    p_pol = sub.add_parser("policy", help="Generate domain policy document(s)")
    group = p_pol.add_mutually_exclusive_group(required=True)
    group.add_argument("--domain", type=_domain_arg,
                       help="Domain code, e.g. AC, AT, AU, CM, IA, IR, MA, "
                            "MP, PS, PE, RA, CA, SC, SI")
    group.add_argument("--all", action="store_true",
                       help="Generate all 14 policies")

    p_proc = sub.add_parser("procedures",
                            help="Generate procedure package(s): procedure, "
                                 "forms, logs, checklists")
    group = p_proc.add_mutually_exclusive_group(required=True)
    group.add_argument("--domain", type=_domain_arg)
    group.add_argument("--all", action="store_true")

    sub.add_parser("matrix",
                   help="Generate the control mapping matrix (Word and Excel)")

    p_bind = sub.add_parser("binder",
                            help="Generate the full branded binder "
                                 "(SPP, policies, procedures, matrix, zip)")
    p_bind.add_argument("--no-zip", action="store_true",
                        help="Skip creating the binder zip archive")

    p_list = sub.add_parser("domains", help="List the 14 CMMC Level 2 domains")

    args = parser.parse_args(argv)

    if args.command == "domains":
        for code, name in DOMAINS.items():
            print(f"  {code}  {name}")
        return 0

    try:
        profile = load_profile(args.profile)
    except (FileNotFoundError, ValueError, KeyError) as exc:
        parser.error(str(exc))

    if args.command == "spp":
        paths = [builders.build_spp(profile, os.path.join(args.out, "01_SPP"))]
    elif args.command == "policy":
        out = os.path.join(args.out, "02_Policies")
        paths = (builders.build_all_policies(profile, out) if args.all
                 else [builders.build_policy(profile, args.domain, out)])
    elif args.command == "procedures":
        out = os.path.join(args.out, "03_Procedures")
        paths = (builders.build_all_procedures(profile, out) if args.all
                 else builders.build_procedure_package(profile, args.domain, out))
    elif args.command == "matrix":
        out = os.path.join(args.out, "04_Control_Matrix")
        paths = [builders.build_matrix_docx(profile, out),
                 builders.build_matrix_xlsx(profile, out)]
    elif args.command == "binder":
        paths = builders.build_binder(profile, args.out,
                                      zip_output=not args.no_zip)

    print(f"Generated {len(paths)} file(s):")
    for p in paths:
        print(f"  {os.path.relpath(p)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
