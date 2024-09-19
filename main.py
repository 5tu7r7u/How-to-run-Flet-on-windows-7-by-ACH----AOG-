import flet as ft 
import cv2 as cv 
import base64


def l(i):
    i=cv.resize(i,(700,1400))
    _,im_arr=cv.imencode(".png",i)
    im_b64=base64.b64encode(im_arr)
    return im_b64.decode("utf-8")





cap=cv.VideoCapture(0)
def main(page:ft.Page):
    page.window.width=350
    page.window.left=700
    page.window.top=1
    global t
    def p(e):
        global t
        t=True
    img=ft.Image(height=700)
    el=ft.ElevatedButton(text="go",on_click=p)

    st=ft.Container(bgcolor=ft.colors.BLACK87,content=ft.Stack(controls=[img,ft.Column(controls=[ft.Column(height=600),ft.Row([el],alignment=ft.MainAxisAlignment.CENTER)],alignment=ft.CrossAxisAlignment.END)]))
    page.add(st)
    t=False
    page.update()
    while True:
        _,im=cap.read()
        im=cv.flip(im,1)
        img.src_base64=l(im)
        if t==True:
            cv.imwrite("1.png",im)
            print(12)
            t=False
        page.update()
        cv.waitKey(1)

ft.app(main)
