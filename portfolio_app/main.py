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
        color=ft.colors.BLUE_800,          # FIX: was "blue800" (invalid string)
    )
    doc_viewer_desc = ft.Text(
        value="Select a certificate or report below to view it instantly.",
        size=13,
        color=ft.colors.GREY_700,          # FIX: was "grey700"
    )
    doc_viewer_image = ft.Image(
        src="",
        fit=ft.ImageFit.CONTAIN,           # FIX: was string "contain"
        visible=False,
        expand=True,
    )
    doc_viewer_placeholder = ft.Text("No document selected", color=ft.colors.GREY_500)  # FIX: color string

    doc_viewer_frame = ft.Container(
        content=ft.Column(
            [doc_viewer_placeholder, doc_viewer_image],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        alignment=ft.alignment.center,     # FIX: was ft.Alignment(0, 0) — use ft.alignment.center
        bgcolor=ft.colors.GREY_200,        # FIX: was "grey200"
        border_radius=10,
        height=500,
        expand=True,
        padding=15,
    )

    # --------------------------------------------------
    # DISPLAY LOGIC
    # --------------------------------------------------
    def display_doc(name: str, doc_type: str, image_path: str):
        doc_viewer_title.value = f"Viewing: {name} — {doc_type}"
        doc_viewer_desc.value = "Document image loaded from local assets."
        doc_viewer_placeholder.visible = False
        doc_viewer_image.src = image_path
        doc_viewer_image.visible = True
        page.update()

    # --------------------------------------------------
    # COURSE CARD
    # --------------------------------------------------
    def course_card(name: str, cert_image: str, report_image: str) -> ft.Container:
        def on_cert(e, n=name, img=cert_image):
            display_doc(n, "Certificate", img)

        def on_report(e, n=name, img=report_image):
            display_doc(n, "Report", img)

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
                        alignment=ft.alignment.center,   # FIX: was ft.Alignment(0,0)
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(
                                    "Certificate",
                                    size=11,
                                    weight=ft.FontWeight.W_500,
                                    color="black",
                                ),
                                bgcolor="white",
                                border_radius=4,
                                padding=6,
                                on_click=on_cert,
                                ink=True,
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Report",
                                    size=11,
                                    weight=ft.FontWeight.W_500,
                                    color="black",
                                ),
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
            bgcolor=ft.colors.BLUE_400,    # FIX: was "blue400"
            width=210,
            height=115,
        )

    # --------------------------------------------------
    # LOG IMAGE CARD (GitHub Evidence)
    # --------------------------------------------------
    def log_image_card(title: str, image_path: str) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        title,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                        color=ft.colors.BLUE_800,          # FIX: was "blue800"
                        text_align=ft.TextAlign.LEFT,
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=image_path,
                            fit=ft.ImageFit.CONTAIN,        # FIX: was ft.ImageFit.CONTAIN but still good
                            border_radius=8,
                            height=300,                     # FIX: CRITICAL — missing height caused crash
                            width=float("inf"),             # let it stretch horizontally
                        ),
                        border=ft.border.all(1, ft.colors.GREY_300),  # FIX: was manual Border() construction
                        border_radius=8,
                        bgcolor=ft.colors.GREY_100,        # FIX: was "grey100"
                        padding=8,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    ),
                ],
                spacing=8,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=0,                                      # FIX: was ft.Padding(0,0,0,0) — just use 0
        )

    # ==================================================
    # TAB 1: PROJECT TIMELINE
    # ==================================================
    def build_timeline_tab():
        def week_entry(label, desc):
            return ft.Column(
                [
                    ft.Text(label, weight=ft.FontWeight.BOLD, size=14),
                    ft.Text(f"- {desc}", size=13, color=ft.colors.GREY_800),
                    ft.Container(height=4),
                ],
                spacing=2,
            )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Project Timeline", size=22, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    week_entry("Week 1-3", "Initial repository structure setup and architectural planning."),
                    week_entry("Week 4-5", "Developed core calculation algorithms and engineering parsing modules."),
                    week_entry("Week 6-7", "Implemented data validation logic and ran integration unit tests."),
                    week_entry(
                        "Week 8-9",
                        "UI layout mockups, debugging component scripts, and resolving data validation issues.",
                    ),
                ],
                spacing=8,
            ),
            padding=20,
        )

    # ==================================================
    # TAB 2: MATLAB HUB
    # ==================================================
    def build_matlab_tab():
        courses_grid = ft.Row(
            controls=[
                course_card(
                    "MATLAB Onramp",
                    "docs/matlab_onramp_certificate-1.png",
                    "docs/matlab_onramp_report-1.png",
                ),
                course_card(
                    "Simulink Onramp",
                    "docs/simulink_onramp_certificate-1.png",
                    "docs/simulink_onramp_report-1.png",
                ),
                course_card(
                    "Calculations with Vectors\nand Matrices",
                    "docs/Calculations_with_Vectors_and_Matrices_certificate-1.png",
                    "docs/Calculations_with_Vectors_and_Matrices_report-1.png",
                ),
                course_card(
                    "Make and Manipulate Matrices",
                    "docs/Make_and_Manipulate_Matrices_certificate-1.png",
                    "docs/Make_and_Manipulate_Matrices_report-1.png",
                ),
                course_card(
                    "Explore Data with MATLAB Plots",
                    "docs/Explore_Data_with_MATLAB_Plots_certificate-1.png",
                    "docs/Explore_Data_with_MATLAB_Plots_report-1.png",
                ),
                course_card(
                    "Wireless Communications\nOnramp",
                    "docs/Wireless_Communications_Onramp_certificate-1.png",
                    "docs/Wireless_Communications_Onramp_report-1.png",
                ),
                course_card(
                    "Machine Learning Onramp",
                    "docs/Machine_Learning_Onramp_certificate-1.png",
                    "docs/Machine_Learning_Onramp_report-1.png",
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
            border=ft.border.all(1, ft.colors.GREY_300),   # FIX: was manual Border() construction
            border_radius=10,
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("MATLAB Achievement Hub", size=22, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text("Completed Courses :", size=14, color=ft.colors.GREY_700),
                    courses_grid,
                    ft.Container(height=10),
                    ft.Text("Document Showcase", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Click on any course certificate or report button above to preview the document below.",
                        size=13,
                        color=ft.colors.GREY_600,
                    ),
                    viewer_panel,
                ],
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=20,
        )

    # ==================================================
    # TAB 3: TECHNICAL BLOG
    # ==================================================
    def build_blog_tab():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Technical Blog", size=22, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text(
                        "Confidence in Concepts",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLUE_700,          # FIX: was "blue700"
                    ),
                    ft.Divider(),
                    ft.Text(
                        "Topic 1: How does a database work?",
                        weight=ft.FontWeight.BOLD,
                        size=14,
                    ),
                    ft.Text(
                        "At its core, a database is an optimized system built to store, manage, and retrieve data "
                        "seamlessly. It operates across three fundamental layers: the Storage Engine, which structures "
                        "physical files on disk using B-Trees or indexes for rapid access; the Query Engine, which parses "
                        "and optimizes execution paths; and the Transaction Manager, which guarantees data safety via ACID compliance.",
                        size=13,
                    ),
                    ft.Divider(),
                    ft.Text(
                        "Topic 2: Material Cost Optimisation Formula",
                        weight=ft.FontWeight.BOLD,
                        size=14,
                    ),
                    ft.Text(
                        "When managing physical design variables across mining and civil engineering subsystems, "
                        "calculations must align with true financial bounds:",
                        size=13,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Total_Cost = Σ (Qᵢ × Pᵢ) + Overheads",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLUE_700,  # FIX: was "blue700"
                                ),
                                ft.Text(
                                    "Where: Qᵢ = Quantity of material i,  Pᵢ = Unit Price of material i",
                                    size=12,
                                    color=ft.colors.GREY_600,  # FIX: was "grey600"
                                    italic=True,
                                ),
                            ],
                            spacing=4,
                        ),
                        bgcolor=ft.colors.BLUE_50,         # FIX: was "blue50"
                        border_radius=8,
                        padding=ft.padding.symmetric(horizontal=20, vertical=12),  # FIX: cleaner padding
                    ),
                    ft.Container(height=10),
                    ft.Text("Embedded Video Explanation:", weight=ft.FontWeight.BOLD, size=14),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.PLAY_CIRCLE_OUTLINE, size=60, color=ft.colors.BLUE_300),
                                ft.Text(
                                    "Replace the URL below with your YouTube embed link.",
                                    size=12,
                                    color=ft.colors.GREY_600,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "Watch Video ↗",
                                        size=13,
                                        weight=ft.FontWeight.W_600,
                                        color="white",
                                    ),
                                    bgcolor=ft.colors.BLUE_600,
                                    border_radius=8,
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                    on_click=lambda e: page.launch_url(
                                        "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
                                    ),
                                    ink=True,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=12,
                        ),
                        bgcolor=ft.colors.GREY_100,
                        border_radius=10,
                        height=200,
                        alignment=ft.alignment.center,     # FIX: was ft.Alignment(0,0)
                        padding=20,
                    ),
                ],
                spacing=12,
            ),
            padding=20,
        )

    # ==================================================
    # TAB 4: GITHUB EVIDENCE
    # ==================================================
    def build_github_tab():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "GitHub Evidence & Documentation",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Divider(),
                    ft.Text(
                        "Large-Scale Team Collaboration Verification (20 Members Group)",
                        size=13,
                        italic=True,
                        color=ft.colors.GREY_700,
                    ),
                    ft.Container(height=8),
                    ft.Text("1. Commit History", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700),
                    ft.Text(
                        "Verified log updates and source tracking metrics mapped directly back to the main branch repository Architecture:",
                        size=13,
                    ),
                    log_image_card("Commit History Log", "assets/commit_history.png"),
                    ft.Container(height=8),
                    ft.Text("2. Pull Request Logs", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700),
                    ft.Text(
                        "Detailed features proposed, structured code reviews performed, and team merges completed successfully:",
                        size=13,
                    ),
                    log_image_card("Pull Request Logs", "assets/pr_logs.png"),
                    ft.Container(height=8),
                    ft.Text("3. Impact Summary", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700),
                    ft.Container(
                        content=ft.Column(
                            [
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
                            ]
                        ),
                        bgcolor=ft.colors.BLUE_50,
                        border_radius=8,
                        padding=ft.padding.symmetric(horizontal=16, vertical=14),  # FIX: was ft.Padding()
                    ),
                ],
                spacing=12,
            ),
            padding=20,
        )

    # ==================================================
    # TAB SWITCHING
    # ==================================================
    content_area = ft.Container(expand=True)

    tab_names = ["Project Timeline", "MATLAB Hub", "Technical Blog", "GitHub Evidence"]
    tab_builders = [build_timeline_tab, build_matlab_tab, build_blog_tab, build_github_tab]
    tab_buttons = []

    def switch_tab(index: int):
        for i, btn in enumerate(tab_buttons):
            btn.bgcolor = ft.colors.BLUE_600 if i == index else ft.colors.GREY_200
            btn.content.color = "white" if i == index else ft.colors.GREY_800
        content_area.content = tab_builders[index]()
        page.update()

    for i, name in enumerate(tab_names):
        btn = ft.Container(
            content=ft.Text(name, size=13, weight=ft.FontWeight.W_500, color=ft.colors.GREY_800),
            bgcolor=ft.colors.GREY_200,
            border_radius=20,
            padding=ft.padding.symmetric(horizontal=16, vertical=8),  # FIX: was ft.Padding()
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
        content=ft.Column(
            [
                ft.Text("My Portfolio", size=28, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text(
                    "Ireneus Shilunga | Electronics and Computer Engineering",
                    size=15,
                    color="white70",
                ),
                ft.Text("Student No: 225030969", size=13, color="white70"),
                ft.Text("© 2026 UNAM", size=12, color="white54"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.BLUE_600,
        padding=20,
        border_radius=15,
        alignment=ft.alignment.center,    # FIX: was ft.Alignment(0,0)
        expand=True,
    )

    switch_tab(1)  # default to MATLAB Hub

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    header_panel,
                    ft.Divider(height=1, color=ft.colors.GREY_300),
                    tab_bar,
                    ft.Divider(height=1, color=ft.colors.GREY_300),
                    content_area,
                ],
                spacing=12,
                expand=True,
            ),
            padding=20,
            expand=True,
        )
    )


ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
