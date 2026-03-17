🖐️ Hand Gesture Calculator

A real-time calculator that lets you perform arithmetic operations using hand gestures instead of a keyboard or mouse. Built using OpenCV and MediaPipe, this project detects your finger position and allows you to click virtual buttons on screen.

🚀 Features

✋ Hand tracking using MediaPipe

🖱️ Touchless interaction (index finger as pointer)

🔢 Virtual calculator UI

➕ Supports basic operations: +, -, *, /

🧹 Clear (C) and Evaluate (=) functions

⏱️ Click delay to prevent multiple accidental inputs

🛠️ Tech Stack

Python

OpenCV

MediaPipe

📁 Project Structure
📦 Hand-Gesture-Calculator
 ┣ 📜 main.py            # Main application
 ┣ 📜 gesture.py         # Hand detection logic
 ┣ 📜 calculator_ui.py   # Calculator UI rendering
 ┗ 📜 README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/hand-gesture-calculator.git
cd hand-gesture-calculator

Create virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate   # Windows

Install dependencies:

pip install opencv-python mediapipe
▶️ Usage

Run the main file:

python main.py

Use your index finger to hover over buttons

Hold for a moment to "click"

Perform calculations on screen

🧠 How It Works

MediaPipe detects hand landmarks

Index finger tip (landmark 8) is tracked

Position is mapped to calculator buttons

If finger stays on a button → input is registered

Expression is evaluated using Python eval()

⚠️ Limitations (Important)

❗ Uses eval() → not safe for complex/real-world apps

❗ Works best in good lighting conditions

❗ Only supports one hand

❗ No advanced operations (sqrt, %, etc.)

🔮 Future Improvements

✅ Add multi-hand support

✅ Add advanced math functions

✅ Improve UI design

✅ Add sound feedback on click

✅ Replace eval() with safer parser

📸 Demo

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ab5c3a9f-b3be-41b6-a95e-623186a456c1" />


🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

📄 License

This project is open-source and available under the MIT License.
