import matplotlib.pyplot as plt

mouse_1 = {}
mouse_1["niacin"] = [3, 3, 2, 2, 1, 1.5, 1.5, 1.75, 1.75, 1.75,]
mouse_1["bodyweight"] = [24.5, 25.3, 25.8, 26.2, 25.1, 26.3, 26.5, 26.7, 26.8, 27.1]
mouse_1["water"] = [6.1,6.2,6.4,6.2,10.2,9.9,9.7,6.5,6.2,6.4]

mouse_2 = {}
mouse_2["niacin"] = [3,3,2,2,1,1,0.75,0.75,0.5,0.7,0.75,0.75,0.75]
mouse_2["bodyweight"] = [27.1,27.4,27.9,28.3,28.6,29,29.1,29.2,28.5,29.1,29.2,29.4,29.5]
mouse_2["water"] = [6.1,6.2,6.4,6.2,6.3,5.9,6.2,6.5,6.2,6.4,6.5,6,6.1]

mouse_3 = {}
mouse_3["niacin"] = [3, 3, 2, 2.5, 2.5, 2.5, 2.5]
mouse_3["bodyweight"] = [24.8, 25.0, 23.6, 23.9, 24.4, 25.1, 25.3]
mouse_3["water"] = [6.1,6.2,9.4,6.2,6.3,5.9,6.2]


def make_figure(mouse_dict):
    f, ax = plt.subplots(nrows=3, sharex=True)

    niacin = mouse_dict["niacin"]
    bws = mouse_dict["bodyweight"]
    water = mouse_dict["water"]

    ax[0].step(range(len(niacin)), niacin)
    ax[1].plot(bws, marker="o")
    ax[2].plot(water)

    ax[0].set_ylabel("Niacin (mg/L)")
    ax[0].set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
    ax[0].set_ylim([0,3.4])

    ax[1].set_ylabel("Body weight (g)")
    ax[2].set_ylabel("Water intake (mL)")
    ax[2].set_ylim([0,12])

    ax[2].set_xlabel("Days")
    ax[2].set_xticklabels([str(int(x*3)) for x in ax[2].get_xticks()])

    # add percentage bodyweight drop as annotation?

    # plt.show()

    return f

f = make_figure(mouse_1)
f.savefig("..//results//mouse_1.png")

f = make_figure(mouse_2)
f.savefig("..//results//mouse_2.png")

f = make_figure(mouse_3)
f.savefig("..//results//mouse_3.png")