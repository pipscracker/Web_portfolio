import flet as ft
import flet_video as ftv  # inline video player — requires: pip install flet-video


def main(page: ft.Page):
    page.title = "My Portfolio"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT

    # --------------------------------------------------
    # DOCUMENT VIEWER — full screen overlay via page.overlay
    # --------------------------------------------------
    overlay_title = ft.Text("", size=15, weight=ft.FontWeight.BOLD, color="#1565C0")
    overlay_image = ft.Image(src="", fit="contain", width=700, height=500)

    def close_viewer(e=None):
        page.overlay.clear()
        page.update()

    overlay_panel = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        overlay_title,
                        ft.Container(expand=True),
                        ft.TextButton("✕  Close", on_click=close_viewer),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(),
                ft.Container(
                    content=overlay_image,
                    bgcolor="#EEEEEE",
                    border_radius=8,
                    padding=10,
                    alignment=ft.Alignment(0, 0),
                ),
            ],
            spacing=8,
            tight=True,
        ),
        bgcolor="white",
        border_radius=12,
        padding=20,
        width=740,
        border=ft.Border(
            left=ft.BorderSide(2, "#1E88E5"),
            right=ft.BorderSide(2, "#1E88E5"),
            top=ft.BorderSide(2, "#1E88E5"),
            bottom=ft.BorderSide(2, "#1E88E5"),
        ),
    )

    overlay_bg = ft.Container(
        content=ft.Column(
            [overlay_panel],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#88000000",
        expand=True,
        alignment=ft.Alignment(0, 0),
        on_click=close_viewer,
    )

    def display_doc(name: str, doc_type: str, image_path: str):
        overlay_title.value = f"{name} — {doc_type}"
        overlay_image.src = image_path
        page.overlay.clear()
        page.overlay.append(overlay_bg)
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
                        alignment=ft.Alignment(0, 0),
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
            bgcolor="#42A5F5",
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
                        color="#1565C0",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=image_path,
                            fit="contain",
                            border_radius=8,
                            height=300,
                            expand=True,
                        ),
                        border=ft.Border(
                            left=ft.BorderSide(1, "#E0E0E0"),
                            right=ft.BorderSide(1, "#E0E0E0"),
                            top=ft.BorderSide(1, "#E0E0E0"),
                            bottom=ft.BorderSide(1, "#E0E0E0"),
                        ),
                        border_radius=8,
                        bgcolor="#F5F5F5",
                        padding=8,
                        clip_behavior="hardEdge",
                    ),
                ],
                spacing=8,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=0,
        )

    # ==================================================
    # TAB 1: PROJECT TIMELINE
    # ==================================================
    def build_timeline_tab():
        def week_entry(label, desc):
            return ft.Column(
                [
                    ft.Text(label, weight=ft.FontWeight.BOLD, size=14),
                    ft.Text(f"- {desc}", size=13, color="#424242"),
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

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("MATLAB Achievement Hub", size=22, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text("Completed Courses :", size=14, color="#616161"),
                    ft.Text(
                        "Click Certificate or Report on any course card to view it.",
                        size=13,
                        color="#757575",
                    ),
                    courses_grid,
                ],
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=20,
        )

    # ==================================================
    # TAB 3: TECHNICAL BLOG  (with BlastX Equations)
    # ==================================================
    def build_blog_tab():
        VIDEO_WIDTH = 560
        VIDEO_HEIGHT = 315

        VIDEO_ASSET = "demo.mp4"
        video_box = ft.Container(width=VIDEO_WIDTH, height=VIDEO_HEIGHT, border_radius=10)

        def thumbnail_content():
            return ft.Stack(
                [
                    ft.Container(
                        bgcolor="#212121",
                        border_radius=10,
                        width=VIDEO_WIDTH,
                        height=VIDEO_HEIGHT,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Icon(
                                    ft.Icons.PLAY_CIRCLE_FILLED,
                                    size=72,
                                    color=ft.Colors.WHITE,
                                ),
                                ft.Text(
                                    "Click to watch the project video",
                                    size=13,
                                    color=ft.Colors.WHITE70,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8,
                        ),
                        alignment=ft.Alignment(0, 0),
                        width=VIDEO_WIDTH,
                        height=VIDEO_HEIGHT,
                    ),
                ]
            )

        def play_video(e):
            video_box.content = ftv.Video(
                playlist=[ftv.VideoMedia(VIDEO_ASSET)],
                autoplay=True,
                show_controls=True,
                fit=ft.BoxFit.CONTAIN,
                aspect_ratio=VIDEO_WIDTH / VIDEO_HEIGHT,
                fill_color=ft.Colors.BLACK,
                expand=True,
            )
            video_box.on_click = None
            video_box.ink = False
            open_btn.visible = False
            page.update()

        video_box.content = thumbnail_content()
        video_box.ink = True
        video_box.on_click = play_video
        video_box.tooltip = "Click to watch video"

        open_btn = ft.Container(
            content=ft.Text(
                "▶  Play Video",
                size=14,
                weight=ft.FontWeight.W_600,
                color="white",
                text_align=ft.TextAlign.CENTER,
            ),
            bgcolor="#1E88E5",
            border_radius=10,
            padding=ft.Padding(left=24, top=12, right=24, bottom=12),
            on_click=play_video,
            ink=True,
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Technical Blog", size=22, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text("Confidence in Concepts", size=18, weight=ft.FontWeight.BOLD, color="#1976D2"),
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
                    ft.Text("Topic 2: BlastX Optimization & Blasting Formulae", weight=ft.FontWeight.BOLD, size=14),
                    ft.Text(
                        "When managing explosive energetic boundaries and raw physical properties across mining, structural civil, "
                        "and metallurgical rock engineering sub-modules within the BlastX analytical engine, system metrics must "
                        "strictly correspond to formal technical and economic parameters:",
                        size=13,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Total_Blasting_Cost = \u2211 [ (Q\u2091 \u00d7 P\u2091) + (N_det \u00d7 P_det) ] + Overheads", size=15, weight=ft.FontWeight.BOLD, color="#1976D2"),
                                ft.Text("Where: Q\u2091 = Total explosive charge mass (kg),  P\u2091 = Explosive agent unit price ($/kg)\n"
                                        "       N_det = Quantity of delay detonators,  P_det = Unit price of initiation networks ($/unit)", size=12, color="#757575", italic=True),
                            ],
                            spacing=6,
                        ),
                        bgcolor="#E3F2FD",
                        border_radius=8,
                        padding=ft.Padding(left=20, top=12, right=20, bottom=12),
                    ),
                    ft.Container(height=4),
                    ft.Text(
                        "To maximize spatial powder distribution efficiency while protecting nearby geologic bounds from micro-crack damage, "
                        "the layout calculator evaluates the Powder Factor (PF):",
                        size=13,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("PF = Total Explosive Mass (kg) / V_rock (m\u00b3)", size=15, weight=ft.FontWeight.BOLD, color="#1976D2"),
                                ft.Text("Where: V_rock = Burden \u00d7 Spacing \u00d7 Bench Height", size=12, color="#757575", italic=True),
                            ],
                            spacing=6,
                        ),
                        bgcolor="#E3F2FD",
                        border_radius=8,
                        padding=ft.Padding(left=20, top=12, right=20, bottom=12),
                    ),
                    ft.Container(height=10),
                    ft.Text("Embedded Video on project contribution:", weight=ft.FontWeight.BOLD, size=14),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("🎬  Click the thumbnail or the button below to watch the video.", size=13, color="#424242", text_align=ft.TextAlign.CENTER),
                                video_box,
                                open_btn,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=12,
                        ),
                        bgcolor="#F5F5F5",
                        border_radius=12,
                        padding=20,
                        alignment=ft.Alignment(0, 0),
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
        # Clean helper function to make compliant bullet rows completely safe from attribute errors
        def make_bullet_row(text_value: str):
            return ft.Row(
                [
                    ft.Text(" \u2022 ", size=14, weight=ft.FontWeight.BOLD, color="#1976D2"),
                    ft.VerticalDivider(width=4),
                    ft.Text(text_value, size=13, expand=True, color="#424242"),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            )

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
                        "Team Collaboration on implementation of BlastX",
                        size=13,
                        italic=True,
                        color="#616161",
                    ),
                    ft.Container(height=8),
                    ft.Text("1. Commit History", size=16, weight=ft.FontWeight.BOLD, color="#1976D2"),
                    ft.Text(
                        "Verified log updates and source tracking metrics mapped directly back to the main branch repository Architecture:",
                        size=13,
                    ),
                    log_image_card("Commit History Log", "commit_history.png"),
                    ft.Container(height=8),
                    ft.Text("2. Pull Request Logs", size=16, weight=ft.FontWeight.BOLD, color="#1976D2"),
                    ft.Text(
                        "Detailed features proposed, structured code reviews performed, and team merges completed successfully:",
                        size=13,
                    ),
                    log_image_card("Pull Request Logs", "pr_logs.png"),
                    ft.Container(height=8),
                    ft.Text("3. BlastX Impact Summary", size=16, weight=ft.FontWeight.BOLD, color="#1976D2"),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Engineering Problem Solved:",
                                    size=14,
                                    weight=ft.FontWeight.BOLD,
                                    color="#1565C0",
                                ),
                                ft.Text(
                                    "In the mining excavation and civil blast estimation sub-modules of BlastX, concurrent calculation data arrays "
                                    "were triggering severe race conditions and runtime deadlocks whenever multi-disciplinary teams "
                                    "attempted to compute rock-mass powder factors or update spatial blast geometries simultaneously.",
                                    size=13,
                                ),
                                ft.Container(height=6),
                                ft.Text(
                                    "My Specific Contribution:",
                                    size=14,
                                    weight=ft.FontWeight.BOLD,
                                    color="#1565C0",
                                ),
                                ft.Text(
                                    "I structured an isolated asynchronous data flow by splitting out the computational logic blocks "
                                    "and introducing a non-blocking execution cycle. By redesigning task queues, I eliminated cross-thread bottlenecks "
                                    "and introduced transactional isolation states to secure spatial coordinate lookups.",
                                    size=13,
                                ),
                                ft.Container(height=6),
                                ft.Text(
                                    "Measurable Impact Score:",
                                    size=14,
                                    weight=ft.FontWeight.BOLD,
                                    color="#1565C0",
                                ),
                                make_bullet_row("Processing Efficiency: Reduced execution overhead for intensive powder factor and volumetric calculations by 34%."),
                                make_bullet_row("System Concurrency: Eliminated 100% of application thread deadlocks during multi-user simulations."),
                                make_bullet_row("Data Integrity: Ensured that structural fragmentation metrics align strictly with factual geo-mechanical constraints."),
                            ],
                            spacing=4,
                        ),
                        bgcolor="#E3F2FD",
                        border_radius=8,
                        padding=ft.Padding(left=16, top=14, right=16, bottom=14),
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
            btn.bgcolor = "#1E88E5" if i == index else "#EEEEEE"
            btn.content.color = "white" if i == index else "#424242"
        content_area.content = tab_builders[index]()
        page.update()

    for i, name in enumerate(tab_names):
        btn = ft.Container(
            content=ft.Text(name, size=13, weight=ft.FontWeight.W_500, color="#424242"),
            bgcolor="#EEEEEE",
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
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("My Portfolio", size=28, weight=ft.FontWeight.BOLD, color="white"),
                        ft.CircleAvatar(
                            background_image_src="profile pic.jpeg",
                            radius=22,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                ),
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
        bgcolor="#1E88E5",
        padding=20,
        border_radius=15,
        alignment=ft.Alignment(0, 0),
        expand=True,
    )

    switch_tab(1)  

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    header_panel,
                    ft.Divider(height=1, color="#E0E0E0"),
                    tab_bar,
                    ft.Divider(height=1, color="#E0E0E0"),
                    content_area,
                ],
                spacing=12,
                expand=True,
            ),
            padding=20,
            expand=True,
        )
    )


ft.run(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)