from baby_names import BabyNamesProject

def main():
    file_name = 'data/yob2021.txt'

    # TODO: Read file into pandas
    bn = BabyNamesProject(file_name=file_name, separator=',')

    # TODO: Print the first ten rows
    print(bn.display_data())

    # TODO: Display the number of rows and columns
    rows, cols = bn.number_rows_cols()
    print(f'The number of rows is {rows}')
    print(f'The number of columns is {cols}')

    # TODO: Calculate the number of babies born
    total_babies_born = bn.total_babies_born()
    print(f'The total number of babies born is {total_babies_born}')

    # TODO: Calculate the sum for boys and girls separately
    total_born_by_sex_boys, total_born_by_sex_girls = bn.total_babies_born_by_sex()
    print(f"Total sum for boys: {total_born_by_sex_boys}")
    print(f"Total sum for girls: {total_born_by_sex_girls}")

    # TODO: Check if your name occurs in the data
    name = 'Temitope'
    try:
        foundName = bn.check_name(name)
        if foundName:
            print(f'{name} found')
        else:
            print(f'{name} not found')
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    # TODO: Calculate the percentage of boys and girls among the total births
    perc_boys, perc_girls = bn.percentage_boys_girls()
    print(f'The percentage of boys is: {perc_boys}%')
    print(f'The percentage of girls is: {perc_girls}%')

    # TODO: Create a table that contains the top 5 girls names and top 5 boys names.
    print(bn.top_names())

    # TODO: Write the data to the excel spreadsheet
    bn.write_to_excel()


if __name__ == '__main__':
    main()