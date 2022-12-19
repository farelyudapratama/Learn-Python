# Import library time dan threading
import time
import threading

# Import library pynput.mouse untuk mengontrol mouse
from pynput.mouse import Button, Controller

# Import library pynput.keyboard untuk menangani event keyboard
from pynput.keyboard import Listener, KeyCode

# Variabel yang digunakan untuk mengatur auto clicker
delay = 0.001  # Durasi delay setiap klik
button = Button.left  # Tombol yang akan digunakan untuk klik
start_stop_key = KeyCode(char='t')  # Tombol untuk mengaktifkan/menonaktifkan auto clicker
exit_key = KeyCode(char='c')  # Tombol untuk menghentikan program

# Kelas ClickMouse untuk mengatur thread auto clicker
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        # Loop utama untuk mengeksekusi klik
        while self.program_running:
            while self.running:
                # Klik tombol yang telah ditentukan
                mouse.click(self.button)
                # Delay sebelum melakukan klik berikutnya
                time.sleep(self.delay)
            # Delay sebelum memeriksa kembali status auto clicker
            time.sleepc(0.1)

# Buat instance dari kelas Controller untuk mengontrol mouse
mouse = Controller()
# Buat instance dari kelas ClickMouse untuk menjalankan thread auto clicker
click_thread = ClickMouse(delay, button)
click_thread.start()

# Fungsi untuk menangani event keyboard
def on_press(key):
    # Jika tombol start_stop_key ditekan, maka aktifkan/nonaktifkan auto clicker
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    # Jika tombol exit_key ditekan, maka hentikan program
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

# Jalankan thread Listener untuk menangani event keyboard
with Listener(on_press=on_press) as listener:
    listener.join()