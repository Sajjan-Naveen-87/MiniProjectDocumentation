import subprocess
import os
import sys

def compile_latex():
    print("Starting LaTeX Compilation Process...")
    
    # Change directory to where the report.tex is located
    report_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(report_dir)
    
    # The commands to run. We run pdflatex multiple times to resolve Table of Contents and References.
    commands = [
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "report.tex"],
        ["bibtex", "report"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "report.tex"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "report.tex"]
    ]
    
    try:
        # Check if pdflatex is actually installed on the system
        subprocess.run(["pdflatex", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n[ERROR] LaTeX is not installed on your system!")
        print("To run this script on a Mac, you MUST install MacTeX first.")
        print("Download it here: https://tug.org/mactex/ (Warning: It is a 5GB download)")
        print("Or install BasicTeX via Homebrew: brew install --cask basictex\n")
        sys.exit(1)

    # Run the compilation steps
    for idx, cmd in enumerate(commands):
        print(f"\n--- Running Step {idx+1}/{len(commands)}: {' '.join(cmd)} ---")
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        if result.returncode != 0:
            print(f"\n[ERROR] Compilation failed during step: {cmd[0]}")
            print("Here is the error log:\n")
            print(result.stdout)
            sys.exit(1)
            
    print("\n[SUCCESS] Compilation complete! The PDF 'report.pdf' has been generated in the current directory.")

if __name__ == "__main__":
    compile_latex()
