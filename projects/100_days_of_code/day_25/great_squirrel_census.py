import pandas

if __name__ == "__main__":
    data = pandas.read_csv("squirrel_census.csv")
    
    primary_fur_color = data["Primary Fur Color"].to_list()
    colors = set(primary_fur_color)
    color_count = {}
    for color in colors:
        color_count[str(color)] = primary_fur_color.count(color)
    
    print(color_count)
    color_dict = {"Colors": color_count.keys(),
                  "Amount": color_count.values()}
    
    file_data = pandas.DataFrame(color_dict)
    file_data.to_csv("squirrtel_count.csv", header=True)