import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

class ImageQuiz:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.index = 0
        self.score = 0

        tk.Label(master, text="Quiz: Agartha or Hyperborea", font=("Arial", 16)).pack(pady=5)

        self.progress_lbl = tk.Label(master, text="")
        self.progress_lbl.pack()
        self.score_lbl = tk.Label(master, text="Score: 0")
        self.score_lbl.pack(pady=2)

        self.prompt_lbl = tk.Label(master, text="", font=("Arial", 12))
        self.prompt_lbl.pack(pady=5)

        self.img_label = tk.Label(master)
        self.img_label.pack(padx=10, pady=10)

        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)
        self.btn_a = tk.Button(btn_frame, width=12)
        self.btn_b = tk.Button(btn_frame, width=12)
        self.btn_a.pack(side=tk.LEFT, padx=5)
        self.btn_b.pack(side=tk.LEFT, padx=5)

        self.feedback = tk.Label(master, text="", font=("Arial", 12))
        self.feedback.pack(pady=5)

        self.load_question()

    def load_question(self):
        if self.index >= len(self.questions):
            return self.end_quiz()

        q = self.questions[self.index]
        total = len(self.questions)

        self.progress_lbl.config(text=f"Question {self.index+1} of {total}")
        self.score_lbl.config(text=f"Score: {self.score}")

        if self.index >= total - 4:
            if 'agartha/allowed' in q['image'] or 'agartha/not_allowed' in q['image']:
                self.prompt_lbl.config(text="Is he allowed to Agartha? Yes/No")
            else:
                self.prompt_lbl.config(text="Is he allowed to Hyperborea? Yes/No")
            self.btn_a.config(text="Yes", command=lambda: self.answer("Yes"))
            self.btn_b.config(text="No", command=lambda: self.answer("No"))
        else:
            self.prompt_lbl.config(text="Select Agartha or Hyperborea:")
            self.btn_a.config(text="Agartha", command=lambda: self.answer("Agartha"))
            self.btn_b.config(text="Hyperborea", command=lambda: self.answer("Hyperborea"))

        path = q['image']
        if not os.path.isfile(path):
            messagebox.showerror("Error", f"File not found:\n{path}")
            self.master.destroy()
            return

        img = Image.open(path).resize((400, 300), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.photo)

    def answer(self, user_answer):
        correct = self.questions[self.index]['answer']
        if user_answer == correct:
            self.score += 1
            self.feedback.config(text="Correct!", fg="green")
        else:
            self.feedback.config(text="Wrong!", fg="red")

        self.index += 1
        self.master.after(1000, self.next_step)

    def next_step(self):
        self.feedback.config(text="")
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Final Score",
                            f"You got {self.score} out of {len(self.questions)} correct.")
        self.master.quit()


def main():
    all_qs = [
        {'image': 'photos/agartha/agartha1.jpg', 'answer': 'Agartha'},
        {'image': 'photos/agartha/agartha2.jpg', 'answer': 'Agartha'},
        {'image': 'photos/agartha/agartha3.jpg', 'answer': 'Agartha'},
        {'image': 'photos/agartha/agartha4.jpg', 'answer': 'Agartha'},
        {'image': 'photos/agartha/agartha5.jpg', 'answer': 'Agartha'},
        {'image': 'photos/agartha/agartha6.jpg', 'answer': 'Agartha'},
        {'image': 'photos/hyperborea/hyperborea1.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/hyperborea/hyperborea2.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/hyperborea/hyperborea3.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/hyperborea/hyperborea4.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/hyperborea/hyperborea5.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/hyperborea/hyperborea6.jpg', 'answer': 'Hyperborea'},
    ]
    last_four = [
        {'image': 'photos/agartha/allowed.jpg', 'answer': 'Yes'},
        {'image': 'photos/agartha/not_allowed.jpg', 'answer': 'No'},
        {'image': 'photos/hyperborea/allowed.jpg', 'answer': 'Yes'},
        {'image': 'photos/hyperborea/not_allowed.jpg', 'answer': 'No'},
    ]
    random.shuffle(all_qs)
    questions = all_qs + last_four

    root = tk.Tk()
    root.title("Agartha vs Hyperborea Quiz")
    root.geometry("500x600")
    ImageQuiz(root, questions)
    root.mainloop()

if __name__ == '__main__':
    main()
