from classes import GameOfLife


def main() -> None:
    g = GameOfLife('matrix.txt')
    g.run()

if __name__ == "__main__":
    main()

