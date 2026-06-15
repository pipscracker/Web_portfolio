import flet as ft


def main(page: ft.Page):
    page.title = "My Portfolio"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT

    # --------------------------------------------------
    # DOCUMENT VIEWER STATE
    # --------------------------------------------------
    doc_viewer_title = ft.Text(
        value="Document Viewer",
        size=16,
        weight=ft.FontWeight.BOLD,
        color="blue800",
    )
    doc_viewer_desc = ft.Text(
        value="Select a certificate or report below to view it instantly.",
        size=13,
        color="grey700",
    )

    # Placeholder shown before any doc is selected
    doc_viewer_frame = ft.Container(
        content=ft.Text("No document selected", color="grey500"),
        alignment=ft.Alignment(0, 0),
        bgcolor="grey200",
        border_radius=10,
        height=500,
        expand=True,
        padding=15,
    )

    # --------------------------------------------------
    # DOCUMENT DISPLAY LOGIC
    # --------------------------------------------------
    def make_drive_preview_url(url: str) -> str:
        """Convert any Google Drive share link to the embeddable /preview URL."""
        try:
            if "/d/" in url:
                file_id = url.split("/d/")[1].split("/")[0]
            elif "id=" in url:
                file_id = url.split("id=")[1].split("&")[0]
            else:
                return url
            return f"https://drive.google.com/file/d/{file_id}/preview"
        except Exception:
            return url

    def display_doc(name: str, doc_type: str, url: str):
        if "YOUR_GOOGLE_DRIVE" in url or url.strip() == "":
            doc_viewer_title.value = "⚠️ No link set"
            doc_viewer_desc.value = f"Replace the placeholder URL for '{name}'."
            doc_viewer_frame.content = ft.Text(
                "Add your Google Drive link in the course_card() call.",
                color="red400",
                text_align=ft.TextAlign.CENTER,
            )
            page.update()
            return

        preview_url = make_drive_preview_url(url)

        doc_viewer_title.value = f"Viewing: {name} — {doc_type}"
        doc_viewer_desc.value = "Document loading below (make sure the file is shared publicly)."

        # -------------------------------------------------------
        # CROSS-PLATFORM EMBED STRATEGY
        #
        # On the WEB:  Flet renders ft.Container with an HTML
        #              iframe injected via page.client_storage /
        #              using the web-safe embed approach below.
        #
        # On DESKTOP:  ft.WebView is unavailable in many Flet
        #              versions, so we show a styled panel with
        #              an "Open in Browser" button instead.
        # -------------------------------------------------------

        # Detect if we're running in a web browser
        is_web = page.web if hasattr(page, "web") else False

        if is_web:
            # Use Flet's HTML control (web-only, Flet ≥ 0.21)
            try:
                iframe_html = (
                    f'<iframe src="{preview_url}" '
                    f'width="100%" height="480" '
                    f'style="border:none;border-radius:8px;" '
                    f'allow="autoplay"></iframe>'
                )
                doc_viewer_frame.content = ft.Html(
                    value=iframe_html,
                    expand=True,
                )
            except AttributeError:
                # ft.Html not available — fall back to link button
                _fallback_frame(name, preview_url)
        else:
            # Desktop: show a clean preview panel + open-in-browser button
            _fallback_frame(name, preview_url)

        page.update()

    def _fallback_frame(name: str, preview_url: str):
        """Shown on desktop or when ft.Html is unavailable."""
        doc_viewer_frame.content = ft.Column(
            [
                ft.Icon(ft.Icons.PICTURE_AS_PDF, size=60, color="blue300"),
                ft.Text(
                    name,
                    size=15,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color="blue800",
                ),
                ft.Text(
                    "Preview is not supported in the desktop app.\n"
                    "Click the button below to open the document.",
                    size=13,
                    color="grey600",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    content=ft.Text(
                        "Open Document ↗",
                        size=13,
                        weight=ft.FontWeight.W_600,
                        color="white",
                    ),
                    bgcolor="blue600",
                    border_radius=8,
                    padding=ft.Padding(left=20, top=10, right=20, bottom=10),
                    on_click=lambda e: page.launch_url(preview_url),
                    ink=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
        )

    # --------------------------------------------------
    # COURSE CARD
    # --------------------------------------------------
    def course_card(name: str, cert_url: str, report_url: str) -> ft.Container:
        def on_cert(e, n=name, u=cert_url):
            display_doc(n, "Certificate", u)

        def on_report(e, n=name, u=report_url):
            display_doc(n, "Report", u)

        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Text(
                            name,
                            weight=ft.FontWeight.BOLD,
                            size=13,
                            text_align=ft.TextAlign.CENTER,
                            color="white",
                        ),
                        height=40,
                        alignment=ft.Alignment(0, 0),
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text("Certificate", size=11, weight=ft.FontWeight.W_500, color="black"),
                                bgcolor="white",
                                border_radius=4,
                                padding=6,
                                on_click=on_cert,
                                ink=True,
                            ),
                            ft.Container(
                                content=ft.Text("Report", size=11, weight=ft.FontWeight.W_500, color="black"),
                                bgcolor="white",
                                border_radius=4,
                                padding=6,
                                on_click=on_report,
                                ink=True,
                            ),
                        ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            border_radius=10,
            bgcolor="blue400",
            width=210,
            height=115,
        )

    # --------------------------------------------------
    # LOG CARD (GitHub Evidence)
    # --------------------------------------------------
    def log_card(title: str, url: str) -> ft.Container:
        def on_view(e, n=title, u=url):
            display_doc(n, "Log", u)

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, weight=ft.FontWeight.BOLD, size=13, color="white", text_align=ft.TextAlign.CENTER),
                    ft.Container(
                        content=ft.Text("View Logs", size=11, weight=ft.FontWeight.W_500, color="black"),
                        bgcolor="white",
                        border_radius=4,
                        padding=ft.Padding(left=12, top=6, right=12, bottom=6),
                        on_click=on_view,
                        ink=True,
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=15,
            border_radius=10,
            bgcolor="blue300",
            width=220,
            height=110,
        )

    # ==================================================
    # TAB CONTENT BUILDERS
    # ==================================================

    # --- TAB 1: PROJECT TIMELINE ---
    def build_timeline_tab():
        def week_entry(label, desc):
            return ft.Column([
                ft.Text(label, weight=ft.FontWeight.BOLD, size=14),
                ft.Text(f"- {desc}", size=13, color="grey800"),
                ft.Container(height=4),
            ], spacing=2)

        return ft.Container(
            content=ft.Column([
                ft.Text("Project Timeline", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                week_entry("Week 1-3", "Initial repository structure setup and architectural planning."),
                week_entry("Week 4-5", "Developed core calculation algorithms and engineering parsing modules."),
                week_entry("Week 6-7", "Implemented data validation logic and ran integration unit tests."),
                week_entry("Week 8-9", "UI layout mockups, debugging component scripts, and resolving data validation issues."),
            ], spacing=8),
            padding=20,
        )

    # --- TAB 2: MATLAB HUB ---
    def build_matlab_tab():
        courses_grid = ft.Row(
            controls=[
                course_card(
                    "MATLAB Onramp",
                    "https://drive.google.com/file/d/1TM1m1WPlafXRTWPksWGXz-BRCKIMGg8f/view?usp=drive_link",
                    "https://drive.google.com/file/d/1bVQbldVf0MLGgGbebD0SBrKq5TXXmXoZ/view?usp=drive_link"
                ),
                course_card(
                    "Simulink Onramp",
                    "https://drive.google.com/file/d/1susucT9qSVG8HOSifw-nsye4HhWnr4qA/view?usp=drive_link",
                    "https://drive.google.com/file/d/15YsdS3ljtY0lKfAt1KnLBdxsDuDXpBU_/view?usp=drive_link"
                ),
                course_card(
                    "Calculations with Vectors\nand Matrices",
                    "https://drive.google.com/file/d/1tLh2bpIYwulD5uHZEEW4mzkBFaC5smoS/view?usp=drive_link",
                    "https://drive.google.com/file/d/1wngp-XVqnvCtYTtCVNeFapEypH6rqODt/view?usp=drive_link"
                ),
                course_card(
                    "Make and Manipulate Matrices",
                    "https://drive.google.com/file/d/15rPC-WyKnU30nZPPPEPKLE3OtXRzjc7c/view?usp=drive_link",
                    "https://drive.google.com/file/d/1kWXR3r3h_dNRksWqpnGaJoO3puz49ow0/view?usp=drive_link"
                ),
                course_card(
                    "Explore Data with MATLAB Plots",
                    "https://drive.google.com/file/d/1a7h-ZjRK4WbEKdBkb9vtWOxUWbUeazto/view?usp=drive_link",
                    "https://drive.google.com/file/d/1qH3xnAN99Zeo_uUmdZaAs9raEDoXWOSo/view?usp=drive_link"
                ),
                course_card(
                    "Wireless Communications\nOnramp",
                    "https://drive.google.com/file/d/1Y0DE6wGDozeZPm5sJDg6_T5MRdjMPgS5/view?usp=drive_link",
                    "https://drive.google.com/file/d/1BvdHNeaCp24rYq42Vs2GHPSLY2uOEyAk/view?usp=drive_link"
                ),
                course_card(
                    "Machine Learning Onramp",
                    "https://drive.google.com/file/d/1JobPmk9J57UFfKxRrQ0nc9jEjkhszGOG/view?usp=drive_link",
                    "https://drive.google.com/file/d/1vI24rs8Wi2C4waV16Tnxwjcp1MgX2TZD/view?usp=drive_link"
                ),
            ],
            spacing=15,
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        viewer_panel = ft.Container(
            content=ft.Column(
                [doc_viewer_title, doc_viewer_desc, doc_viewer_frame],
                spacing=10,
            ),
            padding=15,
            border=ft.Border(
                top=ft.BorderSide(1, "grey300"),
                bottom=ft.BorderSide(1, "grey300"),
                left=ft.BorderSide(1, "grey300"),
                right=ft.BorderSide(1, "grey300"),
            ),
            border_radius=10,
        )

        return ft.Container(
            content=ft.Column([
                ft.Text("MATLAB Achievement Hub", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Text("Completed Courses :", size=14, color="grey700"),
                courses_grid,
                ft.Container(height=10),
                ft.Text("Document Showcase", size=16, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Click on any course certificate or report button above to preview the document below.",
                    size=13,
                    color="grey600",
                ),
                viewer_panel,
            ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.START),
            padding=20,
        )

    # --- TAB 3: TECHNICAL BLOG ---
    def build_blog_tab():
        return ft.Container(
            content=ft.Column([
                ft.Text("Technical Blog", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Text("Confidence in Concepts", size=18, weight=ft.FontWeight.BOLD, color="blue700"),
                ft.Divider(),
                ft.Text("Topic 1: How does a database work?", weight=ft.FontWeight.BOLD, size=14),
                ft.Text(
                    "At its core, a database is an optimized system built to store, manage, and retrieve data "
                    "seamlessly. It operates across three fundamental layers: the Storage Engine, which structures "
                    "physical files on disk using B-Trees or indexes for rapid access; the Query Engine, which parses "
                    "and optimizes execution paths; and the Transaction Manager, which guarantees data safety via ACID compliance.",
                    size=13,
                ),
                ft.Divider(),
                ft.Text("Topic 2: Material Cost Optimisation Formula", weight=ft.FontWeight.BOLD, size=14),
                ft.Text(
                    "When managing physical design variables across mining and civil engineering subsystems, "
                    "calculations must align with true financial bounds:",
                    size=13,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Total_Cost = Σ (Qᵢ × Pᵢ) + Overheads",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color="blue700",
                        ),
                        ft.Text(
                            "Where: Qᵢ = Quantity of material i,  Pᵢ = Unit Price of material i",
                            size=12,
                            color="grey600",
                            italic=True,
                        ),
                    ], spacing=4),
                    bgcolor="blue50",
                    border_radius=8,
                    padding=ft.Padding(left=20, top=12, right=20, bottom=12),
                ),
                ft.Container(height=10),
                ft.Text("Embedded Video Explanation:", weight=ft.FontWeight.BOLD, size=14),
                ft.Container(
                    content=ft.Column([
                        ft.Icon(ft.Icons.PLAY_CIRCLE_OUTLINE, size=60, color="blue300"),
                        ft.Text(
                            "Replace the URL below with your YouTube embed link.",
                            size=12,
                            color="grey600",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Watch Video ↗",
                                size=13,
                                weight=ft.FontWeight.W_600,
                                color="white",
                            ),
                            bgcolor="blue600",
                            border_radius=8,
                            padding=ft.Padding(left=20, top=10, right=20, bottom=10),
                            on_click=lambda e: page.launch_url("https://www.youtube.com/watch?v=YOUR_VIDEO_ID"),
                            ink=True,
                        ),
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=12),
                    bgcolor="grey100",
                    border_radius=10,
                    height=200,
                    alignment=ft.Alignment(0, 0),
                    padding=20,
                ),
            ], spacing=12),
            padding=20,
        )

    # --- TAB 4: GITHUB EVIDENCE ---
    def build_github_tab():
        return ft.Container(
            content=ft.Column([
                ft.Text("GitHub Evidence & Documentation", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Text(
                    "Large-Scale Team Collaboration Verification (20 Members Group)",
                    size=13, italic=True, color="grey700",
                ),
                ft.Container(height=8),
                ft.Text("1. Commit History", size=16, weight=ft.FontWeight.BOLD, color="blue700"),
                ft.Text(
                    "Verified log updates and source tracking metrics mapped directly back to the main branch repository Architecture:",
                    size=13,
                ),
                log_card("Commit History Log", "YOUR_COMMIT_LOG_URL"),
                ft.Container(height=8),
                ft.Text("2. Pull Request Logs", size=16, weight=ft.FontWeight.BOLD, color="blue700"),
                ft.Text(
                    "Detailed features proposed, structured code reviews performed, and team merges completed successfully:",
                    size=13,
                ),
                log_card("Pull Request Logs", "YOUR_PR_LOG_URL"),
                ft.Container(height=8),
                ft.Text("3. Impact Summary", size=16, weight=ft.FontWeight.BOLD, color="blue700"),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "My specific script modifications and hardware interface abstraction logic directly resolved "
                            "critical processing deadlocks within the application's Metallurgical, Mining, and Civil "
                            "engineering estimation sub-modules.",
                            size=13,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Container(height=6),
                        ft.Text(
                            "By cleaning up async calculation steps, processing overhead for large material cost "
                            "computations was minimized, ensuring accurate performance calculations across multi-disciplinary teams.",
                            size=13,
                        ),
                    ]),
                    bgcolor="blue50",
                    border_radius=8,
                    padding=ft.Padding(left=16, top=14, right=16, bottom=14),
                ),
            ], spacing=12),
            padding=20,
        )

    # ==================================================
    # TAB SWITCHING
    # ==================================================
    content_area = ft.Container(expand=True)

    tab_names    = ["Project Timeline", "MATLAB Hub", "Technical Blog", "GitHub Evidence"]
    tab_builders = [build_timeline_tab, build_matlab_tab, build_blog_tab, build_github_tab]
    tab_buttons  = []

    def switch_tab(index: int):
        for i, btn in enumerate(tab_buttons):
            btn.bgcolor = "blue600" if i == index else "grey200"
            btn.content.color = "white" if i == index else "grey800"
        content_area.content = tab_builders[index]()
        page.update()

    for i, name in enumerate(tab_names):
        btn = ft.Container(
            content=ft.Text(name, size=13, weight=ft.FontWeight.W_500, color="grey800"),
            bgcolor="grey200",
            border_radius=20,
            padding=ft.Padding(left=16, top=8, right=16, bottom=8),
            on_click=lambda e, idx=i: switch_tab(idx),
            ink=True,
        )
        tab_buttons.append(btn)

    tab_bar = ft.Row(
        controls=tab_buttons,
        spacing=8,
        wrap=True,
        alignment=ft.MainAxisAlignment.START,
    )

    # --------------------------------------------------
    # HEADER
    # --------------------------------------------------
    header_panel = ft.Container(
        content=ft.Column([
            ft.Text("My Portfolio", size=28, weight=ft.FontWeight.BOLD, color="white"),
            ft.Text("Ireneus Shilunga | Electronics and Computer Engineering", size=15, color="white70"),
            ft.Text("Student No: 225030969", size=13, color="white70"),
            ft.Text("© 2026 UNAM", size=12, color="white54"),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor="blue600",
        padding=20,
        border_radius=15,
        alignment=ft.Alignment(0, 0),
        expand=True,
    )

    switch_tab(1)  # default to MATLAB Hub

    page.add(
        ft.Container(
            content=ft.Column([
                header_panel,
                ft.Divider(height=1, color="grey300"),
                tab_bar,
                ft.Divider(height=1, color="grey300"),
                content_area,
            ], spacing=12, expand=True),
            padding=20,
            expand=True,
        )
    )


ft.app(target=main, assets_dir="assets")
