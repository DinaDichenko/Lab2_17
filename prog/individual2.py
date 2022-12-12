#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import json


def get_poezd(poezd_load, name, no, time, file_name):
    poezd_load.append({"name": name, "no": no, "time": time})
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(poezd_load, fout, ensure_ascii=False, indent=4)
    return load_poezd(file_name)


def list(poezd_load):
    if poezd_load:
        line = "+-{}-+-{}-+-{}-+".format(
            "-" * 10,
            "-" * 20,
            "-" * 8,
        )
        print(line)
        print("| {:^10} | {:^20} | {:^8} |".format(" No ", "Название", "Время"))
        print(line)

        for idx, po in enumerate(poezd_load, 1):
            print(
                "| {:>10} | {:<20} | {"
                "} |".format(po.get("no", ""), po.get("name", ""), po.get("time", ""))
            )
        print(line)


def select_poezd(poezd_load, nom):
    line = "+-{}-+-{}-+-{}-+".format(
        "-" * 10,
        "-" * 20,
        "-" * 8,
    )
    print(line)
    print("| {:^10} | {:^20} | {:^8} |".format(" No ", "Название", "Время"))
    print(line)
    count = 0

    for idx, po in enumerate(poezd_load, 1):
        if po.get("no", 0) == nom:
            count += 1
            print(
                "| {:>10} | {:<20} | {"
                "} |".format(po.get("no", ""), po.get("name", ""), po.get("time", ""))
            )
    print(line)
    if count == 0:
        print("Поездов с таким номером нет.")


def load_poezd(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        loadfile = json.load(fin)
    return loadfile


def help():
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("select <номер> - запросить поезд по номеру;")
    print("load - загрузить данные из файла;")
    print("save - сохранить данные в файл;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


@click.command()
@click.option("-c", "--command")
@click.argument("file_name")
@click.option("-n", "--name")
@click.option("-o", "--no")
@click.option("-t", "time")
def main(command, name, no, time, file_name):
    poezd_load = load_poezd(file_name)
    if command == "add":
        get_poezd(poezd_load, name, no, time, file_name)
        click.secho("Данные добавлены")
    elif command == "display":
        list(poezd_load)
    elif command == "select":
        select_poezd(poezd_load)


if __name__ == "__main__":
    main()
