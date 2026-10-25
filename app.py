import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os

REPORTS_FILE = "filed_reports.json"


class FiledReportsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Filed Incident Reports")
        self.root.geometry("1000x700")

        self.reports = []

        self.build_ui()
        self.load_reports()

    def build_ui(self):

        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(top_frame, text="Search Name:").pack(side="left")

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.refresh_list())

        ttk.Entry(
            top_frame,
            textvariable=self.search_var,
            width=40
        ).pack(side="left", padx=5)

        ttk.Button(
            top_frame,
            text="Reload",
            command=self.load_reports
        ).pack(side="left", padx=5)

        ttk.Button(
            top_frame,
            text="Export Selected",
            command=self.export_report
        ).pack(side="left", padx=5)

        main = ttk.Frame(self.root)
        main.pack(fill="both", expand=True)

        self.report_list = tk.Listbox(main, width=40)
        self.report_list.pack(side="left", fill="y", padx=10, pady=10)

        self.report_list.bind(
            "<<ListboxSelect>>",
            self.show_report
        )

        self.details = tk.Text(
            main,
            wrap="word",
            font=("Consolas", 10)
        )
        self.details.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.details.tag_configure(
            "missing",
            background="yellow"
        )

    def load_reports(self):

        if not os.path.exists(REPORTS_FILE):
            self.reports = []
            self.refresh_list()
            return

        try:
            with open(REPORTS_FILE, "r", encoding="utf-8") as f:
                self.reports = json.load(f)

            self.refresh_list()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Could not load reports:\n{e}"
            )

    def refresh_list(self):

        self.report_list.delete(0, tk.END)

        search = self.search_var.get().lower()

        for report in self.reports:

            name = (
                report
                .get("person_involved", {})
                .get("full_name")
            )

            date = report.get("date_of_report")

            label = f"{name or 'Unknown'} | {date or 'No Date'}"

            if search in label.lower():
                self.report_list.insert(
                    tk.END,
                    label
                )

    def get_filtered_reports(self):

        search = self.search_var.get().lower()

        result = []

        for report in self.reports:

            label = (
                f"{report.get('person_involved', {}).get('full_name') or 'Unknown'} "
                f"{report.get('date_of_report') or ''}"
            )

            if search in label.lower():
                result.append(report)

        return result

    def show_report(self, event=None):

        selection = self.report_list.curselection()

        if not selection:
            return

        reports = self.get_filtered_reports()

        report = reports[selection[0]]

        self.details.delete("1.0", tk.END)

        lines = []

        for section, value in report.items():

            if isinstance(value, dict):

                lines.append(f"\n[{section}]")

                for k, v in value.items():
                    lines.append(
                        f"{k}: {v}"
                    )

            else:
                lines.append(
                    f"{section}: {value}"
                )

        text = "\n".join(lines)

        self.details.insert(
            tk.END,
            text
        )

        missing = set(
            report.get("missing_info", [])
        )

        for field in missing:

            idx = self.details.search(
                field,
                "1.0",
                tk.END
            )

            while idx:
                end = f"{idx}+{len(field)}c"

                self.details.tag_add(
                    "missing",
                    idx,
                    end
                )

                idx = self.details.search(
                    field,
                    end,
                    tk.END
                )

    def export_report(self):

        selection = self.report_list.curselection()

        if not selection:
            messagebox.showwarning(
                "Warning",
                "Select a report first."
            )
            return

        report = self.get_filtered_reports()[
            selection[0]
        ]

        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON", "*.json")]
        )

        if not filename:
            return

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                report,
                f,
                indent=2
            )

        messagebox.showinfo(
            "Success",
            "Report exported successfully."
        )


if __name__ == "__main__":

    root = tk.Tk()
    app = FiledReportsApp(root)
    root.mainloop()