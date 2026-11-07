# -*- coding: utf-8 -*-
"""سامانه شمارش آرای شورای دانش‌آموزی
اجرا در ویندوز: py student_council.py
فقط با کتابخانه‌های استاندارد پایتون ساخته شده است.
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json, csv, os, html, tempfile, webbrowser

APP_TITLE = "سامانه شمارش آرای شورای دانش‌آموزی"
DATA_FILE = "student_council_data.json"

class ElectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1000x720")
        self.root.minsize(760, 560)
        self.root.configure(bg="#f3f6fb")
        self.candidates = []
        self.invalid = 0
        self.load_data()
        self.build_ui()
        self.refresh()

    def load_data(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.candidates = data.get("candidates", [])
                self.invalid = int(data.get("invalid", 0))
        except (OSError, ValueError, TypeError):
            self.candidates, self.invalid = [], 0

    def save_data(self):
        data = {"candidates": self.candidates, "invalid": self.invalid}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def build_ui(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("TButton", font=("Tahoma", 10), padding=7)
        style.configure("TEntry", font=("Tahoma", 11), padding=7)
        header = tk.Frame(self.root, bg="#173b67", height=100)
        header.pack(fill="x")
        tk.Label(header, text="سامانه انتخابات شورای دانش‌آموزی",
                 bg="#173b67", fg="white", font=("Tahoma", 21, "bold")).pack(pady=(18, 4))
        tk.Label(header, text="ثبت نامزدها • شمارش آرا • گزارش نهایی",
                 bg="#173b67", fg="#d8e8fa", font=("Tahoma", 10)).pack()

        stats = tk.Frame(self.root, bg="#f3f6fb")
        stats.pack(fill="x", padx=18, pady=14)
        self.total_var = tk.StringVar()
        self.valid_var = tk.StringVar()
        self.invalid_var = tk.StringVar()
        self.stat_box(stats, "کل آرا", self.total_var, "#245a91")
        self.stat_box(stats, "آرای معتبر", self.valid_var, "#21865b")
        self.stat_box(stats, "آرای باطله", self.invalid_var, "#b45b37")

        add = tk.Frame(self.root, bg="white", padx=14, pady=12,
                       highlightbackground="#dce4ee", highlightthickness=1)
        add.pack(fill="x", padx=18, pady=(0, 12))
        tk.Label(add, text="افزودن نامزد جدید", bg="white", fg="#173b67",
                 font=("Tahoma", 12, "bold")).pack(anchor="e")
        line = tk.Frame(add, bg="white")
        line.pack(fill="x", pady=(8, 0))
        self.name_entry = ttk.Entry(line, justify="right")
        self.name_entry.pack(side="right", fill="x", expand=True, padx=(8, 0))
        self.name_entry.bind("<Return>", lambda e: self.add_candidate())
        ttk.Button(line, text="افزودن نامزد", command=self.add_candidate).pack(side="right")

        tools = tk.Frame(self.root, bg="#f3f6fb")
        tools.pack(fill="x", padx=18, pady=(0, 10))
        ttk.Button(tools, text="ثبت یک رأی باطله", command=self.add_invalid).pack(side="right", padx=3)
        ttk.Button(tools, text="خروجی CSV", command=self.export_csv).pack(side="right", padx=3)
        ttk.Button(tools, text="چاپ گزارش", command=self.print_report).pack(side="right", padx=3)
        ttk.Button(tools, text="صفر کردن شمارش", command=self.reset_votes).pack(side="left", padx=3)

        self.canvas = tk.Canvas(self.root, bg="#f3f6fb", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.cards_frame = tk.Frame(self.canvas, bg="#f3f6fb")
        self.cards_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas_window = self.canvas.create_window((0, 0), window=self.cards_frame, anchor="nw")
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfigure(self.canvas_window, width=e.width))
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True, padx=(18, 0), pady=(0, 12))
        scrollbar.pack(side="right", fill="y", padx=(0, 18), pady=(0, 12))
        self.root.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-e.delta / 120), "units"))

        self.footer = tk.Label(self.root, text="اطلاعات شمارش به‌صورت خودکار در همین پوشه ذخیره می‌شود.",
                               bg="#f3f6fb", fg="#66758a", font=("Tahoma", 9))
        self.footer.pack(fill="x", pady=(0, 8))

    def stat_box(self, parent, title, variable, color):
        box = tk.Frame(parent, bg="white", padx=12, pady=10,
                       highlightbackground="#dce4ee", highlightthickness=1)
        box.pack(side="right", fill="x", expand=True, padx=5)
        tk.Label(box, text=title, bg="white", fg="#65758b",
                 font=("Tahoma", 10)).pack()
        tk.Label(box, textvariable=variable, bg="white", fg=color,
                 font=("Tahoma", 19, "bold")).pack(pady=(3, 0))

    def add_candidate(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("نام خالی", "لطفاً نام نامزد را وارد کنید.")
            self.name_entry.focus_set()
            return
        if any(c["name"].casefold() == name.casefold() for c in self.candidates):
            messagebox.showwarning("نام تکراری", "این نام قبلاً ثبت شده است.")
            return
        self.candidates.append({"name": name, "votes": 0})
        self.name_entry.delete(0, "end")
        self.save_data()
        self.refresh()

    def add_vote(self, index):
        self.candidates[index]["votes"] += 1
        self.save_data()
        self.refresh()

    def add_invalid(self):
        self.invalid += 1
        self.save_data()
        self.refresh()

    def remove_candidate(self, index):
        name = self.candidates[index]["name"]
        if messagebox.askyesno("حذف نامزد", f"نامزد «{name}» و آرای ثبت‌شده‌اش حذف شود؟"):
            self.candidates.pop(index)
            self.save_data()
            self.refresh()

    def reset_votes(self):
        if not messagebox.askyesno("تأیید", "تمام شمارش آرا صفر شود؟ نام نامزدها باقی می‌ماند."):
            return
        for c in self.candidates:
            c["votes"] = 0
        self.invalid = 0
        self.save_data()
        self.refresh()

    def refresh(self):
        valid = sum(int(c.get("votes", 0)) for c in self.candidates)
        total = valid + self.invalid
        self.total_var.set(str(total))
        self.valid_var.set(str(valid))
        self.invalid_var.set(str(self.invalid))
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        if not self.candidates:
            tk.Label(self.cards_frame, text="هنوز نامزدی ثبت نشده است.",
                     bg="#f3f6fb", fg="#718096", font=("Tahoma", 12)).pack(pady=35)
            return
        for i, candidate in enumerate(self.candidates):
            row, col = divmod(i, 2)
            card = tk.Frame(self.cards_frame, bg="white", padx=12, pady=12,
                            highlightbackground="#dce4ee", highlightthickness=1)
            card.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
            self.cards_frame.grid_columnconfigure(0, weight=1, uniform="cards")
            self.cards_frame.grid_columnconfigure(1, weight=1, uniform="cards")
            tk.Label(card, text=candidate["name"], bg="white", fg="#173b67",
                     font=("Tahoma", 13, "bold"), anchor="e").pack(fill="x")
            tk.Label(card, text=f'{candidate["votes"]} رأی',
                     bg="white", fg="#21865b", font=("Tahoma", 18, "bold")).pack(pady=8)
            buttons = tk.Frame(card, bg="white")
            buttons.pack(fill="x")
            ttk.Button(buttons, text="＋ ثبت رأی", command=lambda x=i: self.add_vote(x)).pack(side="right", fill="x", expand=True, padx=(0, 4))
            ttk.Button(buttons, text="حذف", command=lambda x=i: self.remove_candidate(x)).pack(side="left")

    def export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv",
                    filetypes=[("CSV", "*.csv")], initialfile="نتایج_انتخابات.csv")
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["نام نامزد", "تعداد رأی"])
            for c in self.candidates:
                writer.writerow([c["name"], c["votes"]])
            writer.writerow(["آرای باطله", self.invalid])
            writer.writerow(["کل آرا", sum(c["votes"] for c in self.candidates) + self.invalid])
        messagebox.showinfo("ذخیره شد", "فایل گزارش با موفقیت ذخیره شد.")

    def print_report(self):
        valid = sum(c["votes"] for c in self.candidates)
        total = valid + self.invalid
        rows = "".join(
            f"<tr><td>{html.escape(c['name'])}</td><td>{c['votes']}</td></tr>"
            for c in sorted(self.candidates, key=lambda x: x["votes"], reverse=True)
        )
        page = f"""<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8">
        <title>گزارش انتخابات شورای دانش‌آموزی</title>
        <style>body{{font-family:Tahoma,Arial;margin:35px;color:#172b45}}
        h1{{text-align:center;color:#173b67}}table{{width:100%;border-collapse:collapse;margin-top:25px}}
        th,td{{border:1px solid #9aa9ba;padding:12px;text-align:center}}
        th{{background:#eaf1f8}}.stats{{margin-top:22px;line-height:2}}
        @media print{{button{{display:none}}}}</style>
        <h1>گزارش نهایی انتخابات شورای دانش‌آموزی</h1>
        <table><tr><th>نام نامزد</th><th>تعداد رأی</th></tr>{rows}</table>
        <div class="stats"><p>آرای معتبر: {valid}</p><p>آرای باطله: {self.invalid}</p>
        <p><b>مجموع آرا: {total}</b></p></div>
        <button onclick="window.print()">چاپ گزارش</button></html>"""
        fd, path = tempfile.mkstemp(suffix=".html", prefix="election_report_")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(page)
        webbrowser.open("file://" + os.path.abspath(path))

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectionApp(root)
    root.mainloop()
