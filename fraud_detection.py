# Name: Beth Gronski
# CSE 160
# Homework 6

import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import csv
import matplotlib.pyplot as plt
import random


###
# Problem 1
###

def extract_election_votes(filename, column_names):
    # Takes a filename and a list of column names
    # Returns a list of integers that contains the values in those columns
    # from every row (the order of the integers does not matter).
    row_return = []
    file_csv = open(filename)
    input_file = csv.DictReader(file_csv)
    for row in input_file:
        for column in column_names:
            data = row[column]
            data = data.replace(' ', '')
            data = data.replace(',', '')
            data = data.replace('_', '')
            data = data.replace(',', '')
            if data == '':
                pass
            else:
                int_data = int(data)
            # for some reason us_election has random commas in dataset,
            # so this replaces those extra commas with '', and then
            # the code should ignore them while changing the strings
            # of numbers into integers
            row_return.append(int_data)
    file_csv.close()
    return row_return


###
# Problem 2
###

def ones_and_tens_digit_histogram(numbers):
    # Takes as input a list of numbers
    # Produces as output a list of 10 numbers.
    digits = []
    for x in numbers:
        num = x % 100
        tens = num // 10
        digits.append(tens)
        tens = 0
        ones = num % 10
        digits.append(ones)
        ones = 0
    total_num = len(digits)
    histo_list = []
    for x in range(0, 10):
        x_total = digits.count(x)
        distribution = x_total/total_num
        histo_list.append(distribution)
    return histo_list


###
# Problem 3
###

def plot_iran_least_digits_histogram(histogram):
    # Takes a histogram (as created by ones_and_tens_digit_histogram)
    # Graphs the frequencies of the ones and tens digits for the
    # Iranian election data.
    # Save your plot to a file named iran-digits.png using plt.savefig.
    # The function should not return anything.
    # It is all right to have the name of the output file and
    # labels for the graph hard-coded as strings inside of this function.
    result = [0.1] * 10
    plt.plot(histogram, color='r', label="iran")
    plt.plot(result, color='b', label="ideal")
    plt.axis([-0.5, len(histogram) - 0.5, None, None])
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.legend(loc='upper left')
    plt.title("Distribution of the last two digits in Iranian dataset")
    plt.savefig("iran-digits.png")
    # plt.show()
    plt.clf()


###
# Problem 4
###

def random_int_list(k):
    # Creates a list of random integers of k length
    # Integers can only 0 <= x < 100 (Note: 100 is not included here)
    # Returns the list
    i = 0
    ran_int_lst = []
    for i in range(0, k):
        ran_int_lst.append(random.randint(0, 99))
    return ran_int_lst


def plot_dist_by_sample_size():
    # Creates five different collections (one of size 10, another of
    # size 50, then 100, 1000, and 10,000) of random numbers
    # where every element in the collection is a different random
    # number x such that 0 <= x < 100 (Note: 100 is not included here,
    # why not?).
    # Plots the digit histograms for each of those collections on
    # one graph. Your function should save your plot as random-digits.png.
    # The function should not return anything.
    result = [0.1] * 10
    plt.plot(result, color='b', label="ideal")
    plt.plot(ones_and_tens_digit_histogram(random_int_list(10)),
             color='y', label="10 random numbers")
    plt.plot(ones_and_tens_digit_histogram(random_int_list(50)),
             color='g', label="50 random numbers")
    plt.plot(ones_and_tens_digit_histogram(random_int_list(100)),
             color='r', label="100 random numbers")
    plt.plot(ones_and_tens_digit_histogram(random_int_list(1000)),
             color='m', label="1000 random numbers")
    plt.plot(ones_and_tens_digit_histogram(random_int_list(10000)),
             color='k', label="10000 random numbers")
    plt.axis([-0.5, 9.5, None, None])
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.legend(loc='upper left')
    plt.title("Distribution of the last two digits in" +
              "randomly generated dataset")
    plt.savefig("random-digits.png")
    # plt.show()
    plt.clf()


###
# Problem 5
###

def mean_squared_error(numbers1, numbers2):
    # Takes two lists of numbers (assume the lists have
    # the same length and not empty)
    # Returns the mean squared error between the lists.
    total = 0
    for x in range(0, len(numbers1)):
        num1_digit = numbers1[x]
        num2_digit = numbers2[x]
        add_square = (num1_digit - num2_digit) ** 2
        total = total + add_square
    mean_sq_er = total/len(numbers1)
    return mean_sq_er


###
# Problem 6
###

def calculate_mse_with_uniform(histogram):
    # Takes a histogram (as created by ones_and_tens_digit_histogram)
    # Returns the mean squared error of the given histogram
    # with the uniform distribution.
    result = [0.1] * 10
    return mean_squared_error(histogram, result)


def compare_mse_to_samples(mse, number_of_datapoints):
    # returns a dictionary with values of sample mse that is 'more_than',
    # 'less_than' and the 'p_value'
    less_than = []
    more_than = []
    compare_mse_dict = {}
    for x in range(10000):
        lst = random_int_list(number_of_datapoints)
        lst_histo = ones_and_tens_digit_histogram(lst)
        random_mse = calculate_mse_with_uniform(lst_histo)
        if random_mse < mse:
            less_than.append(random_mse)
        else:
            more_than.append(random_mse)
    compare_mse_dict["p_value"] = len(more_than)/10000
    compare_mse_dict["more_than"] = len(more_than)
    compare_mse_dict["less_than"] = len(less_than)
    return compare_mse_dict


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    dict_mse = compare_mse_to_samples(iran_mse, number_of_iran_datapoints)
    print("2009 Iranian election MSE:", iran_mse)
    print("Quantity of MSEs larger than or equal to the 2009",
          "Iranian election MSE:",
          dict_mse["more_than"])
    print("Quantity of MSEs smaller than the 2009 Iranian election MSE:",
          dict_mse["less_than"])
    print("2009 Iranian election null hypothesis rejection level p:",
          dict_mse["p_value"])


###
# Problem 8
###

def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    dict_mse = compare_mse_to_samples(us_mse, number_of_us_datapoints)
    print("2008 United States election MSE:", us_mse)
    print("Quantity of MSEs larger than or equal to the 2008",
          "United States election MSE:",
          dict_mse["more_than"])
    print("Quantity of MSEs smaller than the 2008 United States election MSE:",
          dict_mse["less_than"])
    print("2008 United States election null hypothesis rejection level p:",
          dict_mse["p_value"])


# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    plot_iran_least_digits_histogram(ones_and_tens_digit_histogram(
        extract_election_votes("election-iran-2009.csv",
                               ["Ahmadinejad", "Rezai",
                                "Karrubi", "Mousavi"])))
    plot_dist_by_sample_size()
    compare_iran_mse_to_samples(calculate_mse_with_uniform(
        ones_and_tens_digit_histogram(
            extract_election_votes("election-iran-2009.csv",
                                   ["Ahmadinejad", "Rezai",
                                    "Karrubi", "Mousavi"]))),
                                len(extract_election_votes(
                                    "election-iran-2009.csv",
                                    ["Ahmadinejad", "Rezai",
                                     "Karrubi", "Mousavi"])))
    print()
    compare_us_mse_to_samples(calculate_mse_with_uniform(
        ones_and_tens_digit_histogram(
            extract_election_votes("election-us-2008.csv",
                                   ["Obama", "McCain", "Nader",
                                    "Barr", "Baldwin", "McKinney"]))),
                              len(extract_election_votes(
                                  "election-us-2008.csv",
                                  ["Obama", "McCain", "Nader",
                                   "Barr", "Baldwin", "McKinney"])))


if __name__ == "__main__":
    main()
