import tkinter
from main import create_dict, shot_and_judge, card_sequence_to_link
from web import open_url, web_init, web_close

win = tkinter.Tk()
win.attributes("-alpha", 0.4)
win.wm_attributes('-topmost', 1)
win.title("Majsoul helper")
win.geometry("700x200")

title_label = tkinter.Label(win, text="No data")
title_label.pack()
sim_label = tkinter.Label(win, text="")
sim_label.pack()
state_label = tkinter.Label(win, text="")
state_label.pack()
info_label = tkinter.Label(win, text="")
info_label.pack()

hash_dict = create_dict()

driver = web_init()


def calculate():
    names, sims = shot_and_judge(hash_dict)
    # names = ["3s", "4s"]
    link = card_sequence_to_link(names)

    if len(names) % 3 == 2:
        cards = ""
        for name in names:
            cards += name
        title_label['text'] = cards

        web_page = open_url(driver, link)
        # print(web_page)

        sim_label['text'] = str(sims)

        state = web_page.split("<div id=\"tehai\" align=\"center\">")[1].split("<br>")[0]
        state_label['text'] = state

        split_page = web_page.split(cards)
        info = split_page[2].split("</textarea>")[0]
        info_label['text'] = info

        win.update()


tkinter.Button(win, text="计算", command=calculate).pack()
win.mainloop()
web_close(driver)
