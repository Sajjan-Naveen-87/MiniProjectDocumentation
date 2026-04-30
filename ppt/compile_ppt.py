import subprocess
import os
import sys

def compile_ppt():
    print("Starting Presentation Compilation Process...")
    
    # Change directory to where the presentation.tex is located
    ppt_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(ppt_dir)
    
    # Simple compilation for Beamer
    commands = [
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "presentation.tex"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "presentation.tex"]
    ]
    
    try:
        # Check if pdflatex is installed
        subprocess.run(["pdflatex", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n[ERROR] pdflatex is not installed!")
        sys.exit(1)

    # Run the compilation steps
    for idx, cmd in enumerate(commands):
        print(f"\n--- Running Step {idx+1}/{len(commands)} ---")
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        if result.returncode != 0:
            print(f"\n[ERROR] Compilation failed!")
            print(result.stdout)
            sys.exit(1)

    print("\n[SUCCESS] Presentation compiled successfully!")
    print(f"File location: {os.path.join(ppt_dir, 'presentation.pdf')}")

if __name__ == "__main__":
    compile_ppt()
