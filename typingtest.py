import tkinter as tk 

app = tk.Tk()


def start_timer():
    global remaining_time
    remaining_time = 30
    update_timer_label()
    countdown()

def update_timer_label():
    timer_label["text"] = f"Time remaining: {remaining_time} seconds"

def countdown():
    global remaining_time
    if remaining_time >0:
        remaining_time -= 1
        update_timer_label()
        timer_label.after(1000, countdown)
    else:
        timer_label['text'] = "Time's up!"
        count_completed_words()
        compare_completed_words()

def count_completed_words():
    global completed_words, words
    text = text_box.get("1.0", tk.END).strip()
    words = text.split()
    completed_words = [word for word in words if word.endswith(" ")]
    


def compare_completed_words():
    global completed_words, text_to_type, words
    words_to_type = text_to_type.split()
    correct_words = [word for word in words if word in words_to_type]
    accuracy = len(correct_words) / len(words_to_type) * 100
    wpm = (len(correct_words)/ 30) * 60
    accuracy_label = tk.Label(app, text=f"Accuracy {accuracy:.2f}% \n WPM: {wpm}", font=("Arial", 14))
    accuracy_label.grid(row=5, column=1)
    print(correct_words)
    

def start_typing():
    global text_box, placeholder_text, timer_label, remaining_time, text_to_type
    placeholder_text = "start typing here"
    input_box.delete("1.0", "end")
    text_box = tk.Text(height=3, width=50, font=("Arial", 14))
    text_box.grid(row=3, column=1, columnspan=3)
    text_box.insert("1.0", placeholder_text)
    text_box.bind("<FocusIn>", on_focus_in)
    text_box.bind("<FocusOut>", on_focus_out)
    timer_label = tk.Label(app, text="time remaining: 30 seconds",  font=("Arial", 14))
    timer_label.grid(row=4, column=1)
    start_timer()
    text_to_type = "The quick brown fox jumps over the lazy dog. Today is a beautiful day with clear\n skies and gentle breeze. The sun shines brightly, casting a warm glow on the\n lush green fields. Birds chirp merrily as they flutter from tree to tree. \nThe river flows peacefully, reflecting the serene landscape. It's a \nperfect day for a leisurely stroll in the park."
    
    overlay_label = tk.Label(text=text_to_type, bg="lightgray", fg="gray", font=("Arial", 12))
    overlay_label.place(x=95, y=110)
    
    
def on_focus_in(event):
    if text_box.get("1.0", tk.END).strip() == placeholder_text:
        text_box.delete("1.0", tk.END)

def on_focus_out(event):
    if text_box.get("1.0", tk.END).strip() == "":
        text_box.insert(tk.END, placeholder_text)  


app.title("Typing Speed Test")
app.geometry("750x600")
app.configure(bg="#F7F1E5")

main_label = tk.Label(text="The Typing Test", font=("Arial", 40))
main_label.configure(bg="#F7F1E5", fg="#898121")
main_label.grid(row=0, column=1, sticky="nsew", columnspan=3)

typint_text = tk.Label(text="How fast are your fingers? Do the one-minute typing test to find out!\n Press the space bar after each word. At the end, you'll get your typing speed in CPM and WPM. Good luck!", font=("Arial", 12))
typint_text.configure(bg="#F7F1E5", fg="#4C4B16")
typint_text.grid(row=1, column=1, columnspan=3)
input_box = tk.Text(height=4, width=50, font=("Arial", 14))
input_box.grid(row=2, column=1, columnspan=3)

start_button = tk.Button(text="start typing", command=start_typing)
start_button.grid(row=4, column=1)





app.mainloop()
