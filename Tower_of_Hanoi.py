def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


disks = int(input("Enter number of disks: "))

if disks <= 0:
    print("Number of disks must be greater than zero.")
else:
    tower_of_hanoi(disks, "A", "B", "C")
