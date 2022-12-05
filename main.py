import numpy as np
import pylab


def GetRauchFilterElements(cut_frequency, c):  # calculating filter elements
    H = 1  # transmission ratio
    w0 = cut_frequency * 6.28  # cutoff frequency
    alpha = 1.414  # the coefficient determining the type of frequency response
    c1 = c
    c2 = 0.05 * c

    r3 = (alpha * H - (np.sqrt(pow(alpha, 2) * pow(H, 2) - (4 * (1 + H) * H * 0.05)))) / (2 * w0 * c * H * 0.05)
    r1 = r3 / H
    r2 = 1 / (pow(w0, 2) * pow(c, 2) * r1 * 0.05)

    return [r1, r2, r3, c1, c2]


def DrawAmplFreqCharacter(r1, r2, r3, c1, c2, cut_freq):
    arr = []
    freq = []
    for i in range(1000):
        wi = (2 * 0.314 * i)
        freq.append(i)
        # transitional function
        G = (-1) / (((r1 / r3) + ((r1 * r2) / r3) * c2 * wi) + ((r1 + r2) * c2 * wi) + (r1 * r2 * c1 * c2 * pow(wi, 2)))
        arr.append(20 * np.log(abs(G)))

    print(arr)

    y_axis = np.array(arr)
    x_axis = np.array(freq)
    cut = np.empty(shape=1000)
    cut.fill(cut_freq)

    fig = pylab.figure()
    ax = fig.add_subplot()
    ax.set_xscale('log')
    ax.grid()
    pylab.ylabel("20 * Log(|G(p)|)")
    pylab.xlabel("Frequency")

    pylab.ylim([-4, 0])
    ax.plot(x_axis, y_axis, cut, y_axis)

    pylab.show()


if __name__ == '__main__':
    cut_off_frequency = 80
    a = GetRauchFilterElements(cut_off_frequency, 0.1e-6)
    DrawAmplFreqCharacter(a[0], a[1], a[2], a[3], a[4], cut_off_frequency)
