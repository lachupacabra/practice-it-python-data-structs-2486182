from collections import namedtuple

Driver = namedtuple("Driver", "name, car_type, car_capacity ")


def check_capacity(driver, qty):
    return driver.car_capacity < qty


def main():
    # add code here
    # create a driver with a name, car type, and car capacity
    # an example you can use to practice: "Iris", "Toyota Prius", 7
    # check if they can take a certain order, given their car's capacity.
    iris = Driver("iris", "Toyota Prius", 7)
    order_qty = 10
    print(
        f"Driver name: {iris.name} has capacity for order : {check_capacity(iris,order_qty)}"
    )
    return


if __name__ == "__main__":
    main()
