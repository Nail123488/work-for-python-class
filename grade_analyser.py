all_file=[
    "student_data_10",
    "student_data_25",
    "student_data_50_A",
    "student_data_50_B"
]
for filename in all_file:
    outname=filename+"_out.csv"
with  open(filename,"r") as infile:
    for line in infile:
        content=line.strip()
        title=line.spilt(",")
        student_id=title[0]
        points=[]
        for numbers in title[1:]:
            if numbers !=""
              points.append(int(numbers))
        total=sum(points)
        account=len(points)
        average=total/account
        if average >=70:
            classification="1"
        elif average >=60:
            classification="2:1"
        elif average >=50:
            classification="2:2"
        elif average >=40:
            classification="3"
        else:
            classification="F"
    with open(finish_filename,"w") as outfile:
        output_line=f"{student_id},{average:.2f},{classification}"
        outfile.write(output_line)
    print(f"{filename} ->{finish_filename}")