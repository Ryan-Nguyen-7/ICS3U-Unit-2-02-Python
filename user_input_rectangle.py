#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program calculates area and perimeter of a rectangle
#   with inputted dimensions


def main():
    # this function calculates area and perimeter

    # input
    length = int(input("Enter length of rectangle (cm):"))
    width = int(input("Enter width of rectangle (cm):"))

    # process
    area = length*width
    perimeter = 2*(length+width)

    # output
    print("")
    print("Area is {}cm^2".format(length*width))
    print("Perimeter is {}cm".format(2*(length+width)))


if __name__ == "__main__":
    main()
