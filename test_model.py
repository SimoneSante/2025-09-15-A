from model.model import Model


def main():
    model = Model()

    b="2016-01-01"
    c="2018-12-28"

    cat=7
    print(f"Costruisco il grafo con c = {c,b}...")

    model.build_graph(c,b,cat)

    n_nodi, n_archi = model.get_stats()

    print(model.top3())
    listatot, big=model.connesse()
    for a in listatot:
        print(a)
    print(big)



if __name__ == "__main__":
    main()