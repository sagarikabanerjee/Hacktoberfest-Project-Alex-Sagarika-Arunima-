import customtkinter as ctk
from tkinter import filedialog, messagebox
import json
import os

REPORTS_FILE = "filed_reports.json"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class FiledReportsApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Filed Incident Reports")
        self.root.geometry("1500x900")

        self.reports = []
        self.filtered_reports = []
        self.selected_report = None

        self.build_ui()
        self.load_reports()

    def build_ui(self):

        # ===== HEADER =====

        header = ctk.CTkFrame(
            self.root,
            corner_radius=15,
            height=80
        )

        header.pack(
            fill="x",
            padx=15,
            pady=(15, 10)
        )

        ctk.CTkLabel(
            header,
            text="📋 Filed Incident Reports",
            font=("Segoe UI", 30, "bold")
        ).pack(
            side="left",
            padx=20,
            pady=20
        )

        # ===== SEARCH BAR =====

        search_frame = ctk.CTkFrame(
            self.root,
            corner_radius=15
        )

        search_frame.pack(
            fill="x",
            padx=15,
            pady=(0, 10)
        )

        self.search_var = ctk.StringVar()

        self.search_var.trace_add(
            "write",
            lambda *args: self.refresh_list()
        )

        self.search_box = ctk.CTkEntry(
            search_frame,
            placeholder_text="🔍 Search reports...",
            textvariable=self.search_var,
            width=400,
            height=40
        )

        self.search_box.pack(
            side="left",
            padx=15,
            pady=15
        )

        ctk.CTkButton(
            search_frame,
            text="🔄 Reload",
            width=120,
            command=self.load_reports
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            search_frame,
            text="📤 Export Report",
            width=140,
            command=self.export_report
        ).pack(
            side="left",
            padx=5
        )

        # ===== MAIN AREA =====

        main = ctk.CTkFrame(
            self.root,
            corner_radius=15
        )

        main.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # ==========================
        # LEFT SIDEBAR
        # ==========================

        sidebar = ctk.CTkFrame(
            main,
            width=350,
            corner_radius=15
        )

        sidebar.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            sidebar,
            text="Approved Reports",
            font=("Segoe UI", 20, "bold")
        ).pack(
            pady=(15, 10)
        )

        self.report_list = ctk.CTkTextbox(
            sidebar,
            width=320
        )

        self.report_list.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.report_list.bind(
            "<ButtonRelease-1>",
            self.on_report_click
        )

        # ==========================
        # RIGHT PANEL
        # ==========================

        self.right_panel = ctk.CTkFrame(
            main,
            corner_radius=15
        )

        self.right_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.report_title = ctk.CTkLabel(
            self.right_panel,
            text="Select a report",
            font=("Segoe UI", 26, "bold")
        )

        self.report_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.status_badge = ctk.CTkLabel(
            self.right_panel,
            text="No Report Selected",
            fg_color="#555555",
            corner_radius=20,
            padx=12,
            pady=5
        )

        self.status_badge.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.details_frame = ctk.CTkScrollableFrame(
            self.right_panel
        )

        self.details_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.stats_label = ctk.CTkLabel(
            self.root,
            text="Total Reports: 0"
        )

        self.stats_label.pack(
            pady=(0, 10)
        )

    # ==================================
    # DATA LOADING
    # ==================================

    def load_reports(self):

        if not os.path.exists(REPORTS_FILE):

            self.reports = []
            self.refresh_list()
            return

        try:

            with open(
                REPORTS_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                self.reports = json.load(f)

            self.refresh_list()

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not load reports:\n{e}"
            )

    def refresh_list(self):

        self.report_list.delete(
            "1.0",
            "end"
        )

        self.filtered_reports = []

        search = self.search_var.get().lower()

        for report in self.reports:

            name = report.get(
                "person_involved",
                {}
            ).get(
                "full_name",
                "Unknown"
            )

            date = report.get(
                "date_of_report",
                "No Date"
            )

            missing = len(
                report.get(
                    "missing_info",
                    []
                )
            )

            badge = (
                f"⚠ {missing} missing"
                if missing
                else "✓ complete"
            )

            label = (
                f"{name}\n"
                f"{date} | {badge}\n\n"
            )

            if search in label.lower():

                self.filtered_reports.append(
                    report
                )

                self.report_list.insert(
                    "end",
                    label
                )

        self.stats_label.configure(
            text=f"Total Reports: {len(self.filtered_reports)}"
        )

    # ==================================
    # REPORT SELECTION
    # ==================================

    def on_report_click(self, event):

        try:

            index = self.report_list.index(
                f"@{event.x},{event.y}"
            )

            line = int(
                index.split(".")[0]
            )

            report_number = (line - 1) // 3

            if (
                0 <= report_number <
                len(self.filtered_reports)
            ):

                self.selected_report = (
                    self.filtered_reports[
                        report_number
                    ]
                )

                self.show_report(
                    self.selected_report
                )

        except:
            pass

    # ==================================
    # CARD CREATION
    # ==================================

    def create_card(
        self,
        title,
        info
    ):

        card = ctk.CTkFrame(
            self.details_frame,
            corner_radius=12
        )

        card.pack(
            fill="x",
            padx=10,
            pady=8
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 10)
        )

        for key, value in info.items():

            row = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=15,
                pady=3
            )

            ctk.CTkLabel(
                row,
                text=key.replace(
                    "_",
                    " "
                ).title(),
                width=200,
                anchor="w",
                font=(
                    "Segoe UI",
                    12,
                    "bold"
                )
            ).pack(
                side="left"
            )

            color = "white"

            if value in (
                None,
                "",
                "None"
            ):

                value = (
                    "Missing Information"
                )

                color = "#ffd966"

            ctk.CTkLabel(
                row,
                text=str(value),
                text_color=color,
                anchor="w"
            ).pack(
                side="left"
            )

    # ==================================
    # SHOW REPORT
    # ==================================

    def show_report(self, report):

        for widget in (
            self.details_frame
            .winfo_children()
        ):
            widget.destroy()

        person = report.get(
            "person_involved",
            {}
        )

        incident = report.get(
            "incident",
            {}
        )

        injuries = report.get(
            "injuries",
            {}
        )

        witnesses = report.get(
            "witnesses",
            {}
        )

        missing = report.get(
            "missing_info",
            []
        )

        self.report_title.configure(
            text=person.get(
                "full_name",
                "Unknown Person"
            )
        )

        if missing:

            self.status_badge.configure(
                text=f"⚠ {len(missing)} Missing Fields",
                fg_color="#7a5b00"
            )

        else:

            self.status_badge.configure(
                text="✓ Complete Report",
                fg_color="#1f6f43"
            )

        self.create_card(
            "👤 Person Information",
            person
        )

        self.create_card(
            "📍 Incident Details",
            incident
        )

        self.create_card(
            "🩹 Injuries",
            injuries
        )

        self.create_card(
            "👥 Witnesses",
            witnesses
        )

        if missing:

            warning = ctk.CTkFrame(
                self.details_frame,
                fg_color="#453000",
                corner_radius=12
            )

            warning.pack(
                fill="x",
                padx=10,
                pady=8
            )

            ctk.CTkLabel(
                warning,
                text="⚠ Missing Information",
                font=(
                    "Segoe UI",
                    18,
                    "bold"
                )
            ).pack(
                anchor="w",
                padx=15,
                pady=10
            )

            for item in missing:

                ctk.CTkLabel(
                    warning,
                    text="• " + str(item),
                    text_color="#ffd966"
                ).pack(
                    anchor="w",
                    padx=20,
                    pady=2
                )

    # ==================================
    # EXPORT
    # ==================================

    def export_report(self):

        if not self.selected_report:

            messagebox.showwarning(
                "Warning",
                "Select a report first."
            )

            return

        filename = (
            filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[
                    (
                        "JSON Files",
                        "*.json"
                    )
                ]
            )
        )

        if not filename:
            return

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.selected_report,
                f,
                indent=4
            )

        messagebox.showinfo(
            "Success",
            "Report exported successfully."
        )


if __name__ == "__main__":

    root = ctk.CTk()

    app = FiledReportsApp(root)

    root.mainloop()