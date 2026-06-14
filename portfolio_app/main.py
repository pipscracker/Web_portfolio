import flet as ft

def main(page: ft.Page):
    # Core window configuration matching your style preference
    page.title = "My Portfolio"
    page.theme_mode = "light"  
    page.padding = 20
    page.scroll = "auto"       

    # 1. HEADER HERO PANEL 
    header = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Image(
                        src="https://drive.google.com/file/d/1ka94V7GcKnO5vnbRU7cKqKa9nxDz9oh_/view?usp=drivesdk", 
                        width=120, 
                        height=120, 
                        fit="cover"  
                    ),
                    width=120, height=120, border_radius=60,
                ),
                ft.Column([
                    ft.Text("My Portfolio", size=36, weight="bold", color="white"),
                    ft.Text("Ireneus Shilunga | Electronics and Computer Engineering", size=16, color="white70"),
                    ft.Text("Student No: 225030969", size=14, color="white60"),
                ], alignment="center", spacing=5),
            ], spacing=20, alignment="start", vertical_alignment="center"),
            ft.Divider(color="white24"),
            ft.Row([ft.Text("© 2026 UNAM", size=12, color="white60")],
                alignment="end"),
        ]),
        padding=30, border_radius=15, bgcolor="blue600",
    )

    # 2. TAB CONTENT 1: PROJECT TIMELINE
    timeline = ft.Column([
        ft.Text("Project Timeline", size=24, weight="bold"),
        ft.Divider(),
        ft.Text("Week 1-3", weight="bold"),
        ft.Text("- Initial repository structure setup and architectural planning."),
        ft.Text("Week 4-5", weight= "bold"),
        ft.Text("- Developed core calculation algorithms and engineering parsing modules."),
        ft.Text("Week 6-7", weight="bold"),
        ft.Text("- Implemented data validation logic and ran integration unit tests."),
        ft.Text("Week 8-9", weight="bold"),
        ft.Text("- UI layout mockups, debugging component scripts, and resolving data validation issues."),
    ], spacing=8, visible=True)

    # DYNAMIC DOCUMENT VIEWER COMPONENT PLACEHOLDER
    doc_viewer_title = ft.Text("Document Showcase", size=18, weight="bold")
    doc_viewer_desc = ft.Text("Click on any course certificate or report button above to preview the document down here.", color="grey600")
    
    doc_viewer_frame = ft.Container(
        visible=False, 
        height=600, 
        border=ft.Border(
            top=ft.BorderSide(1, "grey300"),
            bottom=ft.BorderSide(1, "grey300"),
            left=ft.BorderSide(1, "grey300"),
            right=ft.BorderSide(1, "grey300")
        ), 
        border_radius=8
    )
    # Replaced ElevatedButton with Button to resolve deprecation crashes
    doc_viewer_button = ft.Button("Open Document in New Tab", icon="open_in_new", visible=False)

    doc_viewer_zone = ft.Container(
        content=ft.Column([
            doc_viewer_title,
            doc_viewer_desc,
            doc_viewer_button,
            doc_viewer_frame
        ], spacing=15),
        padding=20,
        bgcolor="grey50",
        border_radius=12,
        border=ft.Border(
            top=ft.BorderSide(1, "grey200"),
            bottom=ft.BorderSide(1, "grey200"),
            left=ft.BorderSide(1, "grey200"),
            right=ft.BorderSide(1, "grey200")
        ),
        margin=25 # Safe integer uniform margin setup
    )

    # REUSABLE MATLAB CARD COMPONENT WRAPPER
    def course_card(name, cert_url, report_url):
        def display_doc(e, doc_type, url):
            # Convert the standard view link into a direct image export link
            # Works perfectly for images/PDFs stored on Google Drive
            embed_url = url.replace("/view?usp=drive_link", "/preview").replace("/view?usp=drivesdk", "/preview")

            doc_viewer_title.value = f"Viewing: {name} - {doc_type}"
            doc_viewer_desc.value = "If the embedded document preview doesn't load automatically due to security restrictions, use the action button below to open it directly."

            doc_viewer_button.url = url
            doc_viewer_button.visible = True

            # Use ft.Image pointing to the preview URL
            doc_viewer_frame.content = ft.Image(
                src=embed_url,
                fit="contain",
                expand=True
            )
            doc_viewer_frame.visible = True
            page.update()

        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Text(name, weight="bold", size=12, text_align="center", color="white"),
                    height=35
                ),
                ft.Row([
                    ft.Container(
                        content=ft.Text("Certificate", size=11, weight="w500", color="black"),
                        bgcolor="white", border_radius=4, padding=6,
                        on_click=lambda e: display_doc(e, "Certificate", cert_url)
                    ),
                    ft.Container(
                        content=ft.Text("Report", size=11, weight="w500", color="black"),
                        bgcolor="white", border_radius=4, padding=6,
                        on_click=lambda e: display_doc(e, "Report", report_url)
                    ),
                ], spacing=8, alignment="center"),
            ], spacing=5, alignment="center", horizontal_alignment="center"),
            padding=10, border_radius=10, bgcolor="blue400",
            width=210, height=105,
        )

    # 3. TAB CONTENT 2: MATLAB ACHIEVEMENT HUB
    matlab = ft.Column([
        ft.Text("MATLAB Achievement Hub", size=24, weight="bold"),
        ft.Divider(),
        ft.Text("Completed Courses :", size=16),
        
        ft.Row([
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
                "Calculations with Vectors and Matrices",
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
                "Wireless Communications Onramp",
                "https://drive.google.com/file/d/1Y0DE6wGDozeZPm5sJDg6_T5MRdjMPgS5/view?usp=drive_link",
                "https://drive.google.com/file/d/1BvdHNeaCp24rYq42Vs2GHPSLY2uOEyAk/view?usp=drive_link"
            ),
            course_card(
                "Machine Learning Onramp",
                "https://drive.google.com/file/d/1JobPmk9J57UFfKxRrQ0nc9jEjkhszGOG/view?usp=drive_link",
                "https://drive.google.com/file/d/1vI24rs8Wi2C4waV16Tnxwjcp1MgX2TZD/view?usp=drive_link"
            ),
        ], wrap=True, spacing=15, run_spacing=15),
        
        doc_viewer_zone
    ], spacing=15, visible=False)

    # 4. TAB CONTENT 3: TECHNICAL BLOG
    blog = ft.Column([
        ft.Text("Technical Blog", size=24, weight="bold"),
        ft.Divider(),
        ft.Text("Confidence in Concepts", size=18, weight="bold", color="blue600"),
        
        ft.Text("Topic 1: How does a database work?", weight="bold"),
        ft.Text("At its core, a database is an optimized system built to store, manage, and retrieve data seamlessly. "
                "It operates across three fundamental layers: the Storage Engine, which structures physical files on "
                "disk using B-Trees or indexes for rapid access; the Query Engine, which parses and optimizes execution paths; "
                "and the Transaction Manager, which guarantees data safety via ACID compliance.",
            size=14),
        
        ft.Divider(),
        
        ft.Text("Topic 2: Material Cost Optimisation Formula", weight="bold"),
        ft.Text("When managing physical design variables across mining and civil engineering subsystems, calculations must align with true financial bounds:"),
        
        ft.Container(
            content=ft.Column([
                ft.Image(src="cost_formula.png", error_content=ft.Text("Total_Cost = Σ (Q_i × P_i) + Overheads", size=16, weight="bold", color="blue900")),
                ft.Text("Where: Q_i = Quantity of material i, P_i = Unit Price of material i.", size=12, italic=True)
            ], horizontal_alignment="center"),
            padding=15,
            bgcolor="grey100",
            border_radius=8
        ),
        
        ft.Text("Embedded Video Explanation:", weight="w500"),
        ft.Container(
            content=ft.Row([
                ft.Icon("play_circle_fill", color="red", size=40),
                ft.Text("Click to watch concept implementation video walkthrough", color="blue", size=14, weight="bold")
            ], alignment="center"),
            padding=15,
            border=ft.Border(
                top=ft.BorderSide(1, "grey400"),
                bottom=ft.BorderSide(1, "grey400"),
                left=ft.BorderSide(1, "grey400"),
                right=ft.BorderSide(1, "grey400")
            ),
            border_radius=10,
            on_click=lambda e: page.launch_url("https://www.youtube.com") 
        ),
    ], spacing=12, visible=False)

    # REUSABLE GIT DESIGN COMPONENT WRAPPER
    def git_evidence_card(card_title, action_url):
        return ft.Container(
            content=ft.Column([
                ft.Container(height=15),
                ft.Text(card_title, weight="bold", size=14,
                        text_align="center", color="white"),
                ft.Container(height=10),
                ft.Row([
                    ft.Container(
                        content=ft.Text("", spans=[ft.TextSpan(text="View Logs", url=action_url, style=ft.TextStyle(color="blue800", weight="bold"))]),
                        bgcolor="white", border_radius=5, padding=10,
                    )
                ], alignment="center"),
            ], spacing=5, horizontal_alignment="center"),
            padding=15, border_radius=15, bgcolor="blue200",
            width=270, height=150,
        )

    # 5. TAB CONTENT 4: GITHUB EVIDENCE & DOCUMENTATION
    github_evidence = ft.Column([
        ft.Text("GitHub Evidence & Documentation", size=24, weight="bold"),
        ft.Divider(),
        ft.Text("Large-Scale Team Collaboration Verification (20 Members Group)", size=14, italic=True, color="grey700"),
        
        ft.Column([
            ft.Text("1. Commit History", size=18, weight="bold", color="blue600"),
            ft.Text("Verified log updates and source tracking metrics mapped directly back to the main branch repository Architecture:"),
            ft.Row([
                git_evidence_card(
                    card_title="Commit History Log",
                    action_url="https://drive.google.com/file/d/1x9zN-X0S9gIqYFb7wFcu4crPWlPoH7xI/view?usp=drive_link"
                )
            ]),
        ], spacing=8),
        
        ft.Container(height=10),
        
        ft.Column([
            ft.Text("2. Pull Request Logs", size=18, weight="bold", color="blue600"),
            ft.Text("Detailed features proposed, structured code reviews performed, and team merges completed successfully:"),
            ft.Row([
                git_evidence_card(
                    card_title="Pull Request Logs",
                    action_url="https://drive.google.com/file/d/1U45fAdmJDwL1DJ5uTL7zMvbNO0QeF0oJ/view?usp=drive_link"
                )
            ]),
        ], spacing=8),
        
        ft.Container(height=10),
        
        ft.Text("3. Impact Summary", size=18, weight="bold", color="blue600"),
        ft.Container(
            content=ft.Column([
                ft.Text("My specific script modifications and hardware interface abstraction logic directly resolved critical processing deadlocks within the application's Metallurgical, Mining, and Civil engineering estimation sub-modules.", weight="bold"),
                ft.Text("By cleaning up async calculation steps, processing overhead for large material cost computations was minimized, ensuring accurate performance calculations across multi-disciplinary teams."),
            ]),
            padding=15,
            bgcolor="blue50",
            border_radius=8
        )
    ], spacing=12, visible=False)

    # TAB NAVIGATION CONTROLLER INTERACTION
    def show_tab(index):
        timeline.visible = index == 0
        matlab.visible = index == 1
        blog.visible = index == 2
        github_evidence.visible = index == 3 
        
        for i, btn in enumerate(nav_buttons):
            btn.style = ft.ButtonStyle(bgcolor="blue600" if i == index else "grey300")
            btn.color = "white" if i == index else "blue600"
        page.update()

    # NAVIGATION DECK CONTROL BUTTONS (Updated to ft.Button)
    nav_buttons = [
        ft.Button("Project Timeline", on_click=lambda e: show_tab(0),
            style=ft.ButtonStyle(bgcolor="blue600"), color="white"),
        ft.Button("MATLAB Hub", on_click=lambda e: show_tab(1),
            style=ft.ButtonStyle(bgcolor="grey300"), color="blue600"),
        ft.Button("Technical Blog", on_click=lambda e: show_tab(2),
            style=ft.ButtonStyle(bgcolor="grey300"), color="blue600"),
        ft.Button("GitHub Evidence", on_click=lambda e: show_tab(3),
            style=ft.ButtonStyle(bgcolor="grey300"), color="blue600"),
    ]

    nav = ft.Row(nav_buttons, spacing=10)
    
    page.add(header, nav, ft.Divider(), timeline, matlab, blog, github_evidence)

# Replaced deprecated ft.app with new runtime executor matching your exact stack requirements
if __name__ == "__main__":
    ft.run(main)