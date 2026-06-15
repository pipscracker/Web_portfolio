# publish.py — run this once locally to build the static web files
# Then push the contents of the "build/web" folder to your gh-pages branch

import subprocess
import sys
import shutil

if __name__ == "__main__":
    # First check flet is installed
    if not shutil.which("flet"):
        print("❌ 'flet' CLI not found. Run:  pip install flet")
        sys.exit(1)

    print("Building portfolio as static web app...")

    # FIX: use the 'flet' CLI directly, not 'python -m flet'
    result = subprocess.run(
        ["flet", "build", "web", "--output", "build/web"],
        capture_output=False,
    )

    if result.returncode == 0:
        print("\n✅ Done! Upload the contents of build/web/ to your GitHub Pages branch.")
        print("   Make sure assets/commit_history.png and assets/pr_logs.png are included.")
    else:
        print("\n❌ Build failed.")
        print("   Try running manually:  flet build web --output build/web")
        print("   Also ensure you're in the correct folder (where main.py lives).")
