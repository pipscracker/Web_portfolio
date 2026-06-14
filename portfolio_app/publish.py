import flet as ft

if __name__ == "__main__":
    print("Compiling portfolio app to static web files...")
    # Directly invokes the internal web distribution builder
    ft.app(target=None, export_as_web=True)
    print("Done! Check your project directory for a new build or dist folder.")