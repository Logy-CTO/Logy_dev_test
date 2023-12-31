
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, BooleanVar
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/hongtaegsu/Downloads/build/assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("529x756")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 756,
    width = 529,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    264.0,
    378.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    264.0,
    278.0,
    image=image_image_2
)

canvas.create_text(
    87.0,
    574.0,
    anchor="nw",
    text="PAUSE/UNPAUSE TRACKING",
    fill="#FFFFFF",
    font=("Roboto Medium", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=21.0,
    y=621.0,
    width=488.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=21.0,
    y=682.0,
    width=488.0,
    height=50.0
)

#####토글####
def create_toggle_switch(window, canvas, x, y, scale=0.71):
    # 토글 상태 변수 및 이미지 로드
    toggle_status = BooleanVar()
    toggle_status.set(False)

    original_on_image = Image.open(relative_to_assets("toggle_on.png"))
    original_off_image = Image.open(relative_to_assets("toggle_off.png"))

    # 이미지 크기 조절
    on_image_resized = original_on_image.resize((round(original_on_image.width * scale), round(original_on_image.height * scale)), Image.LANCZOS)
    off_image_resized = original_off_image.resize((round(original_off_image.width * scale), round(original_off_image.height * scale)), Image.LANCZOS)

    toggle_on_image = ImageTk.PhotoImage(on_image_resized)
    toggle_off_image = ImageTk.PhotoImage(off_image_resized)

    # 토글 이미지 생성 및 위치 설정
    toggle_switch = canvas.create_image(x, y, image=toggle_off_image, anchor="nw")

    # 토글 동작 함수
    def toggle_action(event):
        if toggle_status.get():
            canvas.itemconfigure(toggle_switch, image=toggle_off_image)
            toggle_status.set(False)
        else:
            canvas.itemconfigure(toggle_switch, image=toggle_on_image)
            toggle_status.set(True)

    canvas.tag_bind(toggle_switch, "<Button-1>", toggle_action)

    return toggle_switch

toggle_switch_button = create_toggle_switch(window, canvas, x=33, y=567)
#########


window.resizable(False, False)
window.mainloop()
