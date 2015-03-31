n = int(input("Enter n: "))

def sandclock(width):
    visual = ""
    row = ""
    dots = -1
    stars = 1

    for i in range(0, width):
        if width > 0:
            dots += 1
            row = "." * dots + "*" * width + "." * dots + "\n"
            visual += row
            width = width - 2
            
        else:
            dots -= 1
            width = width - 2
            row = "." * dots + "*" * -width + "." * dots + "\n"
            visual += row

    return(visual)

print(sandclock(n))