import flet as ft


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
                        border=ft.Border(left=ft.BorderSide(1,"#E0E0E0"),right=ft.BorderSide(1,"#E0E0E0"),top=ft.BorderSide(1,"#E0E0E0"),bottom=ft.BorderSide(1,"#E0E0E0")),
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
    
    # --------------------------------------------------
    # VIDEO PLAYER OVERLAY — Web-Safe Redirect Interface
    # --------------------------------------------------
    def open_video_overlay(e=None):
        def close_video(e=None):
            page.overlay.clear()
            page.update()

        # FIXED: Declare the action function using modern async await syntax
        async def launch_player(e):
            video_filename = "demo.mp4" # Replace with your actual filename if needed
            target_player_url = f"/video_player.html?v={video_filename}"
            # FIXED: Avoids runtime warnings by calling the updated URL launcher correctly
            await page.open_url_async(target_player_url)

        video_view = ft.Container(
            content=ft.Column(
                [
                    ft.Icon("play_circle_filled", size=64, color="#1E88E5"),
                    ft.Text(
                        "Project Video Demonstration",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#1565C0",
                    ),
                    ft.Text(
                        "Click the button below to launch the dedicated interactive HTML5 video player tab.",
                        size=13,
                        text_align=ft.TextAlign.CENTER,
                        color="#424242",
                    ),
                    ft.Container(height=8),
                    ft.ElevatedButton(
                        "Launch Video Player  ↗",
                        on_click=launch_player,  # FIXED: Now correctly references the function above
                        bgcolor="#1E88E5",
                        color="white",
                        style=ft.ButtonStyle(
                            padding=ft.Padding.all(14),
                        )
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="#F5F5F5",
            border_radius=8,
            padding=24,
            expand=True,
            alignment=ft.Alignment(0, 0),
        )

        video_panel = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Project Video", size=15, weight=ft.FontWeight.BOLD, color="#1565C0"),
                            ft.Container(expand=True),
                            ft.TextButton("✕  Close", on_click=close_video),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=video_view,
                        height=420,
                        border_radius=8,
                        clip_behavior="hardEdge",
                    ),
                ],
                spacing=8,
                tight=True,
            ),
            bgcolor="white",
            border_radius=12,
            padding=20,
            width=860,
            border=ft.Border(
                left=ft.BorderSide(2, "#1E88E5"),
                right=ft.BorderSide(2, "#1E88E5"),
                top=ft.BorderSide(2, "#1E88E5"),
                bottom=ft.BorderSide(2, "#1E88E5"),
            ),
        )

        video_bg = ft.Container(
            content=ft.Column(
                [video_panel],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#88000000",
            expand=True,
            alignment=ft.Alignment(0, 0),
            on_click=close_video,
        )

        page.overlay.clear()
        page.overlay.append(video_bg)
        page.update()

        # FIXED: Designed a highly professional native UI card to substitute the breaking WebView control
        video_view = ft.Container(
            content=ft.Column(
                [
                    ft.Icon("play_circle_filled", size=64, color="#1E88E5"),
                    ft.Text(
                        "Project Video Demonstration",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#1565C0",
                    ),
                    ft.Text(
                        "Click the button below to launch the dedicated interactive HTML5 video player tab.",
                        size=13,
                        text_align=ft.TextAlign.CENTER,
                        color="#424242",
                    ),
                    ft.ElevatedButton(
                        "Launch Video Player  ↗",
                        on_click=launch_player,
                        bgcolor="#1E88E5",
                        color="white",
                        style=ft.ButtonStyle(
                            padding=ft.Padding.all(14),  # <-- Changed to capital P
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="#F5F5F5",
            border_radius=8,
            padding=24,
            expand=True,
            alignment=ft.Alignment(0, 0),
        )

        video_panel = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Project Video", size=15, weight=ft.FontWeight.BOLD, color="#1565C0"),
                            ft.Container(expand=True),
                            ft.TextButton("✕  Close", on_click=close_video),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=video_view,
                        height=420,
                        border_radius=8,
                        clip_behavior="hardEdge",
                    ),
                ],
                spacing=8,
                tight=True,
            ),
            bgcolor="white",
            border_radius=12,
            padding=20,
            width=860,
            border=ft.Border(
                left=ft.BorderSide(2, "#1E88E5"),
                right=ft.BorderSide(2, "#1E88E5"),
                top=ft.BorderSide(2, "#1E88E5"),
                bottom=ft.BorderSide(2, "#1E88E5"),
            ),
        )

        video_bg = ft.Container(
            content=ft.Column(
                [video_panel],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#88000000",
            expand=True,
            alignment=ft.Alignment(0, 0),
            on_click=close_video,
        )

        page.overlay.clear()
        page.overlay.append(video_bg)
        page.update()

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
                        color="#1976D2",
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
                                    color="#1976D2",
                                ),
                                ft.Text(
                                    "Where: Qᵢ = Quantity of material i,  Pᵢ = Unit Price of material i",
                                    size=12,
                                    color="#757575",
                                    italic=True,
                                ),
                            ],
                            spacing=4,
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
                                ft.Text(
                                    "🎬  Click below to watch the project contribution video.",
                                    size=13,
                                    color="#424242",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "▶  Open Video Player",
                                        size=14,
                                        weight=ft.FontWeight.W_600,
                                        color="white",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    bgcolor="#1E88E5",
                                    border_radius=10,
                                    padding=ft.Padding(left=24, top=12, right=24, bottom=12),
                                    on_click=open_video_overlay,
                                    ink=True,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=12,
                        ),
                        bgcolor="#F5F5F5",
                        border_radius=12,
                        height=180,
                        alignment=ft.Alignment(0, 0),
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
                    ft.Text("3. Impact Summary", size=16, weight=ft.FontWeight.BOLD, color="#1976D2"),
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
        bgcolor="#1E88E5",
        padding=20,
        border_radius=15,
        alignment=ft.Alignment(0, 0),
        expand=True,
    )

    switch_tab(1)  # default to MATLAB Hub

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