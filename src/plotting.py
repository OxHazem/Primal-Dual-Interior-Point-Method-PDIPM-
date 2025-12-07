import os
from utils import plt, np

def plot_case_study(name, histories):
   
    fig_dir = "figures"
    os.makedirs(fig_dir, exist_ok=True)

    methods = list(histories.keys())

    plt.figure()
    for method in methods:
        plt.plot(histories[method]['obj'], marker='o', label=method)
    plt.title(f"{name} – Objective")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(fig_dir, f"{name}_objective.png"), dpi=300)
    plt.close()

    plt.figure()
    for method in methods:
        xs = np.array(histories[method]['x'])
        if xs.shape[1] >= 2:
            plt.plot(xs[:, 0], xs[:, 1], marker='o', label=method)
    plt.title(f"{name} – Central Path")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(fig_dir, f"{name}_central_path.png"), dpi=300)
    plt.close()

    plt.figure()
    for method in methods:
        plt.semilogy(histories[method]['mu'], marker='o', label=method)
    plt.title(f"{name} – Complementarity")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(fig_dir, f"{name}_complementarity.png"), dpi=300)
    plt.close()
