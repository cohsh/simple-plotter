#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt


class Data:
    path: str
    name: str
    label: list[str]
    value: np.array

    def __init__(self, path: str):
        self.path = path
        self.name = self._get_name()
        self.value = self._get_value()
        self.label = self._get_label()

    def convert_xscale(self, axis: str, scale: float):
        self.x = [v * scale for v in self.x]

    def convert_yscale(self, axis: str, scale: float):
        self.y = [v * scale for v in self.y]

    def _get_name(self):
        list_path = self.path.split('.')
        n = len(list_path)
        if (n == 1):
            path_wo_fe = list_path[0]
        else:
            path_wo_fe = ''

        for i in range(n-1):
            path_wo_fe += list_path[i]

        return path_wo_fe

    def _get_value(self):
        path = self.path
        value = np.loadtxt(path, comments='#', unpack=True, dtype='float')
        return value

    def _get_label(self):
        with open(self.path) as f:
            first_line = next(f)
        list_first_line = first_line.split()
        del list_first_line[0]
        return list_first_line


class PlottingData:
    name: str
    xlabel: str
    ylabel: str
    graph: dict[str, np.array]

    def __init__(self):
        self.xlabel = ''
        self.ylabel = ''
        self.graph = {}


def parse_for_matplot(data: Data) -> PlottingData:
    name = data.name
    value = data.value
    label = data.label

    parsed_data = PlottingData()
    parsed_data.name = name
    parsed_data.xlabel = label[0]
    x = value[0]
    for i in range(1, len(value)):
        key = label[i]
        val = np.array([x, value[i]])
        parsed_data.graph[key] = val
    return parsed_data


def main():
    args = sys.argv
    path = args[1]

    data = Data(path)
    parsed_data = parse_for_matplot(data)

    fig = plt.figure(figsize=(4, 3), dpi=200)
    ax = fig.add_subplot(111)

    graph = parsed_data.graph
    name = parsed_data.name

    for key, val in graph.items():
        ax.plot(val[0], val[1], label=key)

    xlabel = parsed_data.xlabel

    ax.set_xlabel(xlabel)
    ax.legend()

    plt.savefig(name + '.pdf', bbox_inches='tight', pad_inches=0.1)
    plt.show()


if __name__ == '__main__':
    main()
