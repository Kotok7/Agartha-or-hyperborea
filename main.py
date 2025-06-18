# PLEASE INSTALL PILLOW BEFORE OPENING
# pip install pillow

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

        self.prompt_lbl = tk.Label(master, text="Select Agartha or Hyperborea:", font=("Arial", 12))
        self.prompt_lbl.pack(pady=5)

        self.img_label = tk.Label(master)
        self.img_label.pack(padx=10, pady=10)

        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)
        self.btn_a = tk.Button(btn_frame, text="Agartha", width=12,
                               command=lambda: self.answer("Agartha"))
        self.btn_b = tk.Button(btn_frame, text="Hyperborea", width=12,
                               command=lambda: self.answer("Hyperborea"))
        self.btn_a.pack(side=tk.LEFT, padx=5)
        self.btn_b.pack(side=tk.LEFT, padx=5)

        self.feedback = tk.Label(master, text="", font=("Arial", 12))
        self.feedback.pack(pady=5)

        self.load_question()

    def load_question(self):
        if self.index >= len(self.questions):
            return self.end_quiz()

        q = self.questions[self.index]

        self.progress_lbl.config(text=f"Question {self.index+1} of {len(self.questions)}")
        self.score_lbl.config(text=f"Score: {self.score}")

        if self.index >= len(self.questions) - 2:
            self.prompt_lbl.config(text="Is he from Agartha or Hyperborea?")
        else:
            self.prompt_lbl.config(text="Select Agartha or Hyperborea:")

        path = q['image']
        if not os.path.isfile(path):
            messagebox.showerror("Error", f"File not found:\n{path}")
            self.master.destroy()
            return

        img = Image.open(path).resize((400, 300), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.photo)

    def answer(self, user_answer):
        correct_answer = self.questions[self.index]['answer']
        is_correct = (user_answer == correct_answer)
        if is_correct:
            self.score += 1

        self.feedback.config(
            text="Correct!" if is_correct else "Wrong!",
            fg="green" if is_correct else "red"
        )

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
        {'image': 'photos/agartha1.png',    'answer': 'Agartha'},
        {'image': 'photos/hyperborea1.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/agartha2.webp',   'answer': 'Agartha'},
        {'image': 'photos/hyperborea2.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/agartha3.jpg',    'answer': 'Agartha'},
        {'image': 'photos/hyperborea3.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/agartha4.jpg',    'answer': 'Agartha'},
        {'image': 'photos/hyperborea4.jpg', 'answer': 'Hyperborea'},
        {'image': 'photos/agartha5.png',     'answer': 'Agartha'},
        {'image': 'photos/hyperborea5.jpg',  'answer': 'Hyperborea'},
    ]
    normal, last_two = all_qs[:-2], all_qs[-2:]
    random.shuffle(normal)
    questions = normal + last_two

    root = tk.Tk()
    root.title("Agartha vs Hyperborea Quiz")
    root.geometry("500x550")
    ImageQuiz(root, questions)
    root.mainloop()

if __name__ == '__main__':
    main()
