import os
import sys
import display
import numbers
from prettytable import PrettyTable


def import_library(data):
        with open("/home/pulson/Desktop/CODECOOLMUSICLIBRARY/library.txt", "r") as imported_data:
            lines_list = []
            for line in imported_data:
                lines_list.append(line)
            for element in lines_list:
                single_value = element.strip().split(",")
                data.append(single_value)
            return data


def drawing_table(input_data):
    i = 0
    ID = 1
    table = PrettyTable()
    table.field_names = ["ID", "Artist", "Album name", "Release year", "Genre", "Length"]
    for element in input_data:
        table.add_row([ID, input_data[i][0], input_data[i][1], input_data[i][2], input_data[i][3], input_data[i][4]])
        i += 1
        ID += 1
    print(table)


def find_by_genre(input_data):
    loop = True
    while loop:
        genre = input("Please enter a genre which you are looking for: ")
        genre = genre.strip()
        if genre.isdigit():
            os.system("clear")
            print("Please enter genre not a number.")
        else:
            os.system("clear")
            genres_table = []
            output_data = []
            for albums in input_data:
                genres_table.append(albums[3])
            if genre in genres_table:
                for album in input_data:
                    if genre in album[3]:
                        output_data.append(album)
                return drawing_table(output_data)
            else:
                print("There are no", genre, "albums")


def find_by_name(input_data):
    loop = True
    while loop:
        album_name = input("Please enter name of album which you are looking for: ")
        os.system("clear")
        names_table = []
        output_data = []
        album_name = album_name.strip()
        for albums in input_data:
            names_table.append(albums[1])
        if album_name in names_table:
            for album in input_data:
                if album_name in album[1]:
                    output_data.append(album)
            return drawing_table(output_data)
        else:
            print("There are no albums named", album_name)


def find_by_artist(input_data):
    loop = True
    while loop:
        artist_name = input("Please enter name of artist to search for his albums: ")
        artist_name = artist_name.strip()
        if artist_name.isdigit():
            os.system("clear")
            print("Please enter name of an artist not number.")
        else:
            os.system("clear")
            artists_table = []
            output_data = []
            for albums in input_data:
                artists_table.append(albums[0])
            if artist_name in artists_table:
                for album in input_data:
                    if artist_name in album[0]:
                        output_data.append(album)
                return drawing_table(output_data)
            else:
                print("There are no albums made by", artist_name)


def add_album():
    with open("/home/pulson/Desktop/CODECOOLMUSICLIBRARY/library.txt", 'a') as file:
        new_album = []
        loop = True
        while loop:
            artist_name = input("Artist name: ")
            artist_name = artist_name.strip()
            if artist_name.isdigit() or artist_name == "":
                new_album = []
                print("Enter valid artist name (not a number)")

            else:
                new_album.append(artist_name)

                album_name = input("Album name: ")
                album_name = album_name.strip()
                if album_name == "":
                    new_album = []
                    os.system("clear")
                    print("Enter valid album name")
                else:
                    new_album.append(album_name)
                    release_year = input("Release year: ")
                    release_year = release_year.strip()
                    if release_year.isdigit():
                        release_year_int = int(release_year)
                        if release_year_int < 2019 and release_year_int > 0:
                            new_album.append(release_year)
                            genre = input("Genre: ")
                            genre = genre.strip()
                            if genre.isdigit() or genre == "":
                                new_album = []
                                os.system("clear")
                                print("Next time enter valid genre")
                            else:
                                new_album.append(genre)
                                length_minutes = input("Length (mm):  ")
                                length_minutes = length_minutes.strip()
                                length_seconds = input("Length (ss):  ")
                                length_seconds = length_seconds.strip()

                                if not length_minutes or not length_seconds:
                                    new_album = []
                                    os.system("clear")
                                    print("Next time enter valid time (mm) and (ss smaller then 60)")
                                else:

                                    if length_minutes.isdigit() and length_seconds.isdigit():
                                        length_seconds_int = int(length_seconds)
                                        if length_seconds_int < 60:
                                            length = (length_minutes, length_seconds)
                                            length_seconds_string = str(length[0])
                                            length_minutes_string = str(length[1])
                                            length_string = (length_seconds_string + ":" + length_minutes_string)
                                            new_album.append(length_string)

                                            file.write("\n")
                                            i = 4
                                            for element in new_album:
                                                file.write(element)

                                                if i > 0:
                                                    file.write(",")
                                                    i -= 1
                                            file.close()

                                            os.system("clear")
                                            albums_list = []
                                            albums_list = import_library(albums_list)
                                            return drawing_table(albums_list)
                                        else:
                                            new_album = []
                                            os.system("clear")
                                            print("Next time enter valid time (mm) and (ss smaller then 60)")
                                    else:
                                        new_album = []
                                        os.system("clear")
                                        print("Next time enter valid time (mm) and (ss smaller then 60)")
                        else:
                            new_album = []
                            os.system("clear")
                            print("Next time enter valid year (2018 or lower)")
                    elif release_year == "" or isinstance(release_year, str):
                        new_album = []
                        os.system("clear")
                        print("Next time enter valid year (number, 2018 or lower)")


def delete_album(albums_list):
    loop = True
    while loop:
        index_of_line_to_delete = input("Which album do you want to delete? Write it's ID here: ")
        index_of_line_to_delete = index_of_line_to_delete.strip()
        if index_of_line_to_delete.isdigit():
            index_of_line_to_delete = int(index_of_line_to_delete)
            amount_of_albums = len(albums_list)
            if index_of_line_to_delete > amount_of_albums:
                print("Enter values from 1 to", amount_of_albums, ".")
            else:
                index_of_line_to_delete -= 1

                input_file = open("/home/pulson/Desktop/CODECOOLMUSICLIBRARY/library.txt", "r")
                data_list = input_file.readlines()
                input_file.close

                del data_list[index_of_line_to_delete]
                output_file = open("/home/pulson/Desktop/CODECOOLMUSICLIBRARY/library.txt", "w")
                output_file.writelines(data_list)
                output_file.close()

                albums_list = []
                albums_list = import_library(albums_list)
                os.system("clear")
                return drawing_table(albums_list)
        else:
            print("Please enter an integer value.")


def find_albums_made_in_given_year(albums_list):
    loop = True
    while loop:
        amount_of_albums = len(albums_list)
        # year_int = int(input("Enter year (yyyy): "))
        year = input("Enter year (yyyy): ")
        year = year.strip()
        if year.isdigit():
            year_int = int(year)
            if year_int > 2018:
                os.system("clear")
                print("I don't know what albums will be made in future :D")
                print("Let's stick to the present")
            else:
                year_string = str(year)
                years_table = []
                output_data = []
                os.system("clear")
                for albums in albums_list:
                    years_table.append(albums[2])
                if year_string in years_table:
                    for album in albums_list:
                        if year_string in album[2]:
                            output_data.append(album)
                    return drawing_table(output_data)
                else:
                    print("There are no albums made in", year)
        else:
            os.system("clear")
            print("Please enter valid number (not a string or negative number): ")
            continue


def find_albums_made_between_years(albums_list):
    loop = True
    while loop:
        years_range = []
        starting_year = input("Enter starting year: ")
        starting_year = starting_year.strip()
        if starting_year.isdigit():
            starting_year_int = int(starting_year)
            if starting_year_int > 2018:
                os.system("clear")
                print("You can't search for albums in future.")
                print("Let's stick to the present")
            else:
                starting_year = int(starting_year)
                years_range.append(starting_year)
                ending_year = input("Enter ending year: ")
                ending_year = ending_year.strip()
                ending_year_int = int(ending_year)
                if ending_year_int > 2018:
                    os.system("clear")
                    print("You can't search for albums in future.")
                    print("Let's stick to the present")
                else:
                    if ending_year.isdigit():
                        ending_year = int(ending_year)
                        years_range.append(ending_year)
                        output_data = []
                        os.system("clear")
                        for album in albums_list:
                            if int(album[2]) in range(years_range[0], years_range[1]+1):
                                output_data.append(album)
                        return drawing_table(output_data)
                    else:
                        os.system("clear")
                        print("Please enter valid number (not a string or negative number): ")
                    continue
        else:
            os.system("clear")
            print("Please enter valid number (not a string or negative number): ")
            continue


def find_shortest_album(albums_list):
    print("")
    print("")
    print("Shortest album in library: ")
    n = 0
    ID = n
    output_data = []
    shortest_album = albums_list[n][4]
    shortest = shortest_album.split(":")
    minutes = int(shortest[0])
    seconds = int(shortest[1])
    seconds_final = (minutes * 60) + seconds
    n += 1
    while n < len(albums_list):
        length = albums_list[n][4]
        length_split = length.split(":")
        minutes = int(length_split[0])
        seconds = int(length_split[1])
        sec_final = (minutes * 60) + seconds
        if seconds_final > sec_final:
            ID = n
            seconds_final = sec_final
        n += 1
    output_data.append(albums_list[ID])
    return drawing_table(output_data)


def find_longest_album(albums_list):
    print("")
    print("")
    print("Longest album in library: ")
    n = 0
    ID = n
    output_data = []
    longest_album = albums_list[n][4]
    longest = longest_album.split(":")
    minutes = int(longest[0])
    seconds = int(longest[1])
    seconds_final = (minutes * 60) + seconds
    n += 1
    while n < len(albums_list):
        length = albums_list[n][4]
        length_split = length.split(":")
        minutes = int(length_split[0])
        seconds = int(length_split[1])
        sec_final = (minutes * 60) + seconds
        if seconds_final < sec_final:
            ID = n
            seconds_final = sec_final
        n += 1
    output_data.append(albums_list[ID])
    return drawing_table(output_data)


def amount_of_albums(albums_list):
    print("")
    print("")
    amount_of_albums = len(albums_list)
    print("Amount of albums in library:", amount_of_albums)


def albums_by_genres(albums_list):
    print("")
    print("")
    genres = []
    for n in range(len(albums_list)):
        genres.append(albums_list[n][3])
        n += 1
    genres_set = set(genres)
    genres_count = 0
    genres_display = {}
    rock_count = 0
    hiphop_count = 0
    for element in genres_set:
        genres_count = genres.count(element)
        if "rock" in str(element):
            rock_count += 1
            genres_display["rock"] = rock_count
        elif "hip hop" in str(element):
            hiphop_count += 1
            genres_display["hip hop"] = hiphop_count + 1
        else:
            genres_display[element] = genres_count
    for genre, amount_of_albums in genres_display.items():
        print(genre, "-", amount_of_albums)


def oldest_or_youngest_album(albums_list, oldest_or_youngest):
    youngest_album = []
    oldest_album = []
    years_string = []
    print("")
    print("")
    for album in albums_list:
        years_string.append(album[2])
        years_integer = [int(element) for element in years_string]
        index_of_youngest_album = years_integer.index(max(years_integer))
        index_of_oldest_album = years_integer.index(min(years_integer))
    youngest_album.append(albums_list[index_of_youngest_album])
    oldest_album.append(albums_list[index_of_oldest_album])
    if oldest_or_youngest == "youngest":
        print("Youngest album in library: ")
        return drawing_table(youngest_album)
    else:
        print("Oldest album in library: ")
        return drawing_table(oldest_album)


if __name__ == "__main__":
    main()
