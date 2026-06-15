# publish.py — run this once locally to build the static web files
# Then push the contents of the "build/web" folder to your gh-pages branch

import subprocess
import sys

if __name__ == "__main__":
    print("Building portfolio as static web app...")
    result = subprocess.run(
        [sys.executable, "-m", "flet", "build", "web", "--output", "build/web"],
        capture_output=False,
    )
    if result.returncode == 0:
        print("\n✅ Done! Upload the contents of build/web/ to your GitHub Pages branch.")
        print("   Make sure assets/commit_history.png and assets/pr_logs.png are included.")
    else:
        print("\n❌ Build failed. Make sure flet is installed: pip install flet")
