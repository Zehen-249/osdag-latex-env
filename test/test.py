import os,subprocess
from osdag_latex_env import OsdagLatexEnv

latex_env = OsdagLatexEnv()
print("Available LaTeX:", latex_env.available)

print("Checking for pdflatex:", latex_env.has("pdflatex"))
pdflatex_exec = latex_env.get_pdflatex()
print("Path to pdflatex:", pdflatex_exec)
print("Checking tex root:", latex_env.tex_root)

latex_env.pdflatex("inputs.tex", extra_args=["-interaction=nonstopmode","-output-directory=output"])