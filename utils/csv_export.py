import os
import io
import csv
from flask import Response

def generate_csv(data):
    # Define the file path (you can change this to whatever directory you want)
    file_path = 'borrow_history.csv'
    
    # Open the file in write mode
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())  # Use keys from the first dict as headers
        writer.writeheader()
        writer.writerows(data)
    
    # Return a response with a link to the saved file (or you can send it back directly as you did before)
    return Response(f"CSV file has been saved to {file_path}. You can access it here.", status=200)























# import io
# import csv
# from flask import Response

# def generate_csv(data):
#     si = io.StringIO()
#     writer = csv.writer(si)
#     writer.writerow(data.keys())  # write headers
#     writer.writerows([data.values()])
#     output = si.getvalue()
#     return Response(output, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=history.csv"})



# import io
# import csv
# from flask import Response

# def generate_csv(data):
#     si = io.StringIO()
#     writer = csv.DictWriter(si, fieldnames=data[0].keys())  # Use keys from the first dict as headers
#     writer.writeheader()
#     writer.writerows(data)  # Write all rows
#     output = si.getvalue()
#     return Response(output, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=borrow_history.csv"})
