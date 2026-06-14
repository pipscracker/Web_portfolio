import flet as ft

def main(page: ft.Page):
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
                        src="https://drive.google.com/uc?export=view&id=1ka94V7GcKnO5vnbRU7cKqKa9nxDz9oh_", 
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

    # DYNAMIC DOCUMENT VIEWER COMPONENT PLACEHOLDER (No ft.Html used here)
    doc_viewer_title = ft.Text("Document Showcase", size=18, weight="bold")
    doc_viewer_desc = ft.Text("Click on any course certificate or report button above to preview the document down here.", color="grey600")
    
    # Adding src="" solves the local VS Code positional argument crash
    doc_viewer_image = ft.Image(src="", visible=False, fit="contain", height=450)

    doc_viewer_zone = ft.Container(
        content=ft.Column([
            doc_viewer_title,
            doc_viewer_desc,
            doc_viewer_image
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
        margin=25
    )

    # REUSABLE MATLAB CARD COMPONENT WRAPPER
    def course_card(name, cert_url, report_url):
        
        def display_doc(e, doc_type, url):
            try:
                # Extracts the unique ID between /d/ and /view
                if "/d/" in url:
                    file_id = url.split("/d/")[1].split("/")[0]
                elif "id=" in url:
                    file_id = url.split("id=")[1].split("&")[0]
                else:
                    file_id = url
                
                # FORCE TRUE DIRECT RAW IMAGE STREAMING
                direct_img_url = f"https://drive.google.com/uc?export=view&id={file_id}"
            except Exception:
                direct_img_url = url
            
            # Print the converted link to your terminal to make sure it's formatting right
            print(f"Streaming direct image URL: {direct_img_url}")
            
            doc_viewer_title.value = f"Viewing: {name} - {doc_type}"
            doc_viewer_desc.value = "Displaying verification document inline below:"
            
            # Update source cleanly and force visibility
            doc_viewer_image.src = direct_img_url
            doc_viewer_image.visible = True
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
                ft.Text("Total_Cost = Σ (Q_i × P_i) + Overheads", size=16, weight="bold", color="blue900"),
                ft.Text("Where: Q_i = Quantity of material i, P_i = Unit Price of material i.", size=12, italic=True)
            ], horizontal_alignment="center"),
            padding=15,
            bgcolor="grey100",
            border_radius=8
        ),
        
        ft.Text("Embedded Video Explanation:", weight="w500"),
        
        ft.Row([
            ft.Container(
                content=ft.Row([
                    ft.Icon("play_circle_fill", color="white", size=20),
                    ft.Text("Click to watch the video", color="white", weight="bold", size=14),
                ], alignment="center", spacing=10), 
                bgcolor="red600",
                padding=12,
                border_radius=8,
                width=260,
                height=48, 
                on_click=lambda e: page.launch_url("https://www.youtube.com") 
            )
        ], alignment="start")
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
                ft.Text("Problem Statement & Technical Challenge:", weight="bold", size=14, color="blue900"),
                ft.Text("During the integration phase of the multi-disciplinary engineering estimation engine, major cross-platform compilation deadlocks and data-sync crashes occurred. Mixing core simulation math scripts led to critical runtime environment parsing errors. Additionally, asynchronous calculations within the Civil and Mining sub-modules caused data leakages and UI synchronization stutters, leaving background estimation processes incomplete.", size=13),
                ft.Container(height=5),
                ft.Text("Implemented Solution & Engineering Impact:", weight="bold", size=14, color="blue900"),
                ft.Text("To resolve this, I isolated the cross-language dependencies by tracking down and debugging mixed TypeScript/JavaScript syntax errors across the core processing modules. I stabilized the database and calculation layers by deploying robust Firebase Configuration APIs to securely track engineering data metrics. Finally, I engineered an optimized UI state interval controller ('Countdown Interval Routine') that kept complex metallurgical estimation threads running smoothly in the background, eliminating calculation lags and securing fluid performance across all engineering sub-modules.", size=13),
            ], spacing=8),
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
            if i == index:
                btn.bgcolor = "blue600"
                btn.color = "white"
            else:
                btn.bgcolor = "grey300"
                btn.color = "blue600"
        page.update()

    nav_buttons = [
        ft.Container(content=ft.Text("Project Timeline", color="white"), bgcolor="blue600", padding=10, border_radius=5, on_click=lambda e: show_tab(0)),
        ft.Container(content=ft.Text("MATLAB Hub", color="blue600"), bgcolor="grey300", padding=10, border_radius=5, on_click=lambda e: show_tab(1)),
        ft.Container(content=ft.Text("Technical Blog", color="blue600"), bgcolor="grey300", padding=10, border_radius=5, on_click=lambda e: show_tab(2)),
        ft.Container(content=ft.Text("GitHub Evidence", color="blue600"), bgcolor="grey300", padding=10, border_radius=5, on_click=lambda e: show_tab(3)),
    ]

    nav = ft.Row(nav_buttons, spacing=10)
    page.add(header, nav, ft.Divider(), timeline, matlab, blog, github_evidence)

if __name__ == "__main__":
    ft.app(target=main)