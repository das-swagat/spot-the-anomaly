import numpy as np
import matplotlib.pyplot as plt

def series(n=120):
    t = np.linspace(0, 8 * np.pi, n)
    return np.sin(t) + 0.05 * np.random.randn(n)

def inject(x):
    i = np.random.randint(len(x) // 4, 3 * len(x) // 4)
    x[i:i+3] += 1.2
    return i

def score(x, w=5):
    s = np.zeros_like(x)
    for i in range(len(x)):
        l = max(0, i - w)
        r = min(len(x), i + w)
        s[i] = abs(x[i] - x[l:r].mean())
    return s

def preview(x):
    plt.figure(figsize=(10, 3))
    plt.plot(x, linewidth=1)
    plt.title("Time series (anomaly hidden)")
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(20)
    plt.close()

def main():
    x = series()
    truth = inject(x)

    print("\nInspect the signal. You have 20 seconds.\n")
    preview(x)

    try:
        guess = int(input("Your estimate (index 0–119): "))
    except ValueError:
        return

    s = score(x)
    model = int(np.argmax(s))

    du = abs(guess - truth)
    dm = abs(model - truth)

    print("\nResults")
    print(" user :", guess)
    print(" model:", model)
    print(" truth:", truth)

    print("\nDistance from anomaly")
    print(" user :", du)
    print(" model:", dm)

    plt.figure(figsize=(10, 4))
    plt.plot(x, linewidth=1)

    plt.axvline(truth, linestyle="--", linewidth=1, label="truth")
    plt.axvline(model, linestyle=":", linewidth=1, label="model")
    plt.axvline(guess, linestyle="-.", linewidth=1, label="user")

    plt.title("Anomaly localization")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
