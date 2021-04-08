#!/usr/bin/python3

"""
PDF-Slim v1.1.0 by Federico Stra

`pdfslim` takes a number of PDF files and tries to optimize them
through a suitable call to `ghostscript`.

To upgrade run:
pip3 install --user --upgrade git+https://github.com/FedericoStra/pdfslim
"""


import os
import sys
import shutil
import tempfile
import subprocess
import argparse


# WARNING!!! Don't use whitespaces!!!
# Lazy way of writing a list of strings.
GS_CMD = """
    -q -dBATCH -dSAFER -dNOPAUSE -sDEVICE=pdfwrite -dCompatibilityLevel=1.4
    -dPDFSETTINGS=/ebook -dAutoRotatePages=/None
    -dColorImageDownsampleType=/Bicubic -dColorImageResolution=135
    -dGrayImageDownsampleType=/Bicubic -dGrayImageResolution=135
    -dMonoImageDownsampleType=/Bicubic -dMonoImageResolution=135
    -sOutputFile={outpath} {inpath}
""".split()

if sys.platform in ("win32", "win64"):
    GS_CMD.insert(0, "gswin64c")
else:
    GS_CMD.insert(0, "gs")


def pdf_shrink(inpath, outpath):
    """Shrink `inpath` and write the result to `outpath`."""
    cmd = [s.format(inpath=inpath, outpath=outpath) for s in GS_CMD]
    subprocess.check_call(cmd)


def subdir_path(inpath, subdir):
    """Path corresponding to `inpath` moved in `subdir`."""
    basedir, basename = os.path.split(inpath)
    os.makedirs(os.path.join(basedir, subdir), exist_ok=True)
    return os.path.join(basedir, subdir, basename)


def main():
    """
    Parse the command line arguments and run the program.
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
        epilog="Copyright 2017 Federico Stra",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--inplace", action="store_true", help="shrink the files inplace"
    )
    group.add_argument(
        "--rename",
        action="store_true",
        help="the output is the input with .pdf -> .cmp.pdf",
    )
    group.add_argument(
        "--subdir",
        default="shrunk",
        help="""subdirectory in which to save output
            (default: %(default)s); this is the default option""",
    )
    parser.add_argument(
        "files", metavar="FILES", nargs="+", help="input PDF files to convert"
    )

    args = parser.parse_args()

    if args.inplace:
        tmpdir = tempfile.mkdtemp(prefix="pdfslim_")

        def outputter(inpath):
            return os.path.join(tmpdir, os.path.basename(inpath))

        def cleanup():
            shutil.rmtree(tmpdir)

    elif args.rename:

        def outputter(inpath):
            name, ext = os.path.splitext(inpath)
            return name + ".cmp" + ext

        def cleanup():
            pass

    else:

        def outputter(inpath):
            return subdir_path(inpath, args.subdir)

        def cleanup():
            pass

    for inpath in args.files:
        outpath = outputter(inpath)
        print(inpath, "->", outpath)
        pdf_shrink(inpath, outpath)
        if args.inplace:
            shutil.move(outpath, inpath)

    cleanup()


if __name__ == "__main__":
    sys.exit(main())
